from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from github_api import GitHubAPI

app = Flask(__name__)
app.config['SECRET_KEY'] = 'baran-gurkan-secret-key-2024'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# GitHub API instance
github_api = GitHubAPI('barangurkan')

# Database Models
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    technologies = db.Column(db.String(200))
    github_url = db.Column(db.String(200))
    live_url = db.Column(db.String(200))
    image_url = db.Column(db.String(200))
    category = db.Column(db.String(50))  # AI, Backend, Full-Stack, etc.
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    stars = db.Column(db.Integer, default=0)
    forks = db.Column(db.Integer, default=0)
    language = db.Column(db.String(50))



class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    try:
        # GitHub'dan projeleri çek
        github_projects = github_api.get_user_repos(limit=15)
        
        # GitHub projelerini veritabanına kaydet (eğer yoksa)
        for gh_project in github_projects:
            try:
                existing_project = Project.query.filter_by(github_url=gh_project['github_url']).first()
                if not existing_project:
                    project = Project(
                        title=gh_project['title'],
                        description=gh_project['description'],
                        technologies=gh_project['technologies'],
                        github_url=gh_project['github_url'],
                        live_url=gh_project['live_url'],
                        image_url=gh_project['image_url'],
                        category=gh_project['category'],
                        created_at=gh_project['created_at'],
                        stars=gh_project['stars'],
                        forks=gh_project['forks'],
                        language=gh_project['language']
                    )
                    db.session.add(project)
            except Exception as e:
                print(f"Proje kaydedilirken hata: {e}")
                continue
        
        db.session.commit()
        
    except Exception as e:
        print(f"GitHub senkronizasyon hatası: {e}")
    
    # Tüm projeleri al
    all_projects = Project.query.order_by(Project.created_at.desc()).all()
    return render_template('projects.html', projects=all_projects)



@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

# API Routes
@app.route('/api/contact', methods=['POST'])
def submit_contact():
    try:
        data = request.get_json()
        new_contact = Contact(
            name=data['name'],
            email=data['email'],
            message=data['message']
        )
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Mesajınız başarıyla gönderildi!'})
    except Exception as e:
        return jsonify({'success': False, 'message': 'Bir hata oluştu. Lütfen tekrar deneyin.'}), 500

@app.route('/api/projects')
def get_projects():
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return jsonify([{
        'id': p.id,
        'title': p.title,
        'description': p.description,
        'technologies': p.technologies,
        'github_url': p.github_url,
        'live_url': p.live_url,
        'image_url': p.image_url,
        'category': p.category,
        'created_at': p.created_at.isoformat(),
        'stars': p.stars,
        'forks': p.forks,
        'language': p.language
    } for p in projects])

@app.route('/api/github-projects')
def get_github_projects():
    """GitHub'dan projeleri getir"""
    try:
        projects = github_api.get_user_repos(limit=15)
        return jsonify(projects)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/github-user')
def get_github_user():
    """GitHub kullanıcı bilgilerini getir"""
    try:
        user_info = github_api.get_user_info()
        return jsonify(user_info)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/update-demo-link', methods=['POST'])
def update_demo_link():
    """Demo link güncelle"""
    try:
        data = request.get_json()
        github_url = data.get('github_url')
        demo_url = data.get('demo_url')
        
        if not github_url or not demo_url:
            return jsonify({'success': False, 'message': 'GitHub URL ve Demo URL gerekli!'}), 400
        
        # Projeyi bul ve güncelle
        project = Project.query.filter_by(github_url=github_url).first()
        if project:
            project.live_url = demo_url
            db.session.commit()
            return jsonify({'success': True, 'message': 'Demo link güncellendi!'})
        else:
            return jsonify({'success': False, 'message': 'Proje bulunamadı!'}), 404
            
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500



# Admin routes for adding sample data
@app.route('/admin/init')
def init_data():
    # Sample projects
    sample_projects = [
        {
            'title': 'AI Chatbot Projesi',
            'description': 'Python ve TensorFlow kullanarak geliştirdiğim yapay zeka tabanlı chatbot. Doğal dil işleme ve makine öğrenmesi teknikleri kullanılarak oluşturuldu.',
            'technologies': 'Python, TensorFlow, NLP, Flask',
            'github_url': 'https://github.com/barangurkan/ai-chatbot',
            'live_url': 'https://ai-chatbot-demo.herokuapp.com',
            'image_url': '/static/images/ai-chatbot.jpg',
            'category': 'AI'
        },
        {
            'title': 'Backend API Sistemi',
            'description': 'RESTful API geliştirme projesi. Django REST Framework kullanarak ölçeklenebilir backend sistemi oluşturdum.',
            'technologies': 'Python, Django, PostgreSQL, Docker',
            'github_url': 'https://github.com/barangurkan/backend-api',
            'live_url': 'https://api-demo.herokuapp.com',
            'image_url': '/static/images/backend-api.jpg',
            'category': 'Backend'
        },
        {
            'title': 'Machine Learning Dashboard',
            'description': 'Veri analizi ve makine öğrenmesi sonuçlarını görselleştiren interaktif dashboard.',
            'technologies': 'Python, Scikit-learn, Plotly, Dash',
            'github_url': 'https://github.com/barangurkan/ml-dashboard',
            'live_url': 'https://ml-dashboard.herokuapp.com',
            'image_url': '/static/images/ml-dashboard.jpg',
            'category': 'AI'
        }
    ]
    
    for project_data in sample_projects:
        project = Project(**project_data)
        db.session.add(project)
    
    db.session.commit()
    return 'Sample data initialized!'

@app.route('/admin/sync-github')
def sync_github():
    """GitHub'dan projeleri senkronize et"""
    try:
        github_projects = github_api.get_user_repos(limit=15)
        
        for gh_project in github_projects:
            existing_project = Project.query.filter_by(github_url=gh_project['github_url']).first()
            if not existing_project:
                project = Project(
                    title=gh_project['title'],
                    description=gh_project['description'],
                    technologies=gh_project['technologies'],
                    github_url=gh_project['github_url'],
                    live_url=gh_project['live_url'],
                    image_url=gh_project['image_url'],
                    category=gh_project['category'],
                    created_at=gh_project['created_at'],
                    stars=gh_project['stars'],
                    forks=gh_project['forks'],
                    language=gh_project['language']
                )
                db.session.add(project)
        
        db.session.commit()
        return f'GitHub\'dan {len(github_projects)} proje senkronize edildi!'
    except Exception as e:
        return f'Hata: {str(e)}', 500

if __name__ == '__main__':
    with app.app_context():
        # Veritabanını oluştur
        db.create_all()
        print("✅ Veritabanı başarıyla oluşturuldu!")
        print("📊 Tablolar oluşturuldu:")
        print("   - Project (projeler)")
        print("   - BlogPost (blog yazıları)")
        print("   - Contact (iletişim mesajları)")
    app.run(debug=False, host='127.0.0.1', port=5000) 
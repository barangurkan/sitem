from app import app, db, Project, BlogPost

with app.app_context():
    # Veritabanını oluştur
    db.create_all()
    print("Veritabanı oluşturuldu!")
    
    # Örnek projeleri ekle
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
    
    # Örnek blog yazılarını ekle
    sample_posts = [
        {
            'title': 'Yapay Zeka ve Geleceğimiz',
            'content': 'Yapay zeka teknolojilerinin günlük hayatımıza etkileri ve gelecekte bizi bekleyen değişiklikler hakkında düşüncelerim...',
            'excerpt': 'AI teknolojilerinin gelişimi ve topluma etkileri',
            'tags': 'AI, Technology, Future'
        },
        {
            'title': 'Python Backend Geliştirme İpuçları',
            'content': 'Python ile backend geliştirirken dikkat edilmesi gereken noktalar ve best practice\'ler...',
            'excerpt': 'Python backend geliştirme rehberi',
            'tags': 'Python, Backend, Development'
        }
    ]
    
    for post_data in sample_posts:
        post = BlogPost(**post_data)
        db.session.add(post)
    
    db.session.commit()
    print("Örnek veriler eklendi!")
    print("Projeler:", Project.query.count())
    print("Blog yazıları:", BlogPost.query.count()) 
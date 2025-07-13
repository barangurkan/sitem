from app import app, db, Project
from github_api import GitHubAPI

def sync_github_projects():
    """GitHub'dan projeleri senkronize et"""
    github_api = GitHubAPI('barangurkan')
    
    with app.app_context():
        try:
            # GitHub'dan projeleri çek
            github_projects = github_api.get_user_repos(limit=15)
            print(f"GitHub'dan {len(github_projects)} proje bulundu.")
            
            added_count = 0
            updated_count = 0
            
            for gh_project in github_projects:
                existing_project = Project.query.filter_by(github_url=gh_project['github_url']).first()
                
                if not existing_project:
                    # Yeni proje ekle
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
                    added_count += 1
                    print(f"✅ Yeni proje eklendi: {gh_project['title']}")
                else:
                    # Mevcut projeyi güncelle
                    existing_project.stars = gh_project['stars']
                    existing_project.forks = gh_project['forks']
                    existing_project.description = gh_project['description']
                    existing_project.technologies = gh_project['technologies']
                    existing_project.live_url = gh_project['live_url']
                    updated_count += 1
                    print(f"🔄 Proje güncellendi: {gh_project['title']}")
            
            db.session.commit()
            print(f"\n🎉 Senkronizasyon tamamlandı!")
            print(f"📥 Yeni eklenen: {added_count}")
            print(f"🔄 Güncellenen: {updated_count}")
            print(f"📊 Toplam proje: {Project.query.count()}")
            
        except Exception as e:
            print(f"❌ Hata: {str(e)}")

if __name__ == '__main__':
    sync_github_projects() 
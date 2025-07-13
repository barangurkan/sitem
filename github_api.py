import requests
import os
from datetime import datetime
from typing import List, Dict

class GitHubAPI:
    def __init__(self, username: str, token: str = None):
        self.username = username
        self.token = token
        self.base_url = "https://api.github.com"
        
        # Headers for API requests
        self.headers = {}
        if token:
            self.headers['Authorization'] = f'token {token}'
        self.headers['Accept'] = 'application/vnd.github.v3+json'
    
    def get_user_repos(self, limit: int = 10) -> List[Dict]:
        """Kullanıcının repository'lerini getir"""
        url = f"{self.base_url}/users/{self.username}/repos"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            repos = response.json()
            
            # En son güncellenen repo'ları al
            repos.sort(key=lambda x: x.get('updated_at', ''), reverse=True)
            
            projects = []
            for repo in repos[:limit]:
                # Fork olmayan repo'ları al
                if not repo.get('fork', False):
                    try:
                        project = self._format_repo_to_project(repo)
                        if project:
                            projects.append(project)
                    except Exception as e:
                        print(f"Repo işlenirken hata: {repo.get('name', 'Unknown')} - {e}")
                        continue
            
            return projects
            
        except requests.RequestException as e:
            print(f"GitHub API hatası: {e}")
            return []
        except Exception as e:
            print(f"Beklenmeyen hata: {e}")
            return []
    
    def _format_repo_to_project(self, repo: Dict) -> Dict:
        """Repository'yi proje formatına çevir"""
        # Repo adından kategori belirle
        category = self._determine_category(repo)
        
        # Demo URL'si oluştur (GitHub Pages varsa)
        demo_url = None
        
        # 1. Önce repo'nun homepage alanını kontrol et
        if repo.get('homepage'):
            demo_url = repo['homepage']
        # 2. GitHub Pages aktif mi kontrol et
        elif repo.get('has_pages', False):
            demo_url = f"https://{self.username}.github.io/{repo['name']}"
        # 3. Demo config'den demo linkini al
        else:
            try:
                from demo_config import get_demo_url
                repo_name = repo['name'].lower()
                demo_url = get_demo_url(repo_name)
            except ImportError:
                demo_url = None
        
        # 4. Eğer hala demo URL yoksa, GitHub Pages URL'sini dene
        if not demo_url:
            potential_pages_url = f"https://{self.username}.github.io/{repo['name']}"
            # Bu URL'nin çalışıp çalışmadığını kontrol etmek için basit bir test yapabiliriz
            # Şimdilik sadece URL'yi oluşturalım
            demo_url = potential_pages_url
        
        # Teknolojileri belirle (README'den veya repo adından)
        technologies = self._extract_technologies(repo)
        
        return {
            'title': repo['name'].replace('-', ' ').replace('_', ' ').title(),
            'description': repo.get('description') or 'Açıklama bulunmuyor.',
            'technologies': technologies,
            'github_url': repo['html_url'],
            'live_url': demo_url,
            'image_url': None,  # GitHub'dan resim çekemeyiz
            'category': category,
            'created_at': datetime.fromisoformat(repo['created_at'].replace('Z', '+00:00')),
            'updated_at': datetime.fromisoformat(repo['updated_at'].replace('Z', '+00:00')),
            'stars': repo.get('stargazers_count', 0),
            'forks': repo.get('forks_count', 0),
            'language': repo.get('language', 'Unknown')
        }
    
    def _determine_category(self, repo: Dict) -> str:
        """Repo adı ve açıklamasından kategori belirle"""
        name = repo['name'].lower()
        description = repo.get('description', '') or ''
        description = description.lower()
        
        # AI/ML kategorisi
        ai_keywords = ['ai', 'ml', 'machine-learning', 'deep-learning', 'tensorflow', 'pytorch', 'neural', 'nlp', 'chatbot']
        if any(keyword in name or keyword in description for keyword in ai_keywords):
            return 'AI'
        
        # Backend kategorisi
        backend_keywords = ['api', 'backend', 'server', 'django', 'flask', 'fastapi', 'rest']
        if any(keyword in name or keyword in description for keyword in backend_keywords):
            return 'Backend'
        
        # Data Science kategorisi
        data_keywords = ['data', 'analysis', 'pandas', 'numpy', 'plotly', 'dashboard']
        if any(keyword in name or keyword in description for keyword in data_keywords):
            return 'Data'
        
        # Full-Stack kategorisi
        fullstack_keywords = ['web', 'app', 'website', 'frontend', 'react', 'vue', 'angular']
        if any(keyword in name or keyword in description for keyword in fullstack_keywords):
            return 'Full-Stack'
        
        # Varsayılan olarak Backend
        return 'Backend'
    
    def _extract_technologies(self, repo: Dict) -> str:
        """Repo'dan teknolojileri çıkar"""
        name = repo['name'].lower()
        description = repo.get('description', '') or ''
        description = description.lower()
        language = repo.get('language', '') or ''
        language = language.lower()
        
        technologies = []
        
        # Ana dil
        if language:
            technologies.append(language.title())
        
        # Framework'ler
        frameworks = {
            'django': 'Django',
            'flask': 'Flask',
            'fastapi': 'FastAPI',
            'react': 'React',
            'vue': 'Vue.js',
            'angular': 'Angular',
            'tensorflow': 'TensorFlow',
            'pytorch': 'PyTorch',
            'scikit': 'Scikit-learn',
            'pandas': 'Pandas',
            'numpy': 'NumPy'
        }
        
        for keyword, tech in frameworks.items():
            if keyword in name or keyword in description:
                technologies.append(tech)
        
        # Özel teknolojiler
        if 'api' in name or 'api' in description:
            technologies.append('REST API')
        if 'docker' in name or 'docker' in description:
            technologies.append('Docker')
        if 'postgres' in name or 'postgres' in description:
            technologies.append('PostgreSQL')
        if 'redis' in name or 'redis' in description:
            technologies.append('Redis')
        
        return ', '.join(technologies) if technologies else 'Python'
    
    def get_user_info(self) -> Dict:
        """Kullanıcı bilgilerini getir"""
        url = f"{self.base_url}/users/{self.username}"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            user_data = response.json()
            
            return {
                'name': user_data.get('name', self.username),
                'bio': user_data.get('bio', ''),
                'location': user_data.get('location', ''),
                'public_repos': user_data.get('public_repos', 0),
                'followers': user_data.get('followers', 0),
                'following': user_data.get('following', 0),
                'avatar_url': user_data.get('avatar_url', ''),
                'blog': user_data.get('blog', ''),
                'company': user_data.get('company', ''),
                'created_at': user_data.get('created_at', ''),
                'updated_at': user_data.get('updated_at', '')
            }
            
        except requests.RequestException as e:
            print(f"GitHub API hatası: {e}")
            return {} 
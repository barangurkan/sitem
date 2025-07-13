import requests
import json
from github_api import GitHubAPI

def check_github_pages_status(username, repo_name):
    """GitHub Pages durumunu kontrol et"""
    
    # GitHub API endpoint
    url = f"https://api.github.com/repos/{username}/{repo_name}/pages"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            pages_info = response.json()
            print(f"✅ GitHub Pages Aktif: {repo_name}")
            print(f"   URL: {pages_info.get('html_url', 'N/A')}")
            print(f"   Source: {pages_info.get('source', {}).get('branch', 'N/A')}")
            print(f"   Status: {pages_info.get('status', 'N/A')}")
            return True
        elif response.status_code == 404:
            print(f"❌ GitHub Pages Aktif Değil: {repo_name}")
            return False
        else:
            print(f"⚠️  Hata: {response.status_code} - {repo_name}")
            return False
            
    except Exception as e:
        print(f"❌ Hata: {e}")
        return False

def check_repo_pages_url(username, repo_name):
    """Repo'nun GitHub Pages URL'sini test et"""
    pages_url = f"https://{username}.github.io/{repo_name}"
    
    try:
        response = requests.get(pages_url, timeout=10)
        if response.status_code == 200:
            print(f"✅ URL Çalışıyor: {pages_url}")
            return True
        else:
            print(f"❌ URL Çalışmıyor: {pages_url} (Status: {response.status_code})")
            return False
    except Exception as e:
        print(f"❌ URL Hatası: {pages_url} - {e}")
        return False

def main():
    username = "barangurkan"
    
    # Test edilecek repo'lar
    test_repos = [
        "kendi-sitem",
        "portfolio", 
        "personal-website",
        "demo-project"
    ]
    
    print("🔍 GitHub Pages Durumu Kontrol Ediliyor...\n")
    
    for repo in test_repos:
        print(f"📁 Repo: {repo}")
        print("-" * 50)
        
        # GitHub Pages API kontrolü
        pages_active = check_github_pages_status(username, repo)
        
        # URL testi
        url_works = check_repo_pages_url(username, repo)
        
        if pages_active and url_works:
            print(f"🎉 {repo} için GitHub Pages tamamen aktif!")
        elif pages_active:
            print(f"⚠️  {repo} için GitHub Pages aktif ama URL çalışmıyor")
        else:
            print(f"❌ {repo} için GitHub Pages aktif değil")
        
        print("\n")

if __name__ == "__main__":
    main() 
# Demo Link Yapılandırması
# Bu dosyada projelerin demo linklerini tanımlayabilirsin

DEMO_LINKS = {
    # GitHub repo adı: Demo URL
    'ai-chatbot': 'https://ai-chatbot-demo.herokuapp.com',
    'backend-api': 'https://api-demo.herokuapp.com',
    'ml-dashboard': 'https://ml-dashboard.herokuapp.com',
    'yapay_zeka': 'https://yapay-zeka-demo.vercel.app',
    'yorum_analiz': 'https://yorum-analiz.herokuapp.com',
    'deprem': 'https://deprem-takip.vercel.app',
    'pythonproject': 'https://python-project-demo.netlify.app',
    'parola': 'https://parola-generator.vercel.app',
    
    # GitHub Pages demo linkleri
    'kendi-sitem': 'https://barangurkan.github.io/kendi-sitem',
    'portfolio': 'https://barangurkan.github.io/portfolio',
    'personal-website': 'https://barangurkan.github.io/personal-website',
    'demo-project': 'https://barangurkan.github.io/demo-project',
    
    # Yeni projeler ekleyebilirsin
    # 'proje-adi': 'https://demo-link.com',
}

# Demo platformları ve örnek URL'ler
DEMO_PLATFORMS = {
    'Vercel': 'https://proje-adi.vercel.app',
    'Netlify': 'https://proje-adi.netlify.app',
    'Heroku': 'https://proje-adi.herokuapp.com',
    'Railway': 'https://proje-adi.railway.app',
    'Render': 'https://proje-adi.onrender.com',
    'GitHub Pages': 'https://barangurkan.github.io/proje-adi',
    'Custom Domain': 'https://proje-adi.com',
}

def get_demo_url(repo_name: str) -> str:
    """Repo adından demo URL'sini al"""
    return DEMO_LINKS.get(repo_name.lower(), None)

def add_demo_link(repo_name: str, demo_url: str):
    """Yeni demo link ekle"""
    DEMO_LINKS[repo_name.lower()] = demo_url
    print(f"✅ Demo link eklendi: {repo_name} -> {demo_url}")

def list_demo_links():
    """Tüm demo linkleri listele"""
    print("📋 Mevcut Demo Linkler:")
    for repo, url in DEMO_LINKS.items():
        print(f"   {repo}: {url}")

if __name__ == '__main__':
    list_demo_links() 
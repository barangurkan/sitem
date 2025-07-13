# Baran Gürkan - Kişisel Web Sitesi

Modern ve profesyonel kişisel web sitesi. Yapay zeka ve backend geliştirme konularında uzmanlaşmış bir bilgisayar mühendisinin portföy sitesi.

## 🚀 Özellikler

- **Modern Tasarım**: Bootstrap 5 ve özel CSS ile responsive tasarım
- **Flask Backend**: Python Flask framework ile güçlü backend
- **SQLite Veritabanı**: Projeler ve blog yazıları için veritabanı
- **İletişim Formu**: AJAX ile çalışan iletişim formu
- **Proje Filtreleme**: Kategorilere göre proje filtreleme
- **Blog Sistemi**: Blog yazıları için tam sistem
- **API Endpoints**: RESTful API desteği

## 🛠️ Teknolojiler

- **Backend**: Python, Flask, SQLAlchemy
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Veritabanı**: SQLite
- **İkonlar**: Font Awesome
- **Fontlar**: Google Fonts (Inter)

## 📋 Kurulum

### Gereksinimler

- Python 3.8+
- pip (Python paket yöneticisi)

### Adımlar

1. **Projeyi klonlayın:**
```bash
git clone <repository-url>
cd kendi-sitem
```

2. **Sanal ortam oluşturun:**
```bash
python -m venv venv
```

3. **Sanal ortamı aktifleştirin:**
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

4. **Bağımlılıkları yükleyin:**
```bash
pip install -r requirements.txt
```

5. **Uygulamayı çalıştırın:**
```bash
python app.py
```

6. **Tarayıcıda açın:**
```
http://localhost:5000
```

## 📁 Proje Yapısı

```
kendi-sitem/
├── app.py                 # Ana Flask uygulaması
├── requirements.txt       # Python bağımlılıkları
├── README.md             # Bu dosya
├── templates/            # HTML template'leri
│   ├── base.html         # Ana template
│   ├── index.html        # Ana sayfa
│   ├── about.html        # Hakkımda sayfası
│   ├── projects.html     # Projeler sayfası
│   ├── blog.html         # Blog sayfası
│   └── contact.html      # İletişim sayfası
└── static/               # Statik dosyalar (CSS, JS, resimler)
    ├── css/
    ├── js/
    └── images/
```

## 🎯 Sayfalar

### Ana Sayfa (`/`)
- Hero section ile tanıtım
- Uzmanlık alanları
- Öne çıkan projeler
- Çağrı-to-action

### Hakkımda (`/about`)
- Kişisel bilgiler
- Deneyim geçmişi
- Eğitim bilgileri
- Teknik beceriler

### Projeler (`/projects`)
- Proje listesi
- Kategori filtreleme
- Proje detayları
- GitHub ve demo linkleri

### Blog (`/blog`)
- Blog yazıları listesi
- Kategoriler
- Newsletter aboneliği

### İletişim (`/contact`)
- İletişim formu
- İletişim bilgileri
- Hizmetler
- SSS

## 🔧 API Endpoints

### İletişim Formu
```
POST /api/contact
Content-Type: application/json

{
    "name": "Ad Soyad",
    "email": "email@example.com",
    "message": "Mesaj içeriği"
}
```

### Projeler
```
GET /api/projects
```

### Blog Yazıları
```
GET /api/blog
```

## 📊 Veritabanı Modelleri

### Project
- id (Primary Key)
- title (String)
- description (Text)
- technologies (String)
- github_url (String)
- live_url (String)
- image_url (String)
- category (String)
- created_at (DateTime)

### BlogPost
- id (Primary Key)
- title (String)
- content (Text)
- excerpt (String)
- tags (String)
- created_at (DateTime)

### Contact
- id (Primary Key)
- name (String)
- email (String)
- message (Text)
- created_at (DateTime)

## 🎨 Özelleştirme

### Renkler
CSS değişkenlerini `templates/base.html` dosyasında düzenleyebilirsiniz:

```css
:root {
    --primary-color: #6366f1;
    --secondary-color: #8b5cf6;
    --accent-color: #06b6d4;
    --dark-bg: #0f172a;
    --light-bg: #f8fafc;
    --text-primary: #1e293b;
    --text-secondary: #64748b;
}
```

### İçerik
- Projeleri `app.py` dosyasındaki `init_data()` fonksiyonunda düzenleyin
- Blog yazılarını aynı dosyada ekleyin
- Kişisel bilgileri template dosyalarında güncelleyin

## 🚀 Deployment

### Heroku
1. Heroku CLI'yi yükleyin
2. `Procfile` oluşturun:
```
web: gunicorn app:app
```
3. `gunicorn` ekleyin:
```bash
pip install gunicorn
```
4. Deploy edin:
```bash
heroku create
git push heroku main
```

### VPS/Dedicated Server
1. Nginx kurun
2. Gunicorn ile çalıştırın
3. SSL sertifikası ekleyin

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 🤝 Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit edin (`git commit -m 'Add amazing feature'`)
4. Push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📞 İletişim

Baran Gürkan - [baran@example.com](mailto:baran@example.com)

Proje Linki: [https://github.com/barangurkan/kendi-sitem](https://github.com/barangurkan/kendi-sitem) 
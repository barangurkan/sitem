# 🚀 GitHub Pages Aktif Etme Rehberi

## 📋 Adım Adım GitHub Pages Kurulumu

### 1. GitHub Repository Ayarları

1. **GitHub'da projenize gidin**
   - `https://github.com/barangurkan/kendi-sitem` adresine gidin

2. **Settings sekmesine tıklayın**
   - Repository sayfasında üst menüden "Settings" seçin

3. **Pages bölümünü bulun**
   - Sol menüden "Pages" seçeneğini tıklayın

4. **Source ayarlarını yapın**
   - **Source** bölümünde "Deploy from a branch" seçin
   - **Branch** olarak "main" seçin
   - **Folder** olarak "/ (root)" seçin
   - **Save** butonuna tıklayın

### 2. index.html Dosyası Oluşturma

Projenizin ana dizininde `index.html` dosyası olmalı. Bu dosya zaten oluşturuldu.

### 3. GitHub Actions ile Otomatik Deploy (Opsiyonel)

`.github/workflows/deploy.yml` dosyası oluşturuldu. Bu sayede:
- Her push'ta otomatik deploy
- Static dosyalar otomatik oluşturulur
- GitHub Pages'e otomatik yüklenir

### 4. Demo Link Yönetimi

`demo_config.py` dosyasında GitHub Pages URL'leri tanımlandı:

```python
DEMO_LINKS = {
    'kendi-sitem': 'https://barangurkan.github.io/kendi-sitem',
    'portfolio': 'https://barangurkan.github.io/portfolio',
    # ... diğer projeler
}
```

### 5. Kontrol Scripti

GitHub Pages durumunu kontrol etmek için:

```bash
python check_github_pages.py
```

## 🔧 GitHub Pages URL Formatı

GitHub Pages URL'leri şu formatta olur:
```
https://{username}.github.io/{repository-name}
```

Örnek:
- `https://barangurkan.github.io/kendi-sitem`
- `https://barangurkan.github.io/portfolio`

## 📝 Önemli Notlar

### GitHub Pages Gereksinimleri:
1. **Repository public olmalı** (ücretsiz hesaplar için)
2. **index.html dosyası** ana dizinde olmalı
3. **Branch seçimi** doğru olmalı (genellikle main/master)
4. **Deploy süresi** 5-10 dakika sürebilir

### Sık Karşılaşılan Sorunlar:

1. **404 Hatası**
   - index.html dosyasının ana dizinde olduğundan emin olun
   - Branch adının doğru olduğunu kontrol edin

2. **Deploy Başarısız**
   - GitHub Actions loglarını kontrol edin
   - Repository ayarlarını tekrar kontrol edin

3. **URL Çalışmıyor**
   - Deploy'ın tamamlanmasını bekleyin (5-10 dakika)
   - Cache'i temizleyin (Ctrl+F5)

## 🎯 Hızlı Test

GitHub Pages'in çalışıp çalışmadığını test etmek için:

1. **Tarayıcıda açın:**
   ```
   https://barangurkan.github.io/kendi-sitem
   ```

2. **Kontrol scripti çalıştırın:**
   ```bash
   python check_github_pages.py
   ```

3. **Admin panelinden kontrol edin:**
   ```
   http://localhost:5000/admin
   ```

## 🚀 Sonraki Adımlar

1. **GitHub Pages aktif olduktan sonra:**
   - Demo linklerini admin panelinden güncelleyin
   - Projeleri yeniden senkronize edin

2. **Custom domain eklemek için:**
   - Domain sahibi olun
   - DNS ayarlarını yapın
   - GitHub repository ayarlarından custom domain ekleyin

3. **SSL sertifikası:**
   - GitHub Pages otomatik olarak SSL sağlar
   - Custom domain için de SSL otomatik olarak eklenir

## 📞 Yardım

Eğer sorun yaşıyorsanız:

1. **GitHub Pages dokümantasyonu:** https://pages.github.com/
2. **GitHub Actions dokümantasyonu:** https://docs.github.com/en/actions
3. **Repository ayarları:** Settings > Pages

---

**Not:** GitHub Pages ücretsiz hesaplar için sadece public repository'lerde çalışır. Private repository'ler için GitHub Pro gerekir. 
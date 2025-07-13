from app import app, db

with app.app_context():
    # Veritabanını oluştur
    db.create_all()
    print("✅ Veritabanı başarıyla oluşturuldu!")
    print("📊 Tablolar:")
    print("   - Project (projeler)")
    print("   - BlogPost (blog yazıları)")
    print("   - Contact (iletişim mesajları)")
    print("\n🚀 Artık uygulamayı çalıştırabilirsin!") 
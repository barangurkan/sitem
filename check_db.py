import sqlite3
import os

def check_database():
    """Veritabanı yapısını kontrol et"""
    db_paths = [
        'portfolio.db',
        'instance/portfolio.db',
        'app.db'
    ]
    
    for db_path in db_paths:
        if os.path.exists(db_path):
            print(f"📁 Veritabanı bulundu: {db_path}")
            try:
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                
                # Tabloları listele
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = cursor.fetchall()
                print(f"📊 Tablolar: {[table[0] for table in tables]}")
                
                # Project tablosunun yapısını kontrol et
                if any('project' in table[0].lower() for table in tables):
                    cursor.execute("PRAGMA table_info(project);")
                    columns = cursor.fetchall()
                    print("🔍 Project tablosu sütunları:")
                    for col in columns:
                        print(f"   - {col[1]} ({col[2]})")
                
                conn.close()
                return db_path
                
            except Exception as e:
                print(f"❌ Hata: {e}")
    
    print("❌ Hiçbir veritabanı bulunamadı!")
    return None

if __name__ == '__main__':
    check_database() 
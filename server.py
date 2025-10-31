from flask import Flask, request
import sqlite3
from pyngrok import ngrok, conf

# Ngrok yolunu tanımla (ngrok.exe'nin tam yolu)
conf.get_default().ngrok_path = "C:\\Users\\Arslan\\Desktop\\database\\ngrok.exe"

# Flask uygulaması
app = Flask(__name__)

# Veritabanı oluştur
def init_db():
    conn = sqlite3.connect('veriler.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS veriler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isim TEXT,
            veri TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Veri alma endpoint'i
@app.route('/gonder', methods=['POST'])
def veri_al():
    isim = request.form.get('isim')
    veri = request.form.get('veri')

    if not isim or not veri:
        return "Eksik veri", 400

    with sqlite3.connect('veriler.db') as conn:
        c = conn.cursor()
        c.execute('INSERT INTO veriler (isim, veri) VALUES (?, ?)', (isim, veri))
        conn.commit()

    return "Veri kaydedildi", 200

# Sunucuyu başlat ve Ngrok tünelini aç
if __name__ == '__main__':
    public_url = ngrok.connect(5000)
    print("Ngrok URL'si:", public_url)
    app.run(port=5000)

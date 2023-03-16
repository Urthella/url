import requests
from bs4 import BeautifulSoup

url = 'www.google.com' # İçerik alınacak URL adresi ve aranacak anahtar kelimeler değişkenleri
keywords = ['login', 'password', 'secret']

response = requests.get(url) # URL adresinden içerik al

if response.status_code == 200: # HTTP yanıt kodunu kontrol et
    # Anahtar kelimeleri ara
    for keyword in keywords:
        if keyword in response.text:
            print("Web sitesinde", keyword, "kelimesi bulundu!")

    soup = BeautifulSoup(response.content, 'html.parser')  # Web sayfasının kaynak kodunu analiz et
    forms = soup.find_all('form')

    if len(forms) > 0:     # Formlar varsa, form verileri için HTTP POST isteği gönder
        print("Web sayfasında", len(forms), "adet form bulundu!")
        for form in forms:
            form_data = {}
            inputs = form.find_all('input')
            for input in inputs:
                if input.has_attr('name'):
                    form_data[input['name']] = input.get('value', '')

            post_response = requests.post(url, data=form_data)  # HTTP POST isteği gönder
            print("Form gönderildi:", post_response.status_code)

else:
    print("URL adresine erişilemedi.")

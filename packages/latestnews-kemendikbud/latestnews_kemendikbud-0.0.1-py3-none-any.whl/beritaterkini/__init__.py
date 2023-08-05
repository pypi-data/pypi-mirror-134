import requests
from bs4 import BeautifulSoup

"""
berita terkini dari laman kemendikbud
"""

def ekstraksi_data():
    try:
        content = requests.get('https://kemdikbud.go.id/main/blog/category/berita')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        #print(soup.prettify())
        judul = soup.find('strong')
        judul = judul.text

        waktu = soup.find('span', {'class': 'date'})
        waktu = waktu.text.split(', ')
        tanggal = waktu[0]

        hasil = dict()
        hasil ['judul'] = judul
        hasil ['waktu'] = tanggal

        return hasil


def tampilkan_hasil(result):
    print('Berita Terkini dari Laman Kemendikbud')
    print(f"Judul Berita ={result['judul']}")
    print(f"Waktu Terbit ={result['waktu']}")

if __name__ == '__main__':
    result = ekstraksi_data()
    tampilkan_hasil(result)
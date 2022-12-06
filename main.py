import requests
from bs4 import BeautifulSoup
from Funzioni import FindMatch

DAY = input()
N_PARITE = 10
DIFFERENZA = 0.3

URL = "https://www.soccerstats.com/matches.asp?matchday=" + str(DAY) + "&listing=1"
URL_BASE = "https://www.soccerstats.com/"

response = requests.get(URL, timeout=10)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    rows = soup.find("table", {"id": "btable"}).find("tbody").find_all("tr")
    for row in rows:
        risultato = FindMatch(row, URL_BASE, N_PARITE, DIFFERENZA)
        if risultato != '':
            print(risultato)
else:
    print('Errore nella risposta riprovare')

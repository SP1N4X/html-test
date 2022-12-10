import requests
from bs4 import BeautifulSoup
from Funzioni import FindMatch
import datetime

DAY = input()
giorno = (datetime.datetime.today() + datetime.timedelta(days=int(DAY)-1)).strftime('%d-%m-%Y')
open(f'{giorno}.txt', 'w')

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
            with open(f'{giorno}.txt', 'a') as f:
                f.write(risultato)
            print(risultato)
else:
    print('Errore nella risposta riprovare')

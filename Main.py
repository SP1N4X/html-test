import requests
from bs4 import BeautifulSoup
from Funzioni import FindMatch
import datetime


day = input()
giorno = (datetime.datetime.today() + datetime.timedelta(days=int(day)-1)).strftime('%d/%m/%Y')
open(f'{giorno}.txt', 'w').close()

n_partite = 10
differenza = 0.3

url = "https://www.soccerstats.com/matches.asp?matchday=" + str(day) + "&listing=1"
url_base = "https://www.soccerstats.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    rows = soup.find("table", {"id": "btable"}).find("tbody").find_all("tr")
    for row in rows:
        risultato = FindMatch(row, url_base, n_partite, differenza)
        if risultato != '':
            with open(f'{giorno}.txt', 'a') as f:
                f.write(risultato)
            print(risultato)
else:          
    print('Errore nella risposta riprovare') 
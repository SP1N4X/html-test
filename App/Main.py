import requests
from bs4 import BeautifulSoup
from Funzioni import FindMatch

day = 2
n_partite = 10
differenza = 2

url = "https://www.soccerstats.com/matches.asp?matchday=" + str(day) + "&listing=1"
url_base = "https://www.soccerstats.com/"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
rows = soup.find("table", {"id": "btable"}).find("tbody").find_all("tr")
for row in rows:
    risultato = FindMatch(row, url_base, n_partite, differenza)
    if risultato != '':
        print(risultato)
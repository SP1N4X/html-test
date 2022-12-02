from bs4 import BeautifulSoup

def TrovaCampionato(soup):
    try:
        campionato = soup.find("div", {"id": "content"}).find_all('div')[0].find_all('div')[1].find('h1').text
        return campionato
    except:
        return 'Campionato non trovato'
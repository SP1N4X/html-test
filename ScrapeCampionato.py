def TrovaCampionato(soup):
    try:
        campionato = soup.find("div", {"id": "content"}).find_all('div')[1].find_all('div')[1].find('font').text
        return campionato
    except:
        return 'Campionato non trovato'
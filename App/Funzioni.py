import requests
from bs4 import BeautifulSoup
from ScrapeCorner import Corner
from ScrapeHTGoal import HTGoal
from ScrapeCalcoloRisultato import CalcoloRisultato 


def ScrivereStringaCompleta(casa, tras, orario, campionato, stringaRisultato, avgCornerString, goalHTString):
    if stringaRisultato != '' or avgCornerString != '' or goalHTString != '':
        stringa = casa + ' - ' + tras + '    ' + orario + '\n(' + campionato + ')' + '\n'
        if stringaRisultato != '':
            stringa = stringa + stringaRisultato
        if avgCornerString != '':
            stringa = stringa + avgCornerString
        if goalHTString != '':
            stringa = stringa + goalHTString

        return stringa
    else:
        return ''

def FindMatch(row, url_base, n_partite, differenza):
    dati = row.find_all("td")

    partite_casa = dati[7].text
    partite_tras = dati[13].text
    if partite_casa != "" and int(partite_casa) >= n_partite and partite_tras != "" and int(partite_tras) >= n_partite:
        casa = dati[9].text
        tras = dati[11].text
        orario = dati[10].find("font").text
        link = dati[0].find("a", href=True)['href']

        if link != None:
            try:
                responseLink = requests.get(url_base + link)
                soupLink = BeautifulSoup(responseLink.content, 'html.parser')     
            except:
                campionato = 'Campionato non trovato'
                avgCornerString = ''
                goalHTString = ''
            try:
                campionato = TrovaCampionato(soupLink)    
            except:
                campionato = 'Campionato non trovato'
            try:
                avgCornerString = Corner(soupLink, differenza)
            except:
                avgCornerString = ''     
            try:
                goalHTString = HTGoal(soupLink, partite_casa, partite_tras, differenza)
            except:
                goalHTString = ''
        else:
            campionato = 'Campionato non trovato'
            avgCornerString = ''
            goalHTString = '' 
        

        g_subiti_casa = dati[3].text
        g_fatti_casa = dati[4].text
        g_subiti_tra = dati[17].text
        g_fatti_tra = dati[16].text

        if g_subiti_casa != "" and g_fatti_casa != "" and g_subiti_tra != "" and g_fatti_tra != "":
            stringaRisultato = CalcoloRisultato(g_subiti_casa, g_fatti_casa, g_subiti_tra, g_fatti_tra, differenza)
        else:
            stringaRisultato = ''
        
        stringaCompleta = ScrivereStringaCompleta(casa, tras, orario, campionato, stringaRisultato, avgCornerString, goalHTString)
        
        return stringaCompleta
    else:
        return ''
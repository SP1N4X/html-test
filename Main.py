import requests
from bs4 import BeautifulSoup

a = input()
try:
    integer = int(a)
    print('AVVIO')
except ValueError:
    print('The provided value is not an integer')

n_partite = 10
differenza = 0.3
day = integer

def CalcoloRisultato(m_gol_casa, m_gol_tras, differenza):
    arr_casa = []
    arr_tras = []
    arr_risultati = []

    arr_casa.append(int(m_gol_casa + differenza))  
    arr_casa.append(int(m_gol_casa - differenza))  
    arr_tras.append(int(m_gol_tras + differenza))  
    arr_tras.append(int(m_gol_tras - differenza))  

    for r_c in arr_casa:
        for r_t in arr_tras:
            ris_tot = str(r_c) + '-' + str(r_t)
            arr_risultati.append(ris_tot)
    
    arr_risultati = dict.fromkeys(arr_risultati)
    
    stringaRisultati = ''
    for r in arr_risultati:
        stringaRisultati = stringaRisultati + r + '\n'
    
    casa_min = min(arr_casa)
    tras_min = min(arr_tras)
    
    stringa = '[RISULTATI ESATTI] \n' + stringaRisultati + '[GOAL MINIMI] \n' + 'Casa: ' + str(casa_min) + '\n' + 'Trasferta: ' + str(tras_min)
    return stringa

def Calcolo(g_subiti_casa, g_fatti_casa, g_subiti_tra, g_fatti_tra, diff):
    diff_casa = float(g_fatti_casa) - float(g_subiti_tra)
    diff_tras = float(g_fatti_tra) - float(g_subiti_casa)
    if diff_casa <= diff and diff_casa >= -diff and diff_tras <= diff and diff_tras >= -diff:
        return True
    return False  

def TrovaCampionato(soup):
    try:
        campionato = soup.find("div", {"id": "content"}).find_all('div')[0].find_all('div')[1].find('h1').text
        return campionato
    except:
        return 'Campionato non trovato'

url = "https://www.soccerstats.com/matches.asp?matchday=" + str(day) + "&listing=1"
url_base = "https://www.soccerstats.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
rows = soup.find("table", {"id": "btable"}).find("tbody").find_all("tr")
for row in rows:
    dati = row.find_all("td")
    partite_casa = dati[7].text
    partite_tras = dati[13].text
    if partite_casa != "" and int(partite_casa) >= n_partite and partite_tras != "" and int(partite_tras) >= n_partite:
        g_subiti_casa = dati[3].text
        g_fatti_casa = dati[4].text
        g_subiti_tra = dati[17].text
        g_fatti_tra = dati[16].text
        if g_subiti_casa != "" and g_fatti_casa != "" and g_subiti_tra != "" and g_fatti_tra != "":
            if Calcolo(g_subiti_casa, g_fatti_casa, g_subiti_tra, g_fatti_tra, differenza):
                casa = dati[9].text
                tras = dati[11].text
                orario = dati[10].find("font").text
                link = dati[0].find("a", href=True)['href']
                m_gol_casa = (float(g_fatti_casa) + float(g_subiti_tra))/2
                m_gol_tras = (float(g_fatti_tra) + float(g_subiti_casa))/2
                
                if link != None:
                    try:
                        responseLink = requests.get(url_base + link)
                        soupLink = BeautifulSoup(response.content, 'html.parser')     
                    except:
                        campionato = 'Campionato non trovato'
                        avgCornerString = ''
                        goalHTString = ''    
                    
                    try:
                        campionato = TrovaCampionato(soup)    
                    except:
                        campionato = 'Campionato non trovato'
                    try:
                        avgCornerString = Corner(soup, differenza)
                    except:
                        avgCornerString = ''     
                    try:
                        goalHTString = Corner(soup, differenza)
                    except:
                        goalHTString = ''
                else:
                    campionato = 'Campionato non trovato'
                    avgCornerString = ''
                    goalHTString = ''        
                                          
                stringa = CalcoloRisultato(m_gol_casa, m_gol_tras, differenza)
                print('\n' + casa + ' - ' + tras + '    ' + orario + '\n(' + campionato + ')' + '\n' + str(m_gol_casa) + '/' + str(m_gol_tras) + '\n' + stringa)

print('\nESECUZIONE COMPLETATA')
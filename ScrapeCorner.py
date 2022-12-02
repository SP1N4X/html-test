import requests
from bs4 import BeautifulSoup
url = 'https://www.soccerstats.com/pmatch.asp?league=england3&stats=428-12-3-2023'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
diff = 0.3

def CalcoloAvgCornerCasaTras(riga):
    tds = riga.find_all('td')    
    avgCornerCasa = float(tds[0].find('b').text)
    avgCornerTras = float(tds[-1].find('b').text)
    
    return avgCornerCasa, avgCornerTras
    
def CalcoloTabella(table):
    trs = table.find_all('tr')
    
    rigaCornerFor = trs[1]
    rigaCornerAgainst = trs[2]
    avgCornerForCasa, avgCornerForTras = CalcoloAvgCornerCasaTras(rigaCornerFor) 
    avgCornerAgainstCasa, avgCornerAgainstTras = CalcoloAvgCornerCasaTras(rigaCornerAgainst)   
    
    return avgCornerForCasa, avgCornerForTras, avgCornerAgainstCasa, avgCornerAgainstTras 

def AvgCornerGiusti(avgCornerForCasa, avgCornerForTras, avgCornerAgainstCasa, avgCornerAgainstTras, diff):
    diffCasa = avgCornerForCasa - avgCornerAgainstTras
    diffTras = avgCornerForTras - avgCornerAgainstCasa
    
    if diffCasa <= diff and diffCasa >= -diff and diffTras <= diff and diffTras >= -diff:
        return True
    return False
    
def CalcoloMedie(avgCornerForCasa, avgCornerForTras, avgCornerAgainstCasa, avgCornerAgainstTras, diff):
    diffCasa = avgCornerForCasa - avgCornerAgainstTras
    diffTras = avgCornerForTras - avgCornerAgainstCasa
    
    if diffCasa <= diff and diffCasa >= -diff and diffTras <= diff and diffTras >= -diff:
        avgCasa = (avgCornerForCasa + avgCornerAgainstTras)/2        
        avgTras = (avgCornerForTras + avgCornerAgainstCasa)/2
        
        minCasa = avgCasa - diff
        maxCasa = avgCasa + diff
        minTras = avgTras - diff
        maxTras = avgTras + diff
        
        return minCasa, maxCasa, minTras, maxTras

def ScriviStringa(minCasa, maxCasa, minTras, maxTras):
    stringa = '[AVG CORNER] \nCasaMinCorner' + str(minCasa) + '\nCasaMaxCorner' + str(maxCasa) + '\n \nTrasMinCorner' + str(minTras) + '\nTrasMaxCorner' + str(maxTras) + '\n'
    return stringa
    
def Corner(soup, diff):
    try:
        for table in soup.find_all('table'):
            if table.find('font', text = 'Total Corners = Corners For + Corners Against') != None:
                avgCornerForCasa, avgCornerForTras, avgCornerAgainstCasa, avgCornerAgainstTras = CalcoloTabella(table)
                if AvgCornerGiusti(avgCornerForCasa, avgCornerForTras, avgCornerAgainstCasa, avgCornerAgainstTras, diff):
                    minCasa, maxCasa, minTras, maxTras = CalcoloMedie(avgCornerForCasa, avgCornerForTras, avgCornerAgainstCasa, avgCornerAgainstTras, diff)
                    stringa = ScriviStringa(minCasa, maxCasa, minTras, maxTras)
                    return stringa
        return '' 
    except:
        return                 
print(Corner(soup, diff))
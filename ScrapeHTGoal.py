import requests
from bs4 import BeautifulSoup

def CalcoloRisultato(diff, avgHTFattiCasa, avgHTSubitiCasa, avgHTFattiTras, avgHTSubitiTras):
    avgGoalTempo = (avgHTFattiCasa + avgHTSubitiTras)/2 + (avgHTFattiTras + avgHTSubitiCasa)/2
    minAvgGoalTempo = avgGoalTempo - diff
   
    if minAvgGoalTempo >= 1:
        return True
    return False

def CalcoloGoal(g_fatti_casa, g_subiti_tra, diff):
    diff_casa = g_fatti_casa - g_subiti_tra
    if diff_casa <= diff and diff_casa >= -diff:
        return True
    return False

def ScriviStringa(diff, PGCasa, PGTras, gHTFattiCasa, gHTSubitiCasa, g2HTFattiCasa, g2HTSubitiCasa, gHTFattiTras, gHTSubitiTras, g2HTFattiTras, g2HTSubitiTras):
    avgHTFattiCasa = gHTFattiCasa/PGCasa
    avgHTSubitiTras = gHTSubitiTras/PGTras
    goalCasaHT = CalcoloGoal(avgHTFattiCasa, avgHTSubitiTras, diff)

    avgHTFattiTras = gHTFattiTras/PGTras
    avgHTSubitiCasa = gHTSubitiCasa/PGCasa
    goalTrasHT = CalcoloGoal(avgHTFattiTras, avgHTSubitiCasa, diff)

    avg2HTFattiCasa = g2HTFattiCasa/PGCasa
    avg2HTSubitiTras = g2HTSubitiTras/PGTras
    goalCasa2HT = CalcoloGoal(avg2HTFattiCasa, avg2HTSubitiTras, diff)
    
    avg2HTFattiTras = g2HTFattiTras/PGTras
    avg2HTSubitiCasa = g2HTSubitiCasa/PGCasa
    goalTras2HT = CalcoloGoal(avg2HTFattiTras, avg2HTSubitiCasa, diff)
    
    resultHT = False
    result2HT = False
    
    if goalCasaHT and goalTrasHT:
        resultHT = CalcoloRisultato(diff, avgHTFattiCasa, avgHTSubitiCasa, avgHTFattiTras, avgHTSubitiTras)
    if goalCasa2HT and goalTras2HT:
        result2HT = CalcoloRisultato(diff, avg2HTFattiCasa, avg2HTSubitiCasa, avg2HTFattiTras, avg2HTSubitiTras)
    
    risultato = ''
    if resultHT:
        risultato = risultato + '\n1st. HT Over'
    if result2HT:
        risultato = risultato + '\n2nd. HT Over'
    
    if risultato != '':
        stringa = '[GOAL TEMPI]' + risultato
        return stringa
    return ''

def CalcoloTabCasaTras(tr):
    tds = tr.find_all('td',{'align':'center', 'valign':'top'})
    tdCasa = tds[0]
    tdTras = tds[1]
   
    return tdCasa, tdTras

def CalcoloTabSpecificaCasaTras(tableGeneraleCasa, tableGeneraleTras):
    tableSpecificaCasa = tableGeneraleCasa.find_all('table')[1]
    tableSpecificaTras = tableGeneraleTras.find_all('table')[1]
    
    return tableSpecificaCasa, tableSpecificaTras

def CalcoloGoalFattiSubiti(tableSpecifica):
    trs = tableSpecifica.find_all('tr')

    goalHTFatti = trs[14].find('b').text
    goalHTSubiti = trs[15].find('b').text
    goal2HTFatti = trs[17].find('b').text
    goal2HTSubiti = trs[18].find('b').text

    return int(goalHTFatti), int(goalHTSubiti), int(goal2HTFatti), int(goal2HTSubiti)

def CalcoloTable(table):
    tableGeneraleCasa, tableGeneraleTras = CalcoloTabCasaTras(table.find_all('tr')[1])
    tableSpecificaCasa, tableSpecificaTras = CalcoloTabSpecificaCasaTras(tableGeneraleCasa, tableGeneraleTras) 
    goalHTFattiCasa, goalHTSubitiCasa, goal2HTFattiCasa, goal2HTSubitiCasa = CalcoloGoalFattiSubiti(tableSpecificaCasa)
    goalHTFattiTras, goalHTSubitiTras, goal2HTFattiTras, goal2HTSubitiTras = CalcoloGoalFattiSubiti(tableSpecificaTras)
    
    return goalHTFattiCasa, goalHTSubitiCasa, goal2HTFattiCasa, goal2HTSubitiCasa, goalHTFattiTras, goalHTSubitiTras, goal2HTFattiTras, goal2HTSubitiTras

def HTGoal(soup, PGCasa, PGTras, diff):  
    
    for table in soup.find_all('table'):
        if table.find('font', text = 'GOALS PER TIME SEGMENT') != None:
            gHTFattiCasa, gHTSubitiCasa, g2HTFattiCasa, g2HTSubitiCasa, gHTFattiTras, gHTSubitiTras, g2HTFattiTras, g2HTSubitiTras = CalcoloTable(table)
            stringa = ScriviStringa(diff, PGCasa, PGTras, gHTFattiCasa, gHTSubitiCasa, g2HTFattiCasa, g2HTSubitiCasa, gHTFattiTras, gHTSubitiTras, g2HTFattiTras, g2HTSubitiTras)
            return stringa   
    return ''


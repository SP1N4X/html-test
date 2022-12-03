from bs4 import BeautifulSoup

def Calcolo(g_fatti_casa, g_subiti_tra, diff):
    diff_casa = float(g_fatti_casa) - float(g_subiti_tra)

    if diff_casa <= diff and diff_casa >= -diff:
        g_min = ((float(g_fatti_casa) + float(g_subiti_tra))/2) - diff
        if int(g_min) > 0:
            return str(int(g_min))
        return '-'
    return '-'

def ScriviStringa(diff, PGCasa, PGTras, gHTFattiCasa, gHTSubitiCasa, g2HTFattiCasa, g2HTSubitiCasa, gHTFattiTras, gHTSubitiTras, g2HTFattiTras, g2HTSubitiTras):
    avgHTFattiCasa = gHTFattiCasa/PGCasa
    avgHTSubitiTras = gHTSubitiTras/PGTras
    goalCasaHT = Calcolo(avgHTFattiCasa, avgHTSubitiTras, diff)

    avgHTFattiTras = gHTFattiTras/PGTras
    avgHTSubitiCasa = gHTSubitiCasa/PGCasa
    goalTrasHT = Calcolo(avgHTFattiTras, avgHTSubitiCasa, diff)

    avg2HTFattiCasa = g2HTFattiCasa/PGCasa
    avg2HTSubitiTras = g2HTSubitiTras/PGTras
    goalCasa2HT = Calcolo(avg2HTFattiCasa, avg2HTSubitiTras, diff)
    
    avg2HTFattiTras = g2HTFattiTras/PGTras
    avg2HTSubitiCasa = g2HTSubitiCasa/PGCasa
    goalTras2HT = Calcolo(avg2HTFattiTras, avg2HTSubitiCasa, diff)

    if goalCasaHT != '-' or goalTrasHT != '-' or goalCasa2HT != '-' or goalTras2HT != '-':
        stringa = '[GOAL TEMPI] \n1st. HT \nCasa: ' + goalCasaHT + '\nTras: ' + goalTrasHT + '\n \n2nd. HT \nCasa: ' + goalCasa2HT + '\nTras: ' + goalTras2HT + '\n'
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

    return goalHTFatti, goalHTSubiti, goal2HTFatti, goal2HTSubiti

def CalcoloTable(table):
    tableGeneraleCasa, tableGeneraleTras = CalcoloTabCasaTras(table.find_all('tr')[1])
    tableSpecificaCasa, tableSpecificaTras = CalcoloTabSpecificaCasaTras(tableGeneraleCasa, tableGeneraleTras) 
    goalHTFattiCasa, goalHTSubitiCasa, goal2HTFattiCasa, goal2HTSubitiCasa = CalcoloGoalFattiSubiti(tableSpecificaCasa)
    goalHTFattiTras, goalHTSubitiTras, goal2HTFattiTras, goal2HTSubitiTras = CalcoloGoalFattiSubiti(tableSpecificaTras)
    
    return goalHTFattiCasa, goalHTSubitiCasa, goal2HTFattiCasa, goal2HTSubitiCasa, goalHTFattiTras, goalHTSubitiTras, goal2HTFattiTras, goal2HTSubitiTras

def HTGoal(soup, PGCasa, PGTras, diff):  
    try:
        for i, table in enumerate(soup.find_all('table')):
            if table.find('font', text = 'GOALS PER TIME SEGMENT') != None:
                gHTFattiCasa, gHTSubitiCasa, g2HTFattiCasa, g2HTSubitiCasa, gHTFattiTras, gHTSubitiTras, g2HTFattiTras, g2HTSubitiTras = CalcoloTable(table)
                stringa = ScriviStringa(diff, PGCasa, PGTras, gHTFattiCasa, gHTSubitiCasa, g2HTFattiCasa, g2HTSubitiCasa, gHTFattiTras, gHTSubitiTras, g2HTFattiTras, g2HTSubitiTras)
                return stringa   
        return '' 
    except:
        return ''

html = 'html'

def CalcoloTabCasaTras(tr):
    tds = tr.find_all('td')
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

def CalcoloGoalFromHtml(html):
    for table in html.find_all('table'):
        if table.find('font', text = 'GOAL PER TIMES SEGMENT') != null:
            gHTFattiCasa, gHTSubitiCasa, g2HTFattiCasa, g2HTSubitiCasa, gHTFattiTras, gHTSubitiTras, g2HTFattiTras, g2HTSubitiTras = CalcoloTable(table)
            
            print(gHTFattiCasa, gHTSubitiCasa, g2HTFattiCasa, g2HTSubitiCasa, gHTFattiTras, gHTSubitiTras, g2HTFattiTras, g2HTSubitiTras)
            break

CalcoloGoalFromHtml(html)
import requests
from bs4 import BeautifulSoup

def Calcolo_HT_Avg_goal_home(PG_casa, Scoring_Rate_HT_home, Goals_scored_home):
    Goals_scored_home = Scoring_Rate_HT_home/100*Goals_scored_home
    HT_Avg_goal_home = Goals_scored_home/PG_casa

    return HT_Avg_goal_home

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

def CalcoloGoalFromHtml(href):
    url_base = "https://www.soccerstats.com/"
    
    try:
        response = requests.get(url_base + href)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        for i, table in enumerate(soup.find_all('table')):
            if table.find('font', text = 'GOALS PER TIME SEGMENT') != None:
                gHTFattiCasa, gHTSubitiCasa, g2HTFattiCasa, g2HTSubitiCasa, gHTFattiTras, gHTSubitiTras, g2HTFattiTras, g2HTSubitiTras = CalcoloTable(table)
                    
        print(int(gHTFattiCasa), int(gHTSubitiCasa), int(g2HTFattiCasa), int(g2HTSubitiCasa), int(gHTFattiTras), int(gHTSubitiTras), int(g2HTFattiTras), int(g2HTSubitiTras))
    except:
        print('Errore nelle calcolo goal')
                   
href = 'pmatch.asp?league=england4&stats=328-14-20-2023-crewe-alexandra-newport'
CalcoloGoalFromHtml(href)
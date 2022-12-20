json =  {}
oggetto = {}
def intTry(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def downloadMatch(casa, tras):
    print(casa, tras)

def CheckMatch(line):
    split = line.split('-')
    casa = split[0]
    tras = split[1]
    if intTry(casa) or intTry(tras):
        return 
    oggetto['casa'] = casa
    oggetto['trasferta'] = tras

def CheckCampionato(line):
    line.replace('(', '')
    line.replace(')', '')
    oggetto['campionato'] = line

def PrevisioneTipo(line):
    line.replace(']', '')
    line.replace('[', '')
    return line

def CheckEsatti(line):
    oggetto['risultato'] = line

def CheckCorner(line):
    split = line.split(' ')
    oggetto['Corner'] = split[1]

def CheckMin(line):
    split = line.split(':')
    if split[0] == 'Casa':
        oggetto['MinimiCasa'] = split[1].replace(' ', '')
    if split[0] == 'Trasferta':
        oggetto['MinimiTrasferta'] = split[1].replace(' ','')

def CheckPrevisione(tipo, line):
    if tipo == 'RISULTATI ESATTI':
        CheckEsatti(line)
        return
    
    if tipo == 'GOAL MINIMI':
        CheckMin(line)
        return
    
    if tipo == 'AVG CORNER':
        CheckCorner(line)
        return

def UpdateJson():
    if oggetto != {}:
        jsonOggetto =   {
                        'casa':oggetto['casa'],
                        'trasferta':oggetto['trasferta'],
                        'Previsione':{},
                        'Risultati':{}
                        }
        if 'MinimiCasa' in oggetto:
            jsonOggetto['Previsione']['minCasa'] = oggetto['MinimiCasa']
        if 'MinimiTrasferta' in oggetto:
            jsonOggetto['Previsione']['minTras'] = oggetto['MinimiTrasferta']
        if 'Corner' in oggetto:
            jsonOggetto['Previsione']['corner'] = oggetto['Corner']

        json[today][oggetto['campionato']].append(jsonOggetto)
    oggetto = {}



today = '21-12-2022'
with open(f'{today}.txt', 'r') as f:
    lines = f.readlines()
    json[today] = ''
    i = 0
    start = True
    previsione = ''
    for line in lines:
        if line == '\n':
            UpdateJson()
            start == True
            continue
        if start == True:
            CheckMatch(line)
            start = False
            continue
        if start == False:
            if 'Orario:' in line:
                continue
            if '(' in line and ')' in line:
                CheckCampionato(line)
                continue
            if '[' in line and ']' in line:
                previsione = PrevisioneTipo(line)
                continue
            CheckPrevisione(previsione, line)

print(json)
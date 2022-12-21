import requests
         
json =  {}
oggetto = {}
def intTry(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def UploadJson(json):
    result = requests.patch('https://testwebsocket-672a2-default-rtdb.europe-west1.firebasedatabase.app/Soccer/.json', json=json)
    print(result.content)

def CheckMatch(line):
    global oggetto
    oggetto['partita'] = line

def CheckCampionato(line):
    line = line.replace('(', '')
    line = line.replace(')', '')
    oggetto['campionato'] = line

def PrevisioneTipo(line):
    line = line.replace(']', '')
    line = line.replace('[', '')
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
    print(tipo.encode())
    if tipo == 'RISULTATI ESATTI  ':
        CheckEsatti(line)
        print(line)
        return
    
    if tipo == 'GOAL MINIMI  ':
        CheckMin(line)
        return
    
    if tipo == 'AVG CORNER  ':
        CheckCorner(line)
        return

def UpdateJson():
    global oggetto
    global json
    if oggetto != {}:
        jsonOggetto =   {oggetto['partita']:
                            {
                                'Previsione':{},
                                'Risultati':{}
                            }
                        }
        if 'MinimiCasa' in oggetto:
            if 'Previsione' in jsonOggetto[oggetto['partita']]:
                jsonOggetto[oggetto['partita']]['Previsione']['minCasa'] = oggetto['MinimiCasa']
            else:
                jsonOggetto[oggetto['partita']]['Previsione'] = {'minCasa': oggetto['MinimiCasa']}
        if 'MinimiTrasferta' in oggetto:
            if 'Previsione' in jsonOggetto[oggetto['partita']]:
                jsonOggetto[oggetto['partita']]['Previsione']['minTras'] = oggetto['MinimiTrasferta']
            else:
                jsonOggetto[oggetto['partita']]['Previsione'] = {'minTras': oggetto['MinimiTrasferta']}
        if 'Corner' in oggetto:
            if 'Previsione' in jsonOggetto[oggetto['partita']]:
                jsonOggetto[oggetto['partita']]['Previsione']['corner'] = oggetto['Corner']
            else:
                jsonOggetto[oggetto['partita']]['Previsione'] = {'corner': oggetto['Corner']}

        if today in json:
            if oggetto['campionato'] in json[today]:
                json[today][oggetto['campionato']].update(jsonOggetto)
            else:
                json[today].update({oggetto['campionato']: jsonOggetto})
        else:
            json[today] = {oggetto['campionato']: jsonOggetto}
        
    oggetto = {}

def CheckFile(fileName):
    with open(f'{fileName}.txt', 'r') as f:
        lines = f.readlines()
        json[today] = {}
        start = True
        previsione = ''

        for line in lines:
            line = line.replace('\n', ' ')
            if line == ' ':
                UpdateJson()
                start = True
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

    UploadJson(json)



today = '21-12-2022'
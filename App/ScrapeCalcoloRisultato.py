def CalcoloRisultato(g_subiti_casa, g_fatti_casa, g_subiti_tra, g_fatti_tra, diff):
    if Calcolo(g_subiti_casa, g_fatti_casa, g_subiti_tra, g_fatti_tra, diff):
        m_gol_casa = (float(g_fatti_casa) + float(g_subiti_tra))/2
        m_gol_tras = (float(g_fatti_tra) + float(g_subiti_casa))/2
        
        arr_casa = []
        arr_tras = []
        arr_risultati = []

        arr_casa.append(int(m_gol_casa + diff))  
        arr_casa.append(int(m_gol_casa - diff))  
        arr_tras.append(int(m_gol_tras + diff))  
        arr_tras.append(int(m_gol_tras - diff))  

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
        
        stringa = '[RISULTATI ESATTI] \n' + stringaRisultati + '[GOAL MINIMI] \n' + 'Casa: ' + str(casa_min) + '\n' + 'Trasferta: ' + str(tras_min) + '\n'
        return stringa
    else:
        return ''

def Calcolo(g_subiti_casa, g_fatti_casa, g_subiti_tra, g_fatti_tra, diff):
    diff_casa = float(g_fatti_casa) - float(g_subiti_tra)
    diff_tras = float(g_fatti_tra) - float(g_subiti_casa)
    if diff_casa <= diff and diff_casa >= -diff and diff_tras <= diff and diff_tras >= -diff:
        return True
    return False
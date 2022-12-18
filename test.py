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
    downloadMatch(casa, tras)

today = '18-12-2022'
with open(f'{today}.txt', 'r') as f:
    lines = f.readlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        CheckMatch(line)
        i += 1

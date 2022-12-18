today = '18-12-2022'
with open(f'{today}.txt', 'r') as f:
    lines = f.readlines()
    i = 0
    while i < len(lines):
        print(lines[i])
        i += 1

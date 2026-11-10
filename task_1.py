times = '1h 45m,360s,25m,30m 120s,2h 60s'
minutes = 0

for t in times.split(','):
    for i in t.split(' '):
        if 'h' in i:
            h = int(i.replace('h', ''))
            minutes += int(h * 60)
        elif 'm' in i:
            m = int(i.replace('m', ''))
            minutes += int(m)
        elif 's' in i:
            s = int(i.replace('s', ''))
            minutes += int(s / 60)
            
print(minutes)
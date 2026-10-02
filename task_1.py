times='1h 45m,360s,25m,30m 120s,2h 60s'
sum_minutes=0
for value in times.split(','):        
    for part in value.split():
        if 'h' in part:
            sum_minutes += int(part.replace('h', '')) * 60
        elif 'm' in part:
            sum_minutes += int(part.replace('m', ''))
        elif 's' in part:
            sum_minutes += int(part.replace('s', '')) // 60
print(sum_minutes)
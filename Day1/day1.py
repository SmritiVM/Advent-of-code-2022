max_calorie = 0
with open('sampleinput_day1.txt') as file:
    calorie_count = 0
    for line in file:
        if line == '\n':
            max_calorie = max(max_calorie, calorie_count)
            calorie_count = 0
        
        else:
            calorie_count += int(line.split()[0])

print(max_calorie)
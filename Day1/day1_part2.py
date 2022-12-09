import heapq
calorie = []
heapq.heapify(calorie)

with open('Day1\day1_prob1.txt') as file:
    calorie_count = 0
    for line in file:
        if line == '\n':
            heapq.heappush(calorie, calorie_count)
            calorie_count = 0
        
        else:
            calorie_count += int(line.split()[0])

    heapq.heappush(calorie, calorie_count)
    
print(sum(heapq.nlargest(3, calorie)))


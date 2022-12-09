match = {'A' : ['B', 'C'], 'B' : ['C', 'A'], 'C' : ['A', 'B']} #If a is played, what to play to (win, lose)
points = {'A' : 1, 'B' : 2, 'C' : 3}

with open('Day2\day2.txt') as file:
    score = 0
    for line in file:
        opponent, status = line.split()
        if status == 'X':
            score += points[match[opponent][1]] #to lose
        
        elif status == 'Y':
            score += points[opponent] + 3
        
        else:
            score += points[match[opponent][0]] + 6 #to win
        
        print(opponent, status, score)

print(score)



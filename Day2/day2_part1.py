match = {'A' : 'Y', 'B' : 'Z', 'C' : 'X' }
points = {'X' : 1, 'Y' : 2, 'Z' : 3}

with open('Day2\day2.txt') as file:
    score = 0
    for line in file:
        opponent, played = line.split()
        score += points[played]
        if ord(played) - ord(opponent) == 23:
            score += 3
        elif match[opponent] == played:
            score += 6

print(score)

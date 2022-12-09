def viewing_distance_up(grid, i, j): #vertical
    distance = 0
    tree = grid[i][j]
    for _ in range(i - 1, -1, -1):
        if grid[_][j] < tree:
            distance += 1
        else:
            distance += 1
            break
    return distance

def viewing_distance_down(grid, i, j, m): #vertical
    distance = 0
    tree = grid[i][j]
    for _ in range(i + 1,  m):
        if grid[_][j] < tree:
            distance += 1
        else:
            distance += 1
            break
    return distance

def viewing_distance_left(grid, i, j): #horizontal
    distance = 0
    tree = grid[i][j]
    for _ in range(j - 1, -1, -1):
        if grid[i][_] < tree:
            distance += 1
        else:
            distance += 1
            break
    return distance

def viewing_distance_right(grid, i, j, n): #horizontal
    distance = 0
    tree = grid[i][j]
    for _ in range(j + 1, n):
        if grid[i][_] < tree:
            distance += 1
        else:
            distance += 1
            break
    return distance
    
def scenic_score(grid, i, j, m, n):
    #print( viewing_distance_up(grid, i, j) , viewing_distance_down(grid, i, j, m) , viewing_distance_left(grid, i, j) , viewing_distance_right(grid, i, j, n))
    score = viewing_distance_up(grid, i, j) * viewing_distance_down(grid, i, j, m) * viewing_distance_left(grid, i, j) * viewing_distance_right(grid, i, j, n)
    return score

def largest_scenic_score(grid, m, n):
    max_scenic_score = 0
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            score = scenic_score(grid, i, j, m, n)
            max_scenic_score = max(max_scenic_score, score)
    
    return max_scenic_score


def main():
    with open('Day8\day8.txt') as file:
        grid = []
        m = 0
        for line in file:
            row = [int(digit) for digit in line.rstrip('\n')]
            grid.append(row)
            m += 1

        n = len(grid[0])

        
        print(largest_scenic_score(grid, m, n))

main()
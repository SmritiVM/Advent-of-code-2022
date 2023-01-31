def is_higher(char1, char2):
    return ord(char1) - ord(char2) <= 1 #do not take abs

def is_valid_index(i, j, rows, columns):
    return 0 <= i < rows and 0 <= j < columns

def distance(grid, i, j):
    queue = [[i, j, 0]]
    visited = set([(i, j)])
    rows, columns = len(grid), len(grid[0])

    while queue:
        i, j, d= queue.pop(0)
        if grid[i][j] == 'E':
            return d
        for neighbour_i, neighbour_j in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
            if is_valid_index(neighbour_i, neighbour_j, rows, columns):
                if grid[neighbour_i][neighbour_j] == 'E' and is_higher('z', grid[i][j]):
                    queue.append([neighbour_i, neighbour_j, d + 1])
                elif grid[neighbour_i][neighbour_j] != 'E' and (neighbour_i, neighbour_j) not in visited and is_higher(grid[neighbour_i][neighbour_j], grid[i][j]):
                    queue.append([neighbour_i, neighbour_j, d + 1])
                    visited.add((neighbour_i,neighbour_j))
            

            

def matrix(file):
    grid = []
    for line in file:
        grid.append(list(line.rstrip()))
    return grid

def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                grid[i][j] = 'a' #replacing the S with a
                return (i, j)
    return (-1, -1)

def main():
    with open('Day12\day12.txt') as file:
        grid = matrix(file)
        #print(grid)
        i, j = find_start(grid)
        print(distance(grid, i, j))

main()


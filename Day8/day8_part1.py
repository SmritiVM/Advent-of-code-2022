def is_visible(grid, i, j, m, n):
    tree = grid[i][j]
    if tree > max([grid[_][j] for _ in range(i)]) or tree > max([grid[_][j] for _ in range(i + 1, m)]) or tree > max(grid[i][:j]) or tree > max(grid[i][j + 1:]):
        return True
    return False

def no_of_trees_visible(grid, m, n):
    visible = 2 * m + 2 * (n - 2) #adding all edges
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if is_visible(grid, i, j, m, n):
                visible += 1
    return visible


def main():
    with open('Day8\day8.txt') as file:
        grid = []
        m = 0
        #row_wise_max = []
        for line in file:
            row = [int(digit) for digit in line.rstrip('\n')]
            grid.append(row)
            #row_wise_max.append(max(row))
            m += 1

        n = len(grid[0])

        
        print(no_of_trees_visible(grid, m, n))

main()
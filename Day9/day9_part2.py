def move_head(direction, head):
    if direction == 'R':
        head[1] += 1
    elif direction == 'L':
        head[1] -= 1
    elif direction == 'U':
        head[0] += 1
    elif direction == 'D':
        head[0] -= 1

def adjacent(head, tail):
    if abs(head[1] - tail[1]) == 1 and head[0] == tail[0]: #checking horizontal
        return True
    elif abs(head[0] - tail[0]) == 1 and head[1] == tail[1]: #checking vertical
        return True
    elif head == tail: #overlapping
        return True
    elif abs(head[1] - tail[1]) == 1 and abs(head[0] - tail[0]) == 1: #disgonal
        return True
    return False

def add_to_visited(visited, tail):
    if tuple(tail) not in visited:
        visited.append(tuple(tail))

def move_tail(head, tail):
    if abs(head[1] - tail[1]) == 2 and head[0] == tail[0]: #left, right
        if head[1] > tail[1]:
            tail[1] += 1
        else:
            tail[1] -= 1
        

    elif abs(head[0] - tail[0]) == 2 and head[1] == tail[1]: #up, down
        if head[0] > tail[0]:
            tail[0] += 1
        else:
            tail[0] -= 1
        

    elif abs(head[1] - tail[1]) == 2 or abs(head[0] - tail[0]) == 2: #left, right diagonal
        if head[1] > tail[1]: #head is to right
            tail[1] += 1
        else:
            tail[1] -= 1
        
        
        if head[0] > tail[0]:
            tail[0] += 1
        else:
            tail[0] -= 1
    
    
    
def move_part(prev, current):
    if not adjacent(prev, current):
        move_tail(prev, current)

def find_unique_visits(moves):
    head = [0, 0]
    tail = [0, 0]
    part = [[0, 0] for _ in range(8)]
    visited = [(0, 0)]
    s = [0, 0]
    for move in moves:
        direction, steps = move.split()
        for i in range(int(steps)):
            move_head(direction, head)
            move_part(head, part[0])
            for j in range(1, 8):
                move_part(part[j - 1], part[j])
            move_part(part[7], tail)
            add_to_visited(visited, tail)
            
                
        #print(head, tail)
    return len(visited)


def main():
    with open('Day9\day9.txt') as file:
        print(find_unique_visits(file))

main()
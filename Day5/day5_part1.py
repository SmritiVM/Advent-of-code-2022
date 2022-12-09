

with open('Day5\day5.txt') as file:
    
    stack = {}
    for line in file:
        if line[1] == '1':
            break
        line.rstrip('\n')

        stack_number = 1
        for i in range(1, len(line), 4):
            element = line[i : i + 1]
            if not element.isspace():
                if stack_number in stack:
                    stack[stack_number].append(element)
                else:
                    stack[stack_number] = [element]
            stack_number += 1
        
    file.readline()
    for line in file:
        instruction = line.split()
        source, dest = int(instruction[3]), int(instruction[5])
        for n in range(int(instruction[1])):
            stack[dest].insert(0, stack[source].pop(0))
        

for key in sorted(stack.keys()):
    print(stack[key][0], end = '')

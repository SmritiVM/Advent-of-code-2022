def compare(element1, element2):
    if isinstance(element1, int) and isinstance(element2, int):
        if element1 < element2:
            return -1
        elif element1 > element2:
            return 1
        else:
            return 0
    
    elif isinstance(element1, list) and isinstance(element2, list):
        i = 0
        length1, length2 = len(element1), len(element2)
        while i < length1 and i < length2:
            is_greater =  compare(element1[i], element2[i])
            if is_greater == -1:
                return -1
            
            elif is_greater == 1:
                return 1
            i += 1
        
        if i == length1 and i < length2:
            return -1
        
        elif i == length2 and i < length1:
            return 1

        return 0

    
    elif isinstance(element1, int) and isinstance(element2, list):
        return compare([element1], element2)

    else:
        return compare(element1, [element2])

def check_pair(left, right):
    return compare(left, right)
    
def index_sum_of_ordered_pairs(file):
    index_sum = 0
    index = 1
    for line in file:
        left = eval(line.rstrip('\n'))
        right = eval(file.readline().rstrip('\n'))
        if check_pair(left, right) == -1:
            index_sum += index
        
        index += 1
        file.readline()
    return index_sum


with open('Day13\day13.txt') as file:
    print(index_sum_of_ordered_pairs(file))
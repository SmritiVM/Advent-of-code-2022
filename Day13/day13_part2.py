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


def sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - 1):
            if compare(array[j + 1], array[j]) == -1:
                array[j], array[j + 1] = array[j + 1], array[j]
    
def order_packets(file):
    array = []
    for line in file:
        left = eval(line.rstrip('\n'))
        right = eval(file.readline().rstrip('\n'))
        array.extend([left, right])
        file.readline()
    array.extend([[[2]], [[6]]])
    sort(array)
    return array

def find_decoder_key(file):
    array = order_packets(file)
    return (array.index([[2]]) + 1) * (array.index([[6]]) + 1)




with open('Day13\day13.txt') as file:
    print(find_decoder_key(file))
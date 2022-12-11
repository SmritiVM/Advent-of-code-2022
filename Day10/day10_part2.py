def add_to_image(crt_image, x, crt_pointer):
    if crt_pointer in [x - 1, x , x + 1]:
        crt_image += '#'
    else:
        crt_image += '.'
    if crt_pointer == 39:
        crt_image += '\n'
    return crt_image

def create_image(file):
    x = 1
    crt_pointer = 0
    crt_image = '#'
    for line in file:
        if line.startswith('noop'):
            crt_pointer = (crt_pointer + 1)%40
            crt_image = add_to_image(crt_image, x, crt_pointer)

        elif line.startswith('addx'):
            addend = int(line.split()[1])
            
            crt_pointer = (crt_pointer + 1)%40
            crt_image = add_to_image(crt_image, x, crt_pointer)
        

            x += addend
            crt_pointer = (crt_pointer + 1)%40
            crt_image = add_to_image(crt_image, x, crt_pointer)
            
    return crt_image

def main():
    with open('Day10\day10.txt') as file:
        print(create_image(file))

main()
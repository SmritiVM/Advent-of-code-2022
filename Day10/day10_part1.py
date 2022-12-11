def check_signal_strength(cycle, x):
    if cycle in [20, 60, 100, 140, 180, 220]:
        return cycle * x
    return 0

def total_signal_strength(file):
    x = 1
    cycle = 1
    total_signal_strength = 0
    for line in file:
        if line.startswith('noop'):
            cycle += 1
            total_signal_strength += check_signal_strength(cycle, x)
        elif line.startswith('addx'):
            addend = int(line.split()[1])
            
            cycle += 1
            total_signal_strength += check_signal_strength(cycle, x)
            x += addend
            cycle += 1
            total_signal_strength += check_signal_strength(cycle, x)
            
    return total_signal_strength

def main():
    with open('Day10\day10.txt') as file:
        print(total_signal_strength(file))

main()
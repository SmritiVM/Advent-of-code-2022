import math
def generate_monkeys(file):
    monkeys = {}
    for line in file:
        if line.startswith('Monkey'):
            key = int(line.split()[1][0])
            starting_items = [int(x) for x in file.readline().rstrip()[18:].split(', ')]
            operation = file.readline().rstrip()[19: ]
            test = int(file.readline().rstrip().split()[-1])
            true = int(file.readline().rstrip().split()[-1])
            false = int(file.readline().rstrip().split()[-1])
            monkeys[key] = {'Starting Items' :starting_items,'Operation': operation, 'Test':[test, true, false], 'Items Inspected' : 0}
    #print(monkeys)
    return monkeys

def evaluate_new(old, expression):
    terms = expression.split()
    for i in range(len(terms)):
        if terms[i] == 'old':
            terms[i] = old
    return eval(''.join(terms))

def lcm(numbers: list):
    lcm = numbers[0]
    for i in range(1, len(numbers)):
        lcm = lcm * numbers[i] // math.gcd(lcm, numbers[i])
    return lcm

def find_test_lcm(monkeys):
    tests = [monkeys[monkey]['Test'][0] for monkey in monkeys]
    return lcm(tests)
    
def single_round(monkeys):
    lcm = find_test_lcm(monkeys)
    for monkey in monkeys:
        for item in monkeys[monkey]['Starting Items']:
            monkeys[monkey]['Items Inspected'] += 1
            old = str(item)
            expression = monkeys[monkey]['Operation']
            new = evaluate_new(old, expression)
            new %= lcm
            test, true, false = monkeys[monkey]['Test']
            if new % test == 0:
                monkeys[true]['Starting Items'].append(new)
            else:
                monkeys[false]['Starting Items'].append(new)
        monkeys[monkey]['Starting Items'].clear()


def pass_items(monkeys):
    for i in range(10000):
        single_round(monkeys)
    #print(monkeys)

def calculate_monkey_business(monkeys):
    items_inspected = [monkeys[monkey]['Items Inspected'] for monkey in monkeys]
    items_inspected.sort(reverse = True)
    monkey_business = items_inspected[0] * items_inspected[1]
    return monkey_business


def main():
    with open('Day11\day11.txt') as file:
        monkeys = generate_monkeys(file)
        pass_items(monkeys)
        print(calculate_monkey_business(monkeys))

main()
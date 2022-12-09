#Overlap: ul1 <= ll2 or ul2 <= ll1

nonoverlapping = 0
count = 0
with open('Day4\day4.txt') as file:
    for line in file:
        count += 1
        elf1, elf2 = line.split(',')
        ll1, ul1 = elf1.split('-')
        ll2, ul2 = elf2.split('-')
        if int(ul1) < int(ll2) or int(ll1) > int(ul2):
            nonoverlapping += 1

print(count - nonoverlapping)

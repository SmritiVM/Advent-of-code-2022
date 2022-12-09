#Uppercase: priority = ascii - 38
#Lowercase: priority = ascii - 96

priority = 0
with open('Day3\day3.txt') as file:
    lines = file.readlines()
    n = len(lines)
    for i in range(0, n, 3):
        elf1, elf2, elf3 = set(lines[i]), set(lines[i + 1]), set(lines[i + 2])
        s = elf1 & elf2 & elf3
        for item in s:
            if 'A' <= item <= 'Z':
                priority += ord(item) - 38
            elif 'a' <= item <= 'z':
                priority += ord(item) - 96

print(priority)
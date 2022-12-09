#Uppercase: priority = ascii - 38
#Lowercase: priority = ascii - 96

priority = 0
with open('Day3\day3.txt') as file:
    for line in file:
        n = len(line)
        compartment1, compartment2 = set(line[:n//2]), set(line[n//2:])
        s = compartment1.intersection(compartment2)
        for item in s:
            if 'A' <= item <= 'Z':
                priority += ord(item) - 38
            else:
                priority += ord(item) - 96

print(priority)
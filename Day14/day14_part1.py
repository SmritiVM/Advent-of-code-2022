def plot_rocks(file):
    paths = file.read().split('\n')
    print(paths)

with open('Day14\sampleinput14.txt') as file:
    plot_rocks(file)
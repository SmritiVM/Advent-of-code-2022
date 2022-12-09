
def find_marker(message, marker_start, marker_end):
    if marker_end > len(message):
        return

    sequence = set(message[marker_start : marker_end])
    
    while len(sequence) != 14:
        marker_start += 1
        marker_end += 1
        sequence = set(message[marker_start : marker_end])
    return marker_end
    

            
def main():
    with open('Day6\day6.txt') as file:
        message = file.read()
        marker_start = 0
        marker_end = marker_start + 14
        print(find_marker(message, marker_start, marker_end))

main()
line = input("Input something: ")
length = len(line)
length_middle = int(len(line)/2)
line_start = ''
line_end = ''
if length % 2 == 0:
    line_start = line[0:length_middle]
    line_end = line[length_middle::]
elif length % 2 != 0:
    line_start = line[0:length_middle + 1]
    line_end = line[length_middle+1::]
print('New line is: ', line_end+line_start)


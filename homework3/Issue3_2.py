line = input("Input something: ")
length = len(line)
length_middle = int(len(line)/2)
if length % 2 == 0:
    line_start = line[0:length_middle]
    line_end = line[length_middle::]
elif length % 2 != 0:
    line_start = line[0:length_middle + 1]
    line_end = line[length_middle+1::]
print('New line is: ', line_end+line_start)

#Solution2
line = input("Input something: ")
l = len(line)//2 + len(line)%2
line_start = line[l-1:]
line_end = line[:l-1]
print(' Solution2 line is: ', line_start+' '+line_end)


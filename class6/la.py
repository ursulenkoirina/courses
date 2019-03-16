def generates_song(number_rows = 3 , number_la = 1, i = 0):
    text = 'la-'
    song = ((text*number_la).rstrip('-') + '\n') * number_rows
    if i == 0:
        last_sym = '.'
    elif i == 1:
        last_sym = '!'
    song = song.rstrip() + last_sym
    return song

if __name__ == "__main__":
    a = generates_song(5, 10, 1)
    print(a)

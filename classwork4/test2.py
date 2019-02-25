"""
Test doc
"""
def enter_word():
    while True:
        a = input('Enter word: ')
        if a.isalpha():
            return a

# print('Test2__name__: ', __name__)
if __name__ == "__main__":
    x = enter_word()
    print(x)


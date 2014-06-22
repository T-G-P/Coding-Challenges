letters = {}
def parse_text():
    with open('fogcreek', 'r') as f:
        for line in f:
            char_list= list(line) 
            for char in char_list: 
                if not char in letters:
                    letters[char]=1
                else:
                    letters[char]+=1
def print_word():
    for char in sorted(letters, key=letters.get, reverse=True):
        if(char != '_'):
            print(char, letters[char])
        else:
            break
parse_text()
print_word()



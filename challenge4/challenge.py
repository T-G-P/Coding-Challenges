'''
Sort the characters in the following string:

abcdefghijklmnopqrstuvwxyz_

by the number of times the character appears in the following text (descending):
For this challenge, I am storing the string in a text file rather than a variable.
See the attached text file for the string used here. 

'''
letters = {}
word=[]

def parse_text():
    with open('textfile', 'r') as f:
        for line in f:
            char_list= list(line.strip('\n')) 
            for char in char_list: 
                if not char in letters:
                    letters[char]=1
                else:
                    letters[char]+=1

def print_word():
    print "Here are the sorted letters:\n"
    for char in sorted(letters, key=letters.get, reverse=True):
        if(char != '_'):
            print(char, letters[char])
            word.append(char)
        else:
           result = ''.join(word)
           continue 

    print "\nThe secret word is: \n"+result

parse_text()
print_word()

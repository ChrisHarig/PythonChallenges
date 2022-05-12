'''
#1
5/11/2022  
"Assign every lowercase letter a value, from 1 for a to 26 for z. Given a string of lowercase letters, find the sum of the values of the letters in the string.  
lettersum("") => 0  
lettersum("a") => 1  
lettersum("z") => 26  
lettersum("cab") => 6  
lettersum("excellent") => 100  
lettersum("microspectrophotometries") => 317"
https://www.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/
'''

# My initial solution was to create a dictionary with every letter assigned to it's 
# respective value, and loop each letter in the phrase while keeping a running sum.

letterDictionary = { #dictionary assigning each letter a value so the word can be summed
    "a": 1, "b": 2, "c": 3, "d": 4,"e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, 
    "o": 15, "p": 16, "q": 17,"r": 18, "s": 19, "t": 20,"u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26,
}

def letterSum(phrase): #letterSum function that can take in any string and return the sum of it's characters
    total = 0 
    for letter in phrase: 
        total += letterDictionary[letter]
    return total 

print(letterSum("cab")) #prints out the output to check if the function works

# My second solution involves using the ASCII Table of characters and a function that converts a character to it's numerical value. 
# The table allows me to use the characters assigned values directly and not have to create my own dictionary.

def letterSum2(phrase): #letterSum function that can take in any string and return the sum of it's characters
    total = 0;
    for letter in phrase:
        total += (ord(letter) - 96) #ord function converts to ASCII value 
    return total

print(letterSum2("cab")) #prints out the output to check if the function works

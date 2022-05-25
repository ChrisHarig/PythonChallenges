'''
For the purpose of this challenge, Morse code represents every letter as a sequence of 1-4 characters, each of which is either 
. (dot) or - (dash). The code for the letter a is .-, for b is -..., etc. The codes for each letter a through z are
.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..
Normally, you would indicate where one letter ends and the next begins, for instance with a space between the letters' codes, 
but for this challenge, just smoosh all the coded letters together into a single string consisting of only dashes and dots.

Examples
smorse("sos") => "...---..."
smorse("daily") => "-...-...-..-.--"
smorse("programmer") => ".--..-.-----..-..-----..-."
smorse("bits") => "-.....-..."
smorse("three") => "-.....-..."
An obvious problem with this system is that decoding is ambiguous. For instance, both bits and three encode to the same string, 
so you can't tell which one you would decode to without more information.
https://www.reddit.com/r/dailyprogrammer/comments/cmd1hb/20190805_challenge_380_easy_smooshed_morse_code_1/
'''

#I created a dictionary and converted a given sting input in to a list of characters. I then converted each character in to it's morse version, and 
#created a new string out of that list.

morse = {
    "a" : ".-" ,
    "b" : "-..." ,
    "c" : "-.-." ,
    "d" : "-.." ,
    "e" : "." ,
    "f" : "..-." ,
    "g" : "--." ,
    "h" : "...." ,
    "i" : ".." ,
    "j" : ".---",
    "k" : "-.-" ,
    "l" : ".-.." ,
    "m" : "--" ,
    "n" : "-." ,
    "o" : "---" ,
    "p" : ".--." ,
    "q" : "--.-" ,
    "r" : ".-." ,
    "s" : "..." ,
    "t" : "-",
    "u" : "..-" ,
    "v" : "...-" ,
    "w" : ".--" ,
    "x" : "-..-" ,
    "y" : "-.--" ,
    "z" : "--..",
}

def smorse (morseInput):
    list1 = []
    list1[:] = morseInput
    morsewordlist = []
    for index in range(len(list1)):
        morsewordlist.append(morse[list1[index]]) 
    morseword = ''.join(morsewordlist)
    return morseword

print(smorse("programmer"))
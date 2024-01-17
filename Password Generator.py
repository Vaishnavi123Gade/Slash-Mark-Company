import random

letters = ['a',"b", "c" "d", "e", "f", "g", "h", "i", "j", "k" ,"l" ,"m", "n","o","p","q"
           "r", "s", "t", "u", "v", "w", "x", "y" ,"z" ,"A", "B","C","D","E"
           "F", "G", "H", "I", "J", "K", "L", "M" ,"N" ,"O", "P","Q","R","S"
           "T", "U", "V", "W", "X", "Y", "Z"]
number = ['0','1','2','3','4','5','6','7','8','9']
symbols = ["!", "@", "#", "$", "%", "^", "&", "*" ,"(" ,")", "[","]","{","}"]

print("Welcome to Password Generator")
nLetter = int(input("How many LETTER would you like in your password:::\n"))
nNumber = int(input("How many NUMBER would you like in your password:::\n "))
nSymbol = int(input("How many SYMBOL would you like in your password:::\n"))
password_list = []
for s in range(1,nLetter+1):
    char=random.choice(letters)
    password_list+=char
    for s in range(1,nNumber+1):
        char=random.choice(number)
        password_list+=char
    for s in range(1,nSymbol+1):
        char=random.choice(symbols)
        password_list+=char
print(password_list)
random.shuffle(password_list)
print(password_list)
password=""
for char in password_list:
    password+=char
print(password)
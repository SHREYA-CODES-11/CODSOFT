# Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+', '-', '/']
print("Welcome to the Password Generator!")
let = int(input("How many letters do you want in your password?\n"))
num = int(input("How many numbers do you want in your password?\n"))
sym = int(input("How many symbols do you want in your password?\n"))
# Easy level: [letters, numbers, symbols] gets printed in this order only
# for ran_let in range(1, let + 1): #or range(0, let)
#     print(random.choice(letters), end = '')
# for ran_num in range(1, num + 1): #or range(0, num)
#     print(random.choice(numbers), end = '')
# for ran_sym in range(1, sym + 1): #or range(0, sym)
#     print(random.choice(symbols), end = '')

# Hard level: all the characters gets mixed up
password = []
for ran_let in range(0, let): 
    password.append(random.choice(letters))
for ran_num in range(0, num):
    password.append(random.choice(numbers))
for ran_sym in range(0, sym):
    password.append(random.choice(symbols))
random.shuffle(password)
# print(password)
# converting above list into a password string
pass_str = ""
for char in password:
    pass_str += char
print(f"Your strong password is: {pass_str}")
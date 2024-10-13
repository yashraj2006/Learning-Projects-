import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","%","^","&","*","/","|"]

print("Welcome to Password Generator")

user_alphabet = int(input("How many alphabets do you want\n"))
user_number = int(input("How many numbers do you want\n"))
user_symbol = int(input("How many symbols do you want\n"))

#Easy level
'''password = ""

for word in range(1, user_alphabet + 1):
    password += random.choice(alphabets)

for number in range(1, user_number + 1):
    password += random.choice(numbers)

for symbol in range(1, user_symbol + 1):
    password += random.choice(symbols)

print(password)'''


#Hard Level

password_list = []

for word in range(1, user_alphabet + 1):
    password_list.append(random.choice(alphabets))

for number in range(1, user_number + 1):
    password_list.append(random.choice(numbers))

for symbol in range(1, user_symbol + 1):
    password_list.append(random.choice(symbols))

print(password_list)

random.shuffle(password_list)

print(password_list)

password = ""
for word in password_list:
    password += word

print("Your Password is",password)

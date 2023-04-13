# Password Generator
import string
import random

alphabets = [letter for letter in string.ascii_lowercase + string.ascii_uppercase]
numbers = [num for num in string.digits]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

print("Welcome PyPassword Generator!")


# Check for valid input
def is_valid(num: string):
    if num.isdigit() and 0 < int(num) <= 20:
        return True
    return False


# Get Number of alphabets
def get_alpha():
    user_alpha = "0"
    while not is_valid(user_alpha):
        user_alpha = input("Enter the number of alphabets for your password (1-20): ")
        if not is_valid(user_alpha):
            print("Invalid number. Try again.")
    return int(user_alpha)


# Get Number of digits
def get_digits():
    user_digit = "0"
    while not is_valid(user_digit):
        user_digit = input("Enter the number of digits for your password (1-20): ")
        if not is_valid(user_digit):
            print("Invalid number. Try again.")
    return int(user_digit)


# Get Number of symbols
def get_symbols():
    user_symbols = "0"
    while not is_valid(user_symbols):
        user_symbols = input("Enter the number of symbols for your password (1-20): ")
        if not is_valid(user_symbols):
            print("Invalid number. Try again.")
    return int(user_symbols)


alpha_num = get_alpha()
digit_num = get_digits()
symbol_num = get_symbols()

# Start password generation
password = []

while alpha_num > 0:
    password.append(random.choice(alphabets))
    alpha_num -= 1

while digit_num > 0:
    password.append(random.choice(numbers))
    digit_num -= 1

while symbol_num > 0:
    password.append(random.choice(symbols))
    symbol_num -= 1

random.shuffle(password)
password = "".join(password)

print("Your Password is: ", password)

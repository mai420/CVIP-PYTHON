import random
import string

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
special_char = string.punctuation

def generate_password():
    length = int(input('Enter the length of the password (minimum length of the password is 4): '))
    
    while length < 4:
        print('Please enter a valid length (minimum length is 4).')
        length = int(input('Enter the length of the password (minimum length of the password is 4): '))

    password_characters = uppercase + lowercase + digits + special_char
    finpass = ''

    for i in range(length):
        finpass += random.choice(password_characters)

    print('The password is:', finpass)

# Call the function to generate and print the password
generate_password()

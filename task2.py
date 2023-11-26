from tkinter import *
from tkinter import ttk
import random
import array
import pyperclip
import string

# FIXED VALUES


DIGITS = string.digits
LOCASE_CHARACTERS = string.ascii_lowercase

UPCASE_CHARACTERS = string.ascii_uppercase

SYMBOLS = string.punctuation

COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
# #

def checkcond():
    text = int(inputtext.get())
    try:
        if text < 4:
            result_label.config(text = "Input a number greater than 4")
        else:
            global length 
            length = int(inputtext.get())
            result_label.config(text = "")
    except ValueError:
        result_label.config(text = "Invalid input, please give a valid number")




def generate_password():
    global length
    length = int(inputtext.get())
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    temp_pass_list = array.array('u', temp_pass)


    for x in range(length - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        temp_pass_list.append(temp_pass[-1])  # Append the last character to the array
        random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password = password + x

    # print out password
    final_password.set(password)
    global final_password_in_string
    final_password_in_string = password


def copy_to_clipboard():
    print(final_password_in_string)
    pyperclip.copy(final_password_in_string)
    copied_message.set('Copied to clipboard')
    print(final_password_in_string)


# Window Creation
root = Tk()
final_password = StringVar()
copied_message = StringVar()
frm = ttk.Frame(root, padding=50)
frm.grid()
ttk.Label(frm, text="Password Generator", padding=20).grid(column=0, row=0)
ttk.Label(frm, text="Enter the length of the password(minimum length must be 4)", padding=20).grid(column=0, row=1)
inputtext = ttk.Entry(frm, width = 20)
inputtext.grid(column=0, row=2)
inputtext.bind("<FocusOut>", checkcond)
result_label = ttk.Label(frm, text="", padding=20)
result_label.grid(column=0, row=4)
ttk.Button(frm, text="Generate", command=generate_password).grid(column=0, row=5)
ttk.Label(frm, textvariable=final_password, padding=20).grid(column=0, row=6)
ttk.Button(frm, text="Copy to Clipboard", command=copy_to_clipboard).grid(column=0, row=7)
ttk.Label(frm, textvariable=copied_message, padding=10).grid(column=0, row=8)

root.mainloop()


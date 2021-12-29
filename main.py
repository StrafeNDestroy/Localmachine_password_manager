#Only Imports Constants not modules
from tkinter import *
# module inside tkinter
from tkinter import messagebox
from random import choice, randint, shuffle
# Clipboard copy and paste module
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0,END)
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    # Old way
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    # password = ""
    # for char in password_list:
    #   password += char
    # List Comprehension New way

    password_letters = [choice(letters) for number in range(randint(8, 10))]
    password_symbols = [choice(symbols) for number in range(randint(2, 4))]
    password_numbers = [choice(numbers) for number in range(randint(2, 4))]
    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)
    # JOIN method
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
# Messagebox returns Boolean
    if website_entry.get() == "" or email_entry.get() == "" or password_entry.get() == "":
        # ---------Standard Dialogs(Message Box)----------- #
        messagebox.showinfo(title=" Error ❌", message="Blank Fields")

    else:
        # ---------Standard Dialogs(Message Box)----------- #
        ok_to_add = messagebox.askokcancel(title=f"Website: {website_entry.get()}", message=f"Details entered:"
                                                                                        f" \nEmail: {email_entry.get()} "
                                                                                        f"\nPassword: {password_entry.get()}"
                                                                                        f"\nIs it ok to save?")
        if ok_to_add:
            with open("txt.data", "a") as data:
                data.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
# Deletes any entry text inside the entry box using from index 0 to the END character
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# ---------Window Setup----------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")
# ---------Canvas Setup----------- #
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# ---------Label Creation----------- #
website_label = Label(text="Website URL:", font=("Times New Roman", 10, "bold"), foreground="black", bg="white")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", font=("Times New Roman", 10, "bold"), foreground="black", bg="white")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=("Times New Roman", 10, "bold"), foreground="black", bg="white")
password_label.grid(column=0, row=3)

# ---------Entry Setup----------- #
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
# Places cursor inside website entry box on application launch
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
# inserts a text in a specified index IE zero would beginning of entry end would be at the end character of the entry
email_entry.insert(0, "jacobjpadilla@outlook.com")
password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)

# ---------Button Setup----------- #
generate_button = Button(text="Generate Password",command = generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36,command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()




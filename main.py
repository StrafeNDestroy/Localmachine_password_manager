# Only Imports Constants not modules
from tkinter import *
# module inside tkinter
from tkinter import messagebox
from tkinter import simpledialog
from random import choice, randint, shuffle
# Clipboard copy and paste module
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0,END)
# Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for number in range(randint(8, 10))]
    password_symbols = [choice(symbols) for number in range(randint(2, 4))]
    password_numbers = [choice(numbers) for number in range(randint(2, 4))]
    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)

# JOIN method
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- Update Entries Function ------------------------------- #
def update_details():
    try:
        with open("data.json", "r") as data_file:
            # Reading Old Data
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
        website_entry.delete(0, END)
    else:
        update_return_web_name = (simpledialog.askstring("Update Account Password",
                                                         f"Please Enter Website Name")).title()

        if update_return_web_name == None:
            pass
        elif update_return_web_name in data:
            password = (simpledialog.askstring("Update Account Password", f"Please Enter New Password"))
            data[update_return_web_name]['password'] = password
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
            messagebox.showinfo(title="Update Account Password",message=f"Password For {update_return_web_name} Updated")
        else:
            messagebox.showinfo(title="Error", message=f"No entry details for {update_return_web_name} exists")
            website_entry.delete(0, END)


# ---------------------------- Search Function ------------------------------- #
def search():

    website_name = (website_entry.get()).title()
    try:
        with open("data.json", "r") as data_file:
            # Reading Old Data
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found")
        website_entry.delete(0, END)
    else:
        if website_name in data:
            messagebox.showinfo(title="Account Details", message=f"Email: {data[website_name]['email']}\n"
                                                                 f"Password: {data[website_name]['password']}")
            pyperclip.copy(data[website_name]['password'])
        else:
            messagebox.showinfo(title="Error", message=f"No entry details for {website_name} exists")
            website_entry.delete(0, END)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
# Messagebox returns Boolean
    website = (website_entry.get()).title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
                 }
    }

    if website == "" or password_entry.get() == "":
        # ---------Standard Dialogs(Message Box)----------- #
        messagebox.showinfo(title=" Error ❌", message="Blank Fields")

    else:
        # ---------Standard Dialogs(Message Box)----------- #
        ok_to_add = messagebox.askokcancel(title=f"Website: {website}", message=f"Details entered:"
                                                                                        f" \nEmail: {email} "
                                                                                        f"\nPassword: {password}"
                                                                                        f"\nIs it ok to save?")
        if ok_to_add:
            try:
                with open("data.json", "r") as data_file:
                    # Reading Old Data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    # Updating old data with new data
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
    # Deletes any entry text inside the entry box using from index 0 to the END character
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
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
website_label_name = Label(text="Website*:", font=("Times New Roman", 10, "bold"), foreground="black", bg="white")
website_label_name.grid(column=0, row=3, sticky = E)
website_label_url = Label(text="Website Url:", font=("Times New Roman", 10, "bold"), foreground="black", bg="white")
website_label_url.grid(column=0, row=2, sticky = E)
email_label = Label(text="Email/Username*:", font=("Times New Roman", 10, "bold"), foreground="black", bg="white")
email_label.grid(column=0, row=4,sticky = E)
password_label = Label(text="Password*:", font=("Times New Roman", 10, "bold"), foreground="black", bg="white")
password_label.grid(column=0, row=5,sticky = E)
required_fields_label = Label(text="Required Feilds*", font=("Times New Roman", 10, "bold"), foreground="black", bg="white")
required_fields_label.grid(column=0, row=1,sticky = E)

# ---------Entry Setup----------- #
website_entry = Entry(width=35,)
website_entry.grid(column=1, row=3, sticky = W)
# Places cursor inside website entry box on application launch
website_entry.focus()
website_url = Entry(width=35)
website_url.grid(column=1, row=2, sticky = W)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=4, columnspan=2,sticky = W)
# inserts a text in a specified index IE zero would beginning of entry end would be at the end character of the entry
email_entry.insert(0, "jacobjpadilla@outlook.com")
password_entry = Entry(width=35)
password_entry.grid(column=1, row=5,sticky = W)


# ---------Button Setup----------- #
generate_button = Button(text="Generate Password",command = generate_password,width=15)
generate_button.grid(column=2, row=5,sticky=W)
add_button = Button(text="Add", width=30,command=save)
add_button.grid(column=1, row=6,sticky=W)
search_button = Button(text="Search",width=15,command=search)
search_button.grid(column=2,row=3,sticky=W)
update_button  = Button(text="Update Details",command=update_details,width=15)
update_button.grid(column=2, row=4,sticky=W)
window.mainloop()




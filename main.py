from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

NAME_FILE_SAVE = "Text.json"

FONT = 'Comic Sans MS'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def generator_password():
    password_get = passwor_input.get()
    if len(password_get) == 0:
        password_letters = [choice(letters) for _ in range(randint(6, 8))]
        password_numbers = [choice(numbers) for _ in range(randint(2, 6))]

        password_list = password_letters + password_numbers

        shuffle(password_list)

        password = ''.join(password_list)

        passwor_input.insert(0, password)
        pyperclip.copy(password)

    else:
        passwor_input.delete(0, END)
        generator_password()


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_txt_password():
    web_get = web_site_iput.get()
    email_get = email_input.get()
    passwor_get = passwor_input.get()
    new_data = {
        web_get: {
            "email": email_get,
            "password": passwor_get
        }
    }

    if len(web_get) == 0 or len(email_get) == 0 or len(passwor_get) == 0:
        messagebox.showwarning(title="Warning", message='Sorry,some fields are empty')

    else:
        try:
            with open(NAME_FILE_SAVE, 'r') as file:
                # Reading old data
                data = json.load(file)
                # Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            data = new_data

        with open(NAME_FILE_SAVE, "w") as file:
            # Saving updated data
            json.dump(data, file, indent=4)

            web_site_iput.delete(0, END)
            passwor_input.delete(0, END)

        messagebox.showinfo(title='Info', message=f'Password saved successfully for {web_get} '
                                                  f'site in file {NAME_FILE_SAVE}')


# -----------------------------Search----------------------------------- #
def search():
    website_get = web_site_iput.get()
    try:
        with open(NAME_FILE_SAVE, "r") as data_file:
            file = json.load(data_file)
    except:
        messagebox.showinfo(title="Warning", message="File with passwords is empty")
    else:
        if website_get in file:
            email = file[website_get]['email']
            pasword = file[website_get]['password']
            messagebox.showinfo(title=f"{website_get}", message=f"email: {email}\nPassword: {pasword}")
        else:
            messagebox.showinfo(title=f"{website_get}", message=f"Website: '{website_get}', haven't password")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

web_site_label = Label(text='Website:', font=(FONT, 10, 'bold'))
web_site_label.grid(column=0, row=1)

user_name_label = Label(text='Email/Username:', font=(FONT, 10, 'bold'))
user_name_label.grid(column=0, row=2)

password_label = Label(text='Password:', font=(FONT, 10, 'bold'))
password_label.grid(column=0, row=3)

generate_botton = Button(text='Generate Password', font=(FONT, 10, 'bold'), relief='raised', command=generator_password)
generate_botton.grid(column=2, row=3)

add_botton = Button(text='Add', width=36, font=(FONT, 10, 'bold'), relief='raised', command=save_txt_password)
add_botton.grid(column=1, row=4, columnspan=2, sticky=W + E)

search_botton = Button(text="Search", font=(FONT, 10, "bold"), relief="raised", command=search)
search_botton.grid(column=2, row=1, sticky=W + E)

passwor_input = Entry(width=21)
passwor_input.grid(column=1, row=3, sticky=W + E)

web_site_iput = Entry(width=35)
web_site_iput.grid(column=1, row=1, sticky=W + E)
web_site_iput.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, sticky=W + E, columnspan=2)
email_input.insert(0, 'Your email')

window.mainloop()

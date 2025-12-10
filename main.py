import tkinter as tk
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#PASSWORD GENERATOR
def generate_password():
    password = []
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['1','2','3','4','5','6','7','8','9']
    symbols = ['!','@','$','%','&','*','^','~','+']

    user_letter = random.randint(9,12)
    user_number = random.randint(3,6)
    user_symbol = random.randint(2,4)

    for letter in range(0, user_letter):
        password.append(random.choice(alphabet))
    for number in range (0, user_number):
        password.append(random.choice(numbers))
    for symbol in range(0,user_symbol):
        password.append(random.choice(symbols))

    random.shuffle(password)

    new_pass = ""
    for char in password:
        new_pass += char

    password_entry.insert(0,new_pass)

# # ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():

    user_website = website_entry.get()
    user_email = email_entry.get()
    user_password = password_entry.get()

    if user_website == '' or user_email == '' or user_password == '':
        messagebox.showinfo('Error', "Please don't leave any fields empty ")
    else:
        confirm_input = messagebox.askokcancel(title="Password Manager Inputs", message=f"You've entered the following fields:\n Website: {user_website} \n"
                                                                                        f" Email: {user_email} \n Password: {user_password}\n Is the following Entries correct?")
        if confirm_input:
            with open('password_data.txt', 'a') as data:
                data.write(f"{user_website} | {user_email} | {user_password} \n")
                website_entry.delete(0, tk.END)
                email_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)



# # ---------------------------- UI SETUP ------------------------------- #
main_window = tk.Tk()
main_window.title("Password Manager")
#main_window.geometry("500x400")
main_window.config(padx=50, pady=50,)

password_logo = tk.PhotoImage(file="logo.png") #Saved Image

# Created the Canvas and added the Image onto the Canvas
canvas = tk.Canvas(main_window, width=200, height=200,)
canvas.create_image(100, 100, image=password_logo)
canvas.grid(row=0, column=1,)

#Creating my Labels
website_label = tk.Label(main_window, text="Website:") #Website Label
website_label.grid(row=1, column=0) #Coordinates on where the label will be placed on the Canvas.

email_label=tk.Label(main_window, text="Email/Username:") #Email Label
email_label.grid(row=2, column=0) #Coordinates on where the label will be placed on the Canvas.

password_label=tk.Label(main_window, text="Password:") #Password Label
password_label.grid(row=3, column=0) #Coordinates on where the label will be placed on the Canvas.

# Creating my Entry Boxes
website_entry = tk.Entry(main_window, width=35) #Website Entry
website_entry.grid(row=1, column=1, columnspan=2) #Plotting the Entry label on the Canvas

email_entry = tk.Entry(main_window, width=35) #Email Entry
email_entry.grid(row=2, column=1, columnspan=2) #Plotting the Entry label on the Canvas

password_entry = tk.Entry(main_window, width=18)
password_entry.grid(row=3, column=1)

#Creating Generate and Add Buttons
generate_button = tk.Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", width=36, command=add_data)
add_button.grid(row=4, column=1, columnspan=2)





main_window.mainloop()
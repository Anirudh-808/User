import csv , pathlib
from tkinter import messagebox
from tkinter import *

#creating the list of valid users and passwords
users = []
pwds = []
with open('users.csv', 'r' , newline = '') as file:
    reader = csv.DictReader(file)
    for row in reader:
        users.append(row['username'])
        pwds.append(row['password'])

file = pathlib.Path('users.csv')
if file.exists() == False:
    with open('users.csv', 'w' , newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(['username' , 'password'])

def check_valid_user(username , pwd):
    if username == '' or pwd == '':
        messagebox.showerror('Error' , 'Please enter a valid username and password')
        return
    else:
        if username in users:
            if pwds[users.index(username)] == pwd:
                new = Tk()
                new.title('NEW WINDOW')
                new.geometry('500x500')
                new_label = Label(new , text = 'Welcome ' + username , font = ('Arial' , 20) , fg = 'blue')
                new_label.pack()
                new.mainloop()
            else:
                messagebox.showerror('Error' , 'Invalid password')
        else:
            messagebox.showerror('Error' , 'Invalid username')

def sign_up(username , pwd):
    if username == '' or pwd == '':
        messagebox.showerror('Error' , 'Please enter a valid username and password')
        return
    elif username in users:
        messagebox.showerror('Error' , 'Username already exists. Please use another name')
        return
    else:
        with open('users.csv', 'a' , newline = '') as file:
            writer = csv.writer(file)
            writer.writerow([username , pwd])

        messagebox.showinfo('Success' , 'User created successfully. Please login to continue')
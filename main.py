from tkinter import *
import functions , csv , pathlib

root = Tk()
root.title('Login')
root.geometry('500x500')

intro = Label(root , text = "Enter your username and password" , font = ('Arial' , 16))
intro.place(x = 0 , y = 0)

user_entry = Entry(root , width = 20)
user_entry.place(x = 75 , y = 50)
user_label = Label(root , text = 'Username:')
user_label.place(x = 0 , y = 50)

pwd_entry = Entry(root , width = 20 , show = '*')
pwd_entry.place(x = 75 , y = 75)
pwd_label = Label(root , text = 'Password:')
pwd_label.place(x = 0 , y = 75)

login_button = Button(root , text = 'Login' , command = lambda: functions.check_valid_user(user_entry.get() , pwd_entry.get()))
login_button.place(x = 16 , y = 120)

signup_button = Button(root , text = 'Sign Up' , command = lambda : functions.sign_up(user_entry.get() , pwd_entry.get()))
signup_button.place(x = 70 , y = 120)

root.mainloop()


# Signup
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from verifyUser import *
from globals import *

############################ FUNCTIONS ###############################

############################ WINDOW ###############################
signup=Tk()

# Window placement code
screenWidth = signup.winfo_screenwidth()
screenHeight = signup.winfo_screenheight()

appWidth = 600
appHeight = 300

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)

signup.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

signup.title("Sign Up")
signup.resizable(0,0)

############################ ELEMENTS ###############################

# Label Entry Username
lbl_username = Label(signup, text="Username:", fg="red", font=("TkDefaultFont 11"))
lbl_username.place(x=170, y=40)

# Entry Username
txt_username = Entry(signup, width=25)
txt_username.place(x=270, y=40)

# Label Entry Password
lbl_password = Label(signup, text="Password:", fg="red", font=("TkDefaultFont 11"))
lbl_password.place(x=170, y=70)

# Entry Password
txt_password = Entry(signup, width=25, show="*")
txt_password.place(x=270, y=70)

# Label Entry Password
lbl_passwordConfirm = Label(signup, text="Password Confirmation:", fg="red", font=("TkDefaultFont 11"))
lbl_passwordConfirm.place(x=85, y=100)

# Entry Password Confirmation
txt_passwordConfirm = Entry(signup, width=25, show="*")
txt_passwordConfirm.place(x=270, y=100)

# RadioButton Account Type
selected = StringVar()
selected.set("user")

rdbtn_userAcc = Radiobutton(signup, text="Conta User Normal", fg="blue", value="user", variable=selected)
rdbtn_userAcc.place(x=170, y=160)

rdbtn_adminAcc = Radiobutton(signup, text="Conta Admin", fg="blue", value="admin", variable=selected)
rdbtn_adminAcc.place(x=170, y=200)

# Button Sign up
btn_signUp = Button(signup, text="Criar Conta", fg="blue", relief="raised", bd=3, width=10, height=5, command=lambda: verifySignUp(txt_username.get(), txt_password.get(), txt_passwordConfirm.get(), selected.get()))
btn_signUp.place(x=350, y=150)

############################ MAINLOOP ###############################
signup.mainloop()
#Login
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from verifyUser import *
from globals import *

############################ FUNCTIONS ###############################

############################ WINDOW ###############################
login=Tk()

# Window placement code
appWidth = 600
appHeight = 250

screenWidth = login.winfo_screenwidth()
screenHeight = login.winfo_screenheight()

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)

login.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

login.title("Login")
login.resizable(0,0)

############################ ELEMENTS ###############################

# Label Entry Username
lbl_username = Label(login, text="Username:", fg="red", font=("TkDefaultFont 11"))
lbl_username.place(x=150, y=40)

# Entry Username
txt_username = Entry(login, width=25)
txt_username.place(x=250, y=40)

# Label Entry Password
lbl_password = Label(login, text="Password:", fg="red", font=("TkDefaultFont 11"))
lbl_password.place(x=150, y=70)

# Entry Password
txt_password = Entry(login, width=25, show="*")
txt_password.place(x=250, y=70)

# Button Log in
btn_login = Button(login, text="Iniciar Sessão", fg="blue", relief="raised", bd=3, width=20, height=2, command=lambda: verifyLogIn(txt_username.get(), txt_password.get()))
btn_login.place(x=380, y=150)

############################ MAINLOOP ###############################
login.mainloop()
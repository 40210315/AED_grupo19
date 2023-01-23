# Add Game Page
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Combobox
import os
import datetime
from verifyUser import *
from globals import *

############################ FUNCTIONS ###############################
def mainPg():
    addGame.destroy()
    import mainPage

def searchPg():
    addGame.destroy()
    import search

def userPg():
    addGame.destroy()
    import userPage

def logInPg():
    if (verifiedUser[1] == ""):
        import logIn
        if (verifiedUser[1] != ""):
            btn_Login.config(text = "Terminar Sessão")
    else:
        logOut()
        if (verifiedUser[1] == ""):
            btn_Login.config(text = "Iniciar Sessão")

def signUpPg():
    import signUp
    if (verifiedUser[1] != ""):
        btn_Login.config(text = "Terminar Sessão")

def manageUsers():
    import manage_users

def manageGames():
    import manage_games

def selectImg():
    filename = filedialog.askopenfilename(title="Select Image", initialdir=".\\images", filetypes=(("png files", "*.png"), ("all files", "*.*")))

    gameImg.set(filename)
    img = PhotoImage(file = filename)
    ctnImage.itemconfig(115, 115, anchor="c", image=img)

def submitGame():
    gameName = txt_gameName.get()
    gameCategory = cb_category.get()
    gameYear = spin_year.get()
    gameImg = gameImg.get()
    gameDesc = txt_gameDesc.get()
    gameRating = spin_rating.get()
    noRatings = 1

    f_gamesFile = open("files\\games", "r", encoding="utf-8")
    lines = f_gamesFile.readlines()
    f_gamesFile.close()

    for line in lines:
        content = line.split(";")
        if (content[0] == gameName):
            messagebox.showerror(title="Adicionar Jogo", message="Jogo já xiste.")
    
    newLine = gameName + ";" + gameCategory + ";" + gameImg + ";"+ gameDesc + ";" + gameYear + ";" + gameRating + ";" + noRatings + ";" + "\n"
    f_gamesFile = open("files\\games", "a", encoding="utf-8")
    f_gamesFile.write(newLine)
    f_gamesFile.close()
    

############################ WINDOW ###############################
addGame=Tk()

# Window placement code
screenWidth = addGame.winfo_screenwidth()
screenHeight = addGame.winfo_screenheight()

appWidth = 1300
appHeight = 800

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)

addGame.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

addGame.title("Add Game")
addGame.resizable(0,0)

############################ ELEMENTS ###############################
# Button Main Page
btn_MainPg = Button(addGame, text="Página Principal", relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), fg="blue", command=mainPg)
btn_MainPg.place(x=20, y=20)

# Button Add Game
btn_AddGamePg = Button(addGame, text="Adicionar Jogo", relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), fg="blue", state="disabled")
btn_AddGamePg.place(x=360, y=20)

# Button Search
btn_SearchPg = Button(addGame, text="Pesquisa", relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), fg="blue", command=searchPg)
btn_SearchPg.place(x=530, y=20)

# Button User Page
if (verifiedUser[1] == ""):
    userBtnState = "disabled"
else:
    userBtnState = "active"

btn_SearchPg = Button(addGame, text="Página de Utilisador", relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), fg="blue", state=userBtnState, command=userPg)
btn_SearchPg.place(x=700, y=20)

# Button Log In Page
if (verifiedUser[1] == ""):
    logBtnTxt = "Iniciar Sessão"
else:
    logBtnTxt = "Terminar Sessão"

btn_Login = Button(addGame, text=logBtnTxt, relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), fg="white", bg="red", command=logInPg)
btn_Login.place(x=950, y=20)

# Button Sign Up Page
btn_SignUp = Button(addGame, text="Criar Conta", relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), fg="white", bg="red", command=signUpPg)
btn_SignUp.place(x=1120, y=20)

# Label User Welcome
if (verifiedUser[1] != ""):
    welcomeTxt = "Welcome, user {0}!".format(verifiedUser[1])

    txt_userWelcome = Label(text=welcomeTxt, fg="blue")
    txt_userWelcome.place(x=970, y=80)

# BarMenu Manage Games / Users
if (verifiedUser[0] == "admin"):
    bar_Menu = Menu(addGame)

    admin_menu = Menu(bar_Menu)
    admin_menu.add_command(label="Gerir Jogos", command=manageGames)
    admin_menu.add_command(label="Gerir Utilisadoes", command=manageUsers)
    bar_Menu.add_cascade(label="Admin", menu=admin_menu)

    addGame.configure(menu=bar_Menu)

# Entry Game Name
lbl_gameName = Label(addGame, text="Nome:", fg="red", font=("TkDefaultFont", "12", "bold"))
lbl_gameName.place(x=100, y=200)

txt_gameName = Entry(addGame, width=30)
txt_gameName.place(x=180, y=200)

# Combobox Category
lbl_gameCategory = Label(addGame, text="Categoria:", fg="red", font=("TkDefaultFont", "12", "bold"))
lbl_gameCategory.place(x=100, y=250)

f_categories = open("files\\categories.txt", "r", encoding="utf-8")
categories = f_categories.readlines()
f_categories.close()

cb_category = Combobox(addGame, values=categories)
cb_category.place(x=200, y=250)

# Spinbox Launch Year
today = datetime.date.today()
year = today.year

lbl_gameYear = Label(addGame, text="Ano:", fg="red", font=("TkDefaultFont", "12", "bold"))
lbl_gameYear.place(x=100, y=300)

spin_year = Spinbox(addGame, width=5, from_=1990, to=year, increment=1)
spin_year.place(x=150, y=300)

# Text Game Description
lbl_gameDesc = Label(addGame, text="Descrição:", fg="red", font=("TkDefaultFont", "12", "bold"))
lbl_gameDesc.place(x=100, y=350)

txt_gameDesc = Text(addGame, width=40, height=8, relief="sunken", bd=3, wrap="word")
txt_gameDesc.place(x=200, y=350)

# Spinbox Rating 
lbl_gameRating = Label(addGame, text="Avaliação:", fg="red", font=("TkDefaultFont", "12", "bold"))
lbl_gameRating.place(x=100, y=550)

spin_rating = Spinbox(addGame, width=5, from_=1, to=5, increment=1)
spin_rating.place(x=200, y=550)

# Label get game image
lbl_gameImg = Label(addGame, text="Capa de Jogo \n (imagem tem de ser 230x230 \n e na pasta .\images)", fg="blue", font=("TkDefaultFont", "12", "bold"))
lbl_gameImg.place(x=700, y=160)

# Button Get Image (File Dialogue)
gameImg = StringVar()
btn_getImg = Button(addGame, text="Selecionar Ficheiro", fg="red", width=20, height=2, command=selectImg)
btn_getImg.place(x=750, y=480)

# Canvas for game cover image
ctnImage = Canvas(addGame, width=233, height=233, relief="sunken", bd=3, bg="dark grey")
ctnImage.place(x=700, y=230)

# Button Submit Game
btn_getImg = Button(addGame, text="Submeter \n Jogo", fg="blue", width=20, height=4, font=("TkDefaultFont", "14", "bold"), relief="raised", bd=3, command=submitGame)
btn_getImg.place(x=850, y=600)

############################ MAINLOOP ###############################
addGame.mainloop()
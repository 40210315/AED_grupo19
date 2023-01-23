# User Page
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
import os
from verifyUser import *
from globals import *

############################ FUNCTIONS ###############################
def mainPg():
    userPg.destroy()
    import mainPage

def addGamePg():
    userPg.destroy()
    import addGame

def searchPg():
    userPg.destroy()
    import search

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

def gamePage(selected):
    from gamePage import gamePg
    currentItem = tree.focus()
    gameName = tree.item(currentItem, "values")[0]
    gamePg(gameName)

def changeNamePassword(lines, userPos, userName, password):
    newUser = [verifiedUser[0], userName, password, "\n"]
    lines[userPos] = newUser.join(";")

    f_usersFile = open("files\\users.txt", "w", encoding="utf-8")
    for line in lines:
        f_usersFile.writeline(line)
    f_usersFile.close()

def removeFavorite():
    selected = tree.selection()[0]
    tree.delete(selected)

############################ WINDOW ###############################
userPg=Tk()

# Window placement code
screenWidth = userPg.winfo_screenwidth()
screenHeight = userPg.winfo_screenheight()

appWidth = 1300
appHeight = 800

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)

userPg.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

userPg.title("User Page")
userPg.resizable(0,0)

############################ ELEMENTS ###############################
# Button Main Page
btn_MainPg = Button(userPg, text="Página Principal", relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), fg="blue", command=mainPg)
btn_MainPg.place(x=20, y=20)

# Button Add Game
btn_AddGamePg = Button(userPg, text="Adicionar Jogo", relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), fg="blue", command=addGamePg)
btn_AddGamePg.place(x=360, y=20)

# Button Search
btn_SearchPg = Button(userPg, text="Pesquisa", relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), fg="blue", command=searchPg)
btn_SearchPg.place(x=530, y=20)

# Button User Page
btn_SearchPg = Button(userPg, text="Página de Utilisador", relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), fg="blue", state="disabled")
btn_SearchPg.place(x=700, y=20)

# Button Log In Page
if (verifiedUser[1] == ""):
    logBtnTxt = "Iniciar Sessão"
else:
    logBtnTxt = "Terminar Sessão"

btn_Login = Button(userPg, text=logBtnTxt, relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), fg="white", bg="red", command=logInPg)
btn_Login.place(x=950, y=20)

# Button Sign Up Page
btn_SignUp = Button(userPg, text="Criar Conta", relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), fg="white", bg="red", command=signUpPg)
btn_SignUp.place(x=1120, y=20)

# Label User Welcome
if (verifiedUser[1] != ""):
    welcomeTxt = "Welcome, user {0}!".format(verifiedUser[1])

    txt_userWelcome = Label(text=welcomeTxt, fg="blue")
    txt_userWelcome.place(x=970, y=80)

# BarMenu Manage Games / Users
if (verifiedUser[0] == "admin"):
    bar_Menu = Menu(userPg)

    admin_menu = Menu(bar_Menu)
    admin_menu.add_command(label="Gerir Jogos", command=manageGames)
    admin_menu.add_command(label="Gerir Utilisadoes", command=manageUsers)
    bar_Menu.add_cascade(label="Admin", menu=admin_menu)

    userPg.configure(menu=bar_Menu)

# Label Title
lbl_Title = Label(text="User Profile", fg="red", font=("TkDefaultFont", "16", "bold"))
lbl_Title.place(x=20, y=150)

# Label User type
lbl_userType = Label(text="Tipo de User:", fg="blue", font=("TkDefaultFont", "12", "bold"))
lbl_userType.place(x=90, y=250)

txt_userType = Label(text=verifiedUser[0], font=("TkDefaultFont", "12"))
txt_userType.place(x=220, y=250)

# Label Username
lbl_userName = Label(text="Username:", fg="blue", font=("TkDefaultFont", "12", "bold"))
lbl_userName.place(x=90, y=300)

txt_userName = Label(text=verifiedUser[1], font=("TkDefaultFont", "12"))
txt_userName.place(x=220, y=300)

# Label Frame Change Username and Password
frame1 = LabelFrame(userPg, text="Mudar nome/password", fg="blue", width=300, height=300, relief="sunken", bd=3)
frame1.place(x=70, y=400)

# Entry Change Username
lbl_newUserName = Label(frame1, text="Username:", fg="red", font=("TkDefaultFont", "10", "bold"))
lbl_newUserName.place(x=40, y=50)

txt_newUserName = Entry(frame1, width=20)
txt_newUserName.place(x=120, y=50)

# Entry Change Password
lbl_newPassword = Label(frame1, text="Password:", fg="red", font=("TkDefaultFont", "10", "bold"))
lbl_newPassword.place(x=40, y=100)

txt_newPassord = Entry(frame1, width=20)
txt_newPassord.place(x=120, y=100)

# Button Change username/password
btn_newUserInfo = Button(frame1, text="Mudar user/Palavra-passe", fg="blue", width=25, height=2, command=lambda: changeNamePassword(lines, userPos, txt_newUserName.get(), txt_newPassord.get()))
btn_newUserInfo.place(x=40, y=180)

# Label Favourites
lbl_Title = Label(text="Favoritos", fg="red", font=("TkDefaultFont", "16", "bold"))
lbl_Title.place(x=600, y=150)

# Treeview Game
panel1 = PanedWindow(userPg, width=550, height=300, relief="sunken", bd=2)
panel1.place(x=550, y=200)

global tree
tree = ttk.Treeview(panel1, selectmode="browse", columns=("Nome", "Categoria", "Data Launch", "Avaliação"), show="headings", height=300)

tree.column("Nome", width=155, anchor="c")
tree.heading("Nome", text="Nome")

tree.column("Categoria", width=130, anchor="c")
tree.heading("Categoria", text="Categoria")

tree.column("Data Launch", width=130, anchor="c")
tree.heading("Data Launch", text="Data Launch")

tree.column("Avaliação", width=130, anchor="c")
tree.heading("Avaliação", text="Avaliação")

tree.place(x=0, y=0)

# Scroll bar
verscrlbar = ttk.Scrollbar(panel1, orient ="vertical", command = tree.yview)
# CallinPlace da Scrollbar
verscrlbar.place(x=530, y=0, height=300)
# Adicionar scrollbar à  treeview
tree.configure(yscrollcommand = verscrlbar.set)

# Adicionar linhas à treewview
f_usersFile = open("files\\users.txt", "r", encoding="utf-8")
lines = f_usersFile.readlines()
f_usersFile.close()

lines.pop(0)

for i in range(len(lines)):
    content = lines[i].split(";")
    if (content[1] == verifiedUser[1]):
        userPos = i

favorites = lines[userPos].split(";")[3].split("-")

f_gamesFile = open("files\\games.txt", "r", encoding="utf-8")
linesGames = f_gamesFile.readlines()
f_gamesFile.close()

treeLines = []

for i in range(len(favorites)):
    for line in linesGames:
        if (favorites[i] == line.split(";")[0]):
            treeLines.append(line)

for line in treeLines:
    content = line.split(";")
    tree.insert("", "end", values=(content[0], content[1], content[4], content[5]))

# Button Go to Selected Page
btn_selected = Button(userPg, text="Ir para página", fg="blue", width=15, height=2, font=("TkDefaultFont", "12"), relief="raised", bd=3, command=lambda: gamePage(tree.selection()[0]))
btn_selected.place(x=550, y=520)

# Button Remove from Favourites
btn_remove = Button(userPg, text="Remover de Favoritos", fg="blue", width=20, height=2, font=("TkDefaultFont", "12"), relief="raised", bd=3, command=removeFavorite)
btn_remove.place(x=750, y=520)

############################ MAINLOOP ###############################
userPg.mainloop()
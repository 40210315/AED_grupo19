# Search Page
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
import os
from verifyUser import *
from globals import *
import datetime

############################ FUNCTIONS ###############################
def mainPg():
    search.destroy()
    import mainPage

def addGamePg():
    search.destroy()
    import addGame

def userPg():
    search.destroy()
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

def applyFilters(lines, gameName, gameCategory, gameYear, gameRating):
    newLines = lines.copy()
    if (gameName != ""):
        newLines = filter(lambda line: line.split(";")[0] == gameName, newLines)
    if (gameCategory != ""):
        newLines = filter(lambda line: line.split(";")[0] == gameCategory, newLines)
    if (gameYear != ""):
        newLines = filter(lambda line: line.split(";")[0] == gameCategory, newLines)
    if (gameRating != ""):
        newLines = filter(lambda line: line.split(";")[0] == gameCategory, newLines)

    for item in tree.get_children():
        tree.delete(item)

    for line in newLines:
        content = line.split(";")
        tree.insert("", "end", values=(content[0], content[1], content[5], content[6]))

def gamePage(selected):
    from gamePage import gamePg
    currentItem = tree.focus()
    gameName = tree.item(currentItem, "values")[0]
    gamePg(gameName)

############################ WINDOW ###############################
search=Tk()

# Window placement code
screenWidth = search.winfo_screenwidth()
screenHeight = search.winfo_screenheight()

appWidth = 1300
appHeight = 800

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)

search.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

search.title("Search")
search.resizable(0,0)

############################ ELEMENTS ###############################
# Button Main Page
btn_MainPg = Button(search, text="Página Principal", relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), fg="blue", command=mainPg)
btn_MainPg.place(x=20, y=20)

# Button Add Game
btn_AddGamePg = Button(search, text="Adicionar Jogo", relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), fg="blue", command=addGamePg)
btn_AddGamePg.place(x=360, y=20)

# Button Search
btn_SearchPg = Button(search, text="Pesquisa", relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), fg="blue", state="disabled")
btn_SearchPg.place(x=530, y=20)

# Button User Page
if (verifiedUser[1] == ""):
    userBtnState = "disabled"
else:
    userBtnState = "active"

btn_SearchPg = Button(search, text="Página de Utilisador", relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), fg="blue", state=userBtnState, command=userPg)
btn_SearchPg.place(x=700, y=20)

# Button Log In Page
if (verifiedUser[1] == ""):
    logBtnTxt = "Iniciar Sessão"
else:
    logBtnTxt = "Terminar Sessão"

btn_Login = Button(search, text=logBtnTxt, relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), fg="white", bg="red", command=logInPg)
btn_Login.place(x=950, y=20)

# Button Sign Up Page
btn_SignUp = Button(search, text="Criar Conta", relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), fg="white", bg="red", command=signUpPg)
btn_SignUp.place(x=1120, y=20)

# Label User Welcome
if (verifiedUser[1] != ""):
    welcomeTxt = "Welcome, user {0}!".format(verifiedUser[1])

    txt_userWelcome = Label(text=welcomeTxt, fg="blue")
    txt_userWelcome.place(x=970, y=80)

# BarMenu Manage Games / Users
if (verifiedUser[0] == "admin"):
    bar_Menu = Menu(search)

    admin_menu = Menu(bar_Menu)
    admin_menu.add_command(label="Gerir Jogos", command=manageGames)
    admin_menu.add_command(label="Gerir Utilisadoes", command=manageUsers)
    bar_Menu.add_cascade(label="Admin", menu=admin_menu)

    search.configure(menu=bar_Menu)

# Entry Game Name
lbl_gameName = Label(search, text="Nome:", fg="red", font=("TkDefaultFont", "12", "bold"))
lbl_gameName.place(x=100, y=200)

txt_gameName = Entry(search, width=30)
txt_gameName.place(x=180, y=200)

# Combobox Category
lbl_gameCategory = Label(search, text="Categoria:", fg="red", font=("TkDefaultFont", "12", "bold"))
lbl_gameCategory.place(x=100, y=250)

f_categories = open("files\\categories.txt", "r", encoding="utf-8")
categories = f_categories.readlines()
f_categories.close()

cb_category = Combobox(search, values=categories)
cb_category.place(x=200, y=250)

# Spinbox Launch Year
today = datetime.date.today()
year = today.year

lbl_gameYear = Label(search, text="Ano:", fg="red", font=("TkDefaultFont", "12", "bold"))
lbl_gameYear.place(x=100, y=300)

spin_year = Spinbox(search, width=5, from_=1990, to=year, increment=1)
spin_year.place(x=150, y=300)

# Spinbox Rating 
lbl_gameRating = Label(search, text="Avaliação:", fg="red", font=("TkDefaultFont", "12", "bold"))
lbl_gameRating.place(x=100, y=350)

spin_rating = Spinbox(search, width=5, from_=1, to=5, increment=1)
spin_rating.place(x=200, y=350)

# Button Search
btn_search = Button(search, text="Pesquisar", fg="blue", width=15, height=2, font=("TkDefaultFont", "12"), relief="raised", bd=3, command=lambda: applyFilters(lines, txt_gameName.get(), cb_category.get(), spin_year.get(), spin_rating.get()))
btn_search.place(x=150, y=450)

# Button Go to Selected Page
btn_selected = Button(search, text="Ir para página", fg="blue", width=15, height=2, font=("TkDefaultFont", "12"), relief="raised", bd=3, command=lambda: gamePage(tree.selection()[0]))
btn_selected.place(x=500, y=500)

# Treeview Game
panel1 = PanedWindow(search, width=550, height=300, relief="sunken", bd=2)
panel1.place(x=500, y=150)

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
f_gamesFile = open("files\\games.txt", "r", encoding="utf-8")
lines = f_gamesFile.readlines()
f_gamesFile.close()

lines.pop(0)

for line in lines:
    content = line.split(";")
    tree.insert("", "end", values=(content[0], content[1], content[4], content[5]))

############################ MAINLOOP ###############################
search.mainloop()
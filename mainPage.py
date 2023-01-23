# Main Page
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
import os
from verifyUser import *
from globals import *

############################ FUNCTIONS ###############################
def addGamePg():
    main.destroy()
    import addGame

def searchPg():
    main.destroy()
    import search

def userPg():
    main.destroy()
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

def gamePg(gameName):
    import gamePage
    gamePg(gameName)

def manageUsersPg():
    import manage_users

def manageGamesPg():
    import manage_users

############################ WINDOW ###############################
main=Tk()

# Window placement code
screenWidth = main.winfo_screenwidth()
screenHeight = main.winfo_screenheight()

appWidth = 1300
appHeight = 800

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)

main.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

main.title("Main Page")
main.resizable(0,0)

############################ ELEMENTS ###############################

panel1 = PanedWindow(main, height=320, width=1270, relief="sunken", bd=3, bg="dark grey")
panel1.place(x=15, y=430)

f = open("files\\games.txt", "r", encoding="utf-8")
gameList = f.readlines()
f.close()

gameList.pop(0)
gameListLast = gameList[-5:]

# Label Last Additions
lbl_last = Label(panel1, text="Últimas Adições", fg="blue", font=("TkDefaultFont", "12", "bold", "underline"), bg="dark grey")
lbl_last.place(x=550, y=15)

posX = [15, 265, 515, 765, 1015]
names = []
img = []

for i in range(len(gameListLast)):
    content = gameListLast[i].split(";")

    names.append(content[0])
    img.append(content[2])

# Button Last Addition 1
image1 = PhotoImage(file=img[0])
btn_new1 = Button(panel1, text=names[0], fg="red", font=("TkDefaultFont", "12", "bold"), relief="raised", bd=3, width=230, height=250, image=image1, compound=TOP, command=lambda: gamePg(names[0]))
btn_new1.place(x=posX[0], y=50)

# Button Last Addition 2
image2 = PhotoImage(file=img[1])
btn_new2 = Button(panel1, text=names[1], fg="red", font=("TkDefaultFont", "12", "bold"), relief="raised", bd=3, width=230, height=250, image=image2, compound=TOP, command=lambda: gamePg(names[1]))
btn_new2.place(x=posX[1], y=50)

# Button Last Addition 3
image3 = PhotoImage(file=img[2])
btn_new3 = Button(panel1, text=names[2], fg="red", font=("TkDefaultFont", "12", "bold"), relief="raised", bd=3, width=230, height=250, image=image3, compound=TOP, command=lambda: gamePg(names[2]))
btn_new3.place(x=posX[2], y=50)

# Button Last Addition 4
image4 = PhotoImage(file=img[3])
btn_new4 = Button(panel1, text=names[3], fg="red", font=("TkDefaultFont", "12", "bold"), relief="raised", bd=3, width=230, height=250, image=image4, compound=TOP, command=lambda: gamePg(names[3]))
btn_new4.place(x=posX[3], y=50)

# Button Last Addition 5
image5 = PhotoImage(file=img[4])
btn_new5 = Button(panel1, text=names[4], fg="red", font=("TkDefaultFont", "12", "bold"), relief="raised", bd=3, width=230, height=250, image=image5, compound=TOP, command=lambda: gamePg(names[4]))
btn_new5.place(x=posX[4], y=50)

############################################
############################################
############################################

panel2 = PanedWindow(main, height=320, width=1270, relief="sunken", bd=3, bg="dark grey")
panel2.place(x=15, y=100)

highestRated = []
rating = 5

while (len(highestRated) < 5):
    for i in range(len(gameList)):
        content = gameList[i].split(";")
        if (content[5] == str(rating)):
            highestRated.append(gameList[i])
        print(highestRated)
    rating -= 1

posX = [15, 265, 515, 765, 1015]

names1 = []
img1 = []

for i in range(len(highestRated)):
    content = highestRated[i].split(";")

    names1.append(content[0])
    img1.append(content[2])

# Label Highest Rated
lbl_highest = Label(panel2, text="Highest Rating", fg="blue", font=("TkDefaultFont", "12", "bold", "underline"), bg="dark grey")
lbl_highest.place(x=550, y=15)

# Button Top Rated 1
image1 = PhotoImage(file=img1[0])
btn_highest1 = Button(panel2, text=names1[0], fg="red", font=("TkDefaultFont", "12", "bold"), relief="raised", bd=3, width=230, height=250, image=image1, compound=TOP, command=lambda: gamePg(names1[0]))
btn_highest1.place(x=posX[0], y=50)

# Button Top Rated 2
image2 = PhotoImage(file=img1[1])
btn_highest1 = Button(panel2, text=names1[1], fg="red", font=("TkDefaultFont", "12", "bold"), relief="raised", bd=3, width=230, height=250, image=image2, compound=TOP, command=lambda: gamePg(names1[1]))
btn_highest1.place(x=posX[1], y=50)

# Button Top Rated 3
image3 = PhotoImage(file=img1[2])
btn_name = Button(panel2, text=names1[2], fg="red", font=("TkDefaultFont", "12", "bold"), relief="raised", bd=3, width=230, height=250, image=image3, compound=TOP, command=lambda: gamePg(names1[2]))
btn_name.place(x=posX[2], y=50)

# Button Top Rated 4
image4 = PhotoImage(file=img1[3])
btn_name = Button(panel2, text=names1[3], fg="red", font=("TkDefaultFont", "12", "bold"), relief="raised", bd=3, width=230, height=250, image=image4, compound=TOP, command=lambda: gamePg(names1[3]))
btn_name.place(x=posX[3], y=50)

# Button Top Rated 5
image5 = PhotoImage(file=img1[4])
btn_name = Button(panel2, text=names1[4], fg="red", font=("TkDefaultFont", "12", "bold"), relief="raised", bd=3, width=230, height=250, image=image5, compound=TOP, command=lambda: gamePg(names1[4]))
btn_name.place(x=posX[4], y=50)


#############################################
#############################################
#############################################

# Button Main Page
btn_MainPg = Button(main, text="Página Principal", relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), fg="blue", state="disabled")
btn_MainPg.place(x=20, y=20)

# Button Add Game
btn_AddGamePg = Button(main, text="Adicionar Jogo", relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), fg="blue", command=addGamePg)
btn_AddGamePg.place(x=360, y=20)

# Button Search
btn_SearchPg = Button(main, text="Pesquisa", relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), fg="blue", command=searchPg)
btn_SearchPg.place(x=530, y=20)

# Button User Page
if (verifiedUser[1] == ""):
    userBtnState = "disabled"
else:
    userBtnState = "active"

btn_SearchPg = Button(main, text="Página de Utilisador", relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), fg="blue", state=userBtnState, command=userPg)
btn_SearchPg.place(x=700, y=20)

# Button Log In Page
if (verifiedUser[1] == ""):
    logBtnTxt = "Iniciar Sessão"
else:
    logBtnTxt = "Terminar Sessão"

btn_Login = Button(main, text=logBtnTxt, relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), fg="white", bg="red", command=logInPg)
btn_Login.place(x=950, y=20)

# Button Sign Up Page
btn_SignUp = Button(main, text="Criar Conta", relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), fg="white", bg="red", command=signUpPg)
btn_SignUp.place(x=1120, y=20)

# Label User Welcome
if (verifiedUser[1] != ""):
    welcomeTxt = "Welcome, user {0}!".format(verifiedUser[1])

    txt_userWelcome = Label(text=welcomeTxt, fg="blue")
    txt_userWelcome.place(x=970, y=80)

# BarMenu Manage Games / Users
if (verifiedUser[0] == "admin"):
    bar_Menu = Menu(main)

    admin_menu = Menu(bar_Menu)
    admin_menu.add_command(label="Gerir Jogos", command=manageGamesPg)
    admin_menu.add_command(label="Gerir Utilisadoes", command=manageUsersPg)
    bar_Menu.add_cascade(label="Admin", menu=admin_menu)

    main.configure(menu=bar_Menu)

############################ MAINLOOP ###############################
main.mainloop()
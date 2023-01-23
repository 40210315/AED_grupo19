# Game Page
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
import os
from verifyUser import *
from globals import *

def gamePg(gameName):
    ############################ FUNCTIONS ###############################
    def nextComment(commPos):
        txt_user.config(state="normal")
        txt_user.delete(END)

        txt_comment.config(state="normal")
        txt_comment.delete(END)

        if (commPos+1 == len(comments)):
            commPos = 0
        else:
            commPos += 1

        user = comments[commPos][1]
        comment = comments[commPos][2]

        txt_user.insert(INSERT, user)
        txt_user.config(state="disabled")

        txt_comment.insert(INSERT, comment)
        txt_comment.config(state="disabled")

    def lastComment(commPos):
        txt_user.config(state="normal")
        txt_user.delete(END)

        txt_comment.config(state="normal")
        txt_comment.delete(END)

        if (commPos == 0):
            commPos = len(comments)-1
        else:
            commPos -= 1

        user = comments[commPos][1]
        comment = comments[commPos][2]

        txt_user.insert(INSERT, user)
        txt_user.config(state="disabled")

        txt_comment.insert(INSERT, comment)
        txt_comment.config(state="disabled")

    def newComment():
        # Paned Window Comment 
        commPanel = PanedWindow(game, width=500, height=250, relief="raised", bd=3)
        commPanel.place(x=100, y=100)

        # Label Comment Text Entry
        lbl_comment = Label(commPanel, text="Commentário:", fg="blue", font=("TkDefaultFont", "10", "bold"))
        lbl_comment.place(x=20, y=20)

        # Text Commment
        txt_comment = Text(commPanel, width=50, height=8, wrap="word")
        txt_comment.place(x=20, y=50)

        # Button close Paned Window
        btn_panelClose = Button(commPanel, text="Cancelar", fg="red", command=commPanel.destroy)
        btn_panelClose.place(x=20, y=200)

        # Button Add Comment
        btn_addComment = Button(commPanel, text="Deixar Comentário", fg="red", command=lambda: addComment(txt_comment.get()))
        btn_addComment.place(x=100, y=200)

    def addComment(commentTxt):
        f_commentsFile = open("files\\comments.txt", "a", encoding="utf-8")
        newLine = gameName + ";" + verifiedUser[1] + ";" + commentTxt + ";" + "\n"
        f_commentsFile.write(newLine)
        f_commentsFile.close()

    def addFavourites():
        f_users = open("files\\users.txt", "r")
        lines = f_users.readlines()
        f_users.close()

        for i in range(len(lines)):
            content = lines[i].split(";")
            if (content[1] == verifiedUser[1]):
                pos = i

        newLine = lines[pos].split(";")
        if (newLine[3] == "Ainda não tem favoritos"):
            newLine[3] = gameName
        else:
            newLine[3] += "-" + gameName

        lines[pos] = ";".join(newLine)

        f_users = open("files\\games.txt", "w")
        for line in lines:
            f_users.write(line)
        f_users.close()

    def submitRating():
        rating = spin_rating.get()
        
        f_gamesFile = open("files\\games.txt", "r", encoding="utf-8")
        lines = f_gamesFile.readlines()
        f_gamesFile.close()

        for i in range(len(lines)):
            content = lines[i].split(";")
            if (content[0] == gameName):
                pos = i

        newLine = lines[pos].split(";")
        oldRating = int(newLine[5])
        numRatings = int(newLine[6])

        newRating = ((oldRating*numRatings) + rating) / numRatings + 1

        newLine[5] = str(round(newRating, 0))
        newLine[6] = str(numRatings + 1)

        lines[pos] = ";".join(newLine)

        f_gamesFile = open("files\\games.txt", "w")
        for line in lines:
            f_gamesFile.write(line)
        f_gamesFile.close()

    ############################ WINDOW ###############################
    game=Tk()

    # Window placement code
    screenWidth = game.winfo_screenwidth()
    screenHeight = game.winfo_screenheight()

    appWidth = 800
    appHeight = 700

    x = (screenWidth/2) - (appWidth/2)
    y = (screenHeight/2) - (appHeight/2)

    game.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

    game.title("Game Page")
    game.resizable(0,0)

    ############################ ELEMENTS ###############################
    f_gamesFile = open("files\\games.txt", "r", encoding="utf-8")
    lines = f_gamesFile.readlines()
    f_gamesFile.close()

    for i in range(len(lines)):
        if (lines[i].split(";")[0] == gameName):
            linePos = i

    content = lines[linePos].split(";")

    # Canvas Game Cover image
    ctnImage = Canvas(game, width=230, height=230)
    ctnImage.place(x=20, y=20)

    img = PhotoImage(file=content[2])
    ctnImage.create_image(0, 0, anchor="nw", image=img)

    # Label Game Name
    txt_gameName = Label(game, text=content[0], fg="blue", font=("TkDefaultFont", "20", "bold"))
    txt_gameName.place(x=300, y=30)

    # Text Block Description
    description = content[3]
    txt_gameDesc = Text(game, width=50, height=10, relief="sunken", bd=3, wrap="word")
    txt_gameDesc.insert(INSERT, description)
    txt_gameDesc.config(state="disabled")
    txt_gameDesc.place(x=300, y=80)

    # Label Game Category
    lbl_gameCateg = Label(game, text="Categoria: " + content[1], fg="red", font=("TkDefaultFont", "12"))
    lbl_gameCateg.place(x=20, y=280)

    txt_gameCateg = Label(game, text=content[1], font=("TkDefaultFont", "12"))
    txt_gameCateg.place(x=100, y=280)

    # Label Game Launch Year
    lbl_gameYear = Label(game, text="Ano de Lançamento: ", fg="red", font=("TkDefaultFont", "12"))
    lbl_gameYear.place(x=20, y=310)

    txt_gameYear = Label(game, text=content[4], font=("TkDefaultFont", "12"))
    txt_gameYear.place(x=170, y=310)

    # Label Game Rating
    lbl_gameRate = Label(game, text="Avaliação: ", fg="red", font=("TkDefaultFont", "12"))
    lbl_gameRate.place(x=310, y=280)

    txt_gameRate = Label(game, text=content[5], font=("TkDefaultFont", "12"))
    txt_gameRate.place(x=390, y=280)

    # Label Game Rating Amount
    lbl_gameRate = Label(game, text="Nº Avaliações: ", fg="red", font=("TkDefaultFont", "12"))
    lbl_gameRate.place(x=310, y=310)

    txt_gameRate = Label(game, text=content[6], font=("TkDefaultFont", "12"))
    txt_gameRate.place(x=420, y=310)

    # Panel Comments
    panel1 = PanedWindow(game, height=225, width=760, bg="dark grey", relief="raised", bd=3)
    panel1.place(x=20, y=450)

    f_commentFile = open("files\\comments.txt", "r", encoding="utf-8")
    lines = f_commentFile.readlines()
    f_commentFile.close()

    lines.pop(0)

    comments = []

    for line in lines:
        gameName = line.split(";")[0]
        if (gameName == content[0]):
            comments.append(line)

    for i in range(len(comments)):
        comments[i] = str(comments[i]).split(";")

    if (len(comments) == 0):
        lbl_noComments = Label(panel1, text="Esta página ainda não tem comentários :(", fg="red", bg="dark grey", font=("TkDefaultFont", "12", "bold"))
        lbl_noComments.place(x=20, y=20)
    else:
        commPos = 0
        # Label Comment Username
        lbl_user = Label(panel1, text="Username:", font=("TkDefaultFont", "10", "bold"))
        lbl_user.place(x=20, y=20)

        # Comment Username
        user = comments[commPos][1]
        txt_user = Entry(panel1, width=20)
        txt_user.insert(INSERT, user)
        txt_user.config(state="disabled")
        txt_user.place(x=100, y=20)

        # Text Comment
        comment = comments[commPos][2]
        txt_comment = Text(panel1, width=87, height=6, relief="sunken", bd=3, wrap="word")
        txt_comment.insert(INSERT, comment)
        txt_comment.config(state="disabled")
        txt_comment.place(x=20, y=50)

        # Button forward and back
        btn_nextComm = Button(panel1, text=">>>", width=30, height=2, command=lambda: (nextComment(commPos)))
        btn_nextComm.place(x=380, y=165)

        btn_lastComm = Button(panel1, text="<<<", width=30, height=2, command=lambda: (lastComment(commPos)))
        btn_lastComm.place(x=150, y=165)


    if (verifiedUser[1] == ""):
        btnState = "disabled"
    else:
        btnState = "active"

    # Button Make Comment
    btn_newComment = Button(game, text="Adicionar Comentário", width=20, height=2, fg="blue", state=btnState, command=newComment)
    btn_newComment.place(x=30, y=370)

    # Button Add to Favourites
    btn_addFavourites = Button(game, text="Adicionar aos Favoritos", width=20, height=2, fg="blue", state=btnState, command=addFavourites)
    btn_addFavourites.place(x=200, y=370)

    # Label Rating
    lbl_rating = Label(game, text="Avaliação:", fg="blue", font=("TkDefaultFont", "12"))
    lbl_rating.place(x=580, y=300)

    # Spin Box Rating Option
    spin_rating = Spinbox(game, width=5, from_=1, to=5, increment=1)
    spin_rating.place(x=680, y=300)

    # Button Leave Rating
    btn_leaveRating = Button(game, text="Submeter Avaliação", width=20, height=2, fg="red", state=btnState, command=submitRating)
    btn_leaveRating.place(x=570, y=330)

    ############################ MAINLOOP ###############################
    game.mainloop()

gamePg("Subnautica") # Dados de Controlo

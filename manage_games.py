# Manage Games
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from verifyUser import *
from globals import *

############################ FUNCTIONS ###############################
def applyFilters(lines, gameName, gameCategory):
    newLines = lines.copy()
    if (gameName != ""):
        newLines = filter(lambda line: line.split(";")[0] == gameName, newLines)
    if (gameCategory != ""):
        newLines = filter(lambda line: line.split(";")[0] == gameCategory, newLines)

    for item in tree.get_children():
        tree.delete(item)

    for line in newLines:
        content = line.split(";")
        tree.insert("", "end", values=(content[0], content[1], content[5], content[6]))

def deleteSelected():
    selected = tree.selection()[0]
    currentItem = tree.focus()
    gameName = tree.item(currentItem, "values")[0]

    f_gamesFile = open("files\\games.txt", "r+", encoding="utf-8")
    lines = f_gamesFile.readlines()

    for line in lines:
        content = line.split(";")
        if (content[0] == gameName):
            lines.remove(line)

    f_gamesFile.writelines(lines)
    f_gamesFile.close()

    tree.delete(selected)

############################ WINDOW ###############################
manageGames=Tk()

# Window placement code
screenWidth = manageGames.winfo_screenwidth()
screenHeight = manageGames.winfo_screenheight()

appWidth = 900
appHeight = 350

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)

manageGames.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

manageGames.title("Manage Games Page")
manageGames.resizable(0,0)

############################ ELEMENTS ###############################
# Menu Barra
barra_Menu = Menu(manageGames)

# Games Menu Cascade
games_Menu = Menu(barra_Menu)
games_Menu.add_command(label="Pesquisa", command="noaction")
barra_Menu.add_cascade(label="Jogos", menu=games_Menu)

# User Menu Cascade
user_Menu = Menu(barra_Menu)
user_Menu.add_command(label="Perfil de Utilizador", command="noaction")
barra_Menu.add_cascade(label="Utilizador", menu=user_Menu)

# Admin Menu Cascade
admin_Menu = Menu(barra_Menu)
admin_Menu.add_command(label="Gerir Utilizadores", command="noaction")
admin_Menu.add_command(label="Gerir Jogos", command="noaction")
barra_Menu.add_cascade(label="Admin", menu=admin_Menu)

# Close Option
barra_Menu.add_command(label="Sair", command=manageGames.destroy)

manageGames.configure(menu=barra_Menu)

# LabelFrame Filter
frame1 = LabelFrame(manageGames, text="Filtros", fg="red", width=300, height=210, relief="sunken", bd=3)
frame1.place(x=10, y=10)

# Label Entry Game Name
lbl_gameName = Label(frame1, text="Nome do Jogo:", fg="blue")
lbl_gameName.place(x=20, y=30)

# Entry Game Search
txt_gameName = Entry(frame1, width=25)
txt_gameName.place(x=110, y=30)

# Label Category 
lbl_gameCat = Label(frame1, text="Categoria:", fg="blue")
lbl_gameCat.place(x=20, y=80)

# Combobox Category
f_categories = open("files\\categories.txt", "r", encoding="utf-8")
categoryList = f_categories.readlines()
f_categories.close()

cb_category = Combobox(frame1, values=categoryList)
cb_category.place(x=110, y=80)

# Button Filter
btn_search = Button(frame1, text="Filtrar", fg="red", width=15, height=2, command=lambda: applyFilters(lines, txt_gameName.get(), cb_category.get()))
btn_search.place(x=120, y=130)

# Button Delete Game
btn_del = Button(manageGames, text="Apagar Seleção", fg="blue", width=25, height=3, command=deleteSelected)
btn_del.place(x=40, y= 250)

# Treeview Game
panel1 = PanedWindow(manageGames, width=550, height=300, relief="sunken", bd=2)
panel1.place(x=330, y=20)

global tree
tree = ttk.Treeview(panel1, selectmode="browse", columns=("Nome", "Categoria", "Avalição", "Nº de Avaliações"), show="headings", height=300)

tree.column("Nome", width=155, anchor="c")
tree.heading("Nome", text="Nome")

tree.column("Categoria", width=130, anchor="c")
tree.heading("Categoria", text="Categoria")

tree.column("Avalição", width=130, anchor="c")
tree.heading("Avalição", text="Avalição")

tree.column("Nº de Avaliações", width=130, anchor="c")
tree.heading("Nº de Avaliações", text="Nº de Avaliações")

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
    tree.insert("", "end", values=(content[0], content[1], content[5], content[6]))

############################ MAINLOOP ###############################
manageGames.mainloop()
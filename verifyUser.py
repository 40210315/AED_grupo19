from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from globals import *

fUsers = "files\\users.txt"

def logOut():
    verifiedUser[0] = ""
    verifiedUser[1] = ""

def verifyLogIn(userName, password):
    f = open(fUsers, "r", encoding="utf-8")
    listUsers = f.readlines()
    f.close()

    listUsers.pop(0)

    for linha in listUsers:
        content = linha.split(";")
        if (content[1] == userName) and (content[2] == password):
            verifiedUser[0] = content[0]
            verifiedUser[1] = userName
    messagebox.showerror("Iniciar Sessão", "Username ou password inválidos.")

def verifySignUp(userName, password, passwordConfirm, userType):
    if (password != passwordConfirm):
        messagebox.showerror("Criar Conta", "Passwords inseridas não coincidem.")
        return

    if (userName == "") or (password == ""):
        messagebox.showerror("Criar Conta", "Campos vazios inválidos.")
        return
    f = open(fUsers, "r", encoding="utf-8")
    listUsers = f.readlines()
    f.close()

    listUsers.pop(0)

    for linha in listUsers:
        content = linha.split(";")
        if (content[1] == userName):
            messagebox.showerror("Criar Conta", "Username já em uso.")
            return
    
    f = open(fUsers, "a")
    line = userType + ";" + userName + ";" + password + "\n"
    f.write(linha)
    f.close()
    verifiedUser[1] = userName
    verifiedUser[0] = userType
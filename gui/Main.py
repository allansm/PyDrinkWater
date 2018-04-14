from persistence.UserDao import *
from persistence.CupDao import *
from gui.Cadastro import Cadastro
from gui.Painel import Painel
import tkinter
from tkinter import ttk
from tkinter import *

class Main(tkinter.Tk):
    def auth(self,login,senha):
        user = User()
        user.setLogin(login)
        user.setPassword(senha)
        fetch = UserDao().autenticate(user)
        user.setId(fetch[0])
        user.setLogin(fetch[1])
        user.setPassword(fetch[2])
        return user
    def execute(self):
        self.title("DrinkWater/Login")
        self.geometry("400x300")
        self.resizable(False, False)
        x = 90
        y = 30
        label =ttk.Label(text = "login" ,font=20)
        label.place(x=x,y=y)
        login = tkinter.StringVar()
        input = ttk.Entry(width=35,textvariable=login)
        input.place(x=x,y=y+50)
        label = ttk.Label(text="senha",font=20)
        label.place(x=x, y=y+100)
        senha = tkinter.StringVar()
        input = ttk.Entry(width=35 ,textvariable=senha,show="*")
        input.place(x=x, y=y+150)
        def autenticar():
            user = self.auth(login.get(),senha.get())
            Painel().execute(user)
        button = ttk.Button(text="Autenticar" ,command=autenticar)
        button.place(x=x,y=y+200)
        def cadastro():
           Cadastro().execute()
        button = ttk.Button(text="Cadastrar" ,command=cadastro)
        button.place(x=x+140, y=y + 200)
        self.mainloop()
main = Main()
main.execute()



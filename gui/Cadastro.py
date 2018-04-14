from persistence.UserDao import *
from persistence.CupDao import *
import datetime
import tkinter
from tkinter import messagebox
from tkinter import ttk

class Cadastro:
    def execute(self):
        cadastro = tkinter.Tk()
        cadastro.title("DrinkWater/Cadastro")
        cadastro.geometry("400x400")
        cadastro.resizable(False, False)
        x = 90
        y = 30
        label =ttk.Label(cadastro,text = "login" ,font=20)
        label.place(x=x,y=y)
        input1 = ttk.Entry(cadastro,width=35)
        input1.place(x=x,y=y+50)
        label = ttk.Label(cadastro,text="senha",font=20)
        label.place(x=x, y=y+100)
        input2 = ttk.Entry(cadastro,width=35 ,show="*")
        input2.place(x=x, y=y+150)
        label = ttk.Label(cadastro,text="Confirmar Senha", font=20)
        label.place(x=x, y=y + 200)
        input3 = ttk.Entry(cadastro,width=35, show="*")
        input3.place(x=x, y=y + 250)
        def cadastrar():
            u = User()
            u.setLogin(input1.get())
            u.setPassword(input2.get())
            if (u.getPassword() == input3.get()):
                UserDao().insert(u)
                messagebox.showinfo("Aviso","usuario cadastrado")
            else:
                messagebox.showinfo("Aviso","erro ao cadastrar")
        button = ttk.Button(cadastro,text="Cadastrar" ,command=cadastrar)
        button.place(x=x,y=y+300)
        cadastro.mainloop()


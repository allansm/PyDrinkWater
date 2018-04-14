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
        cadastro.geometry("400x340")
        cadastro.resizable(False, False)
        x = 90
        y = 30
        label =ttk.Label(cadastro,text = "login" ,font=20)
        label.place(x=x,y=y)
        input1 = ttk.Entry(cadastro,width=35)
        input1.place(x=x,y=y+30)
        label = ttk.Label(cadastro,text="senha",font=20)
        label.place(x=x, y=y+80)
        input2 = ttk.Entry(cadastro,width=35 ,show="*")
        input2.place(x=x, y=y+110)
        label = ttk.Label(cadastro,text="Confirmar Senha", font=20)
        label.place(x=x, y=y + 160)
        input3 = ttk.Entry(cadastro,width=35, show="*")
        input3.place(x=x, y=y + 190)
        def cadastrar():
            u = User()
            u.setLogin(input1.get())
            u.setPassword(input2.get())
            if(u.getLogin() != "" and u.getPassword() != ""):
                if (u.getPassword() == input3.get()):
                    UserDao().insert(u)
                    messagebox.showinfo("Aviso","usuario cadastrado")
                else:
                    messagebox.showinfo("Erro","erro ao cadastrar")
            else:
                messagebox.showinfo("Erro","usuario e senha invalidos")
        button = ttk.Button(cadastro,text="Cadastrar" ,command=cadastrar)
        button.place(x=x,y=y+240)
        cadastro.mainloop()


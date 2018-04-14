from persistence.UserDao import *
from persistence.CupDao import *
import datetime
import tkinter
from tkinter import ttk
class Painel:
    def execute(self,user):
        painel = tkinter.Tk()
        painel.title("DrinkWater/Login/"+user.getLogin())
        painel.geometry("400x300")
        painel.resizable(False, False)
        x = 90
        y = 30
        cups = CupDao().all()
        data = "" + datetime.datetime.now().strftime("%d/%m/%Y")
        copos = 0
        for copo in cups:
            if (copo[2] == user.getId() and copo[3] == data):
                copos += copo[1]
        label1 = ttk.Label(painel, text="Copos hoje:                     "+str(copos), font=20)
        label1.place(x=x, y=y)
        
        
        label2 = ttk.Label(painel, text="Usuario:                        "+user.getLogin(), font=20)
        label2.place(x=x, y=y + 50)
        
       
        label3 = ttk.Label(painel, text="Data:                           "+data, font=20)
        label3.place(x=x, y=y + 100)

        label = ttk.Label(painel, text="Copos:", font=20)
        label.place(x=x, y=y + 150)

        times = ttk.Entry(painel,validate="key",width=5)
        times.place(x=x+70,y=y+150)
        def adicionar():
            if(int(times.get()) >= 1):
                cup = Cup()
                cup.setTimes(times.get())
                cup.setUser_id(user.getId())
                cup.setCupdate(datetime.datetime.now().strftime("%d/%m/%Y"))
                cup.setCupTime(datetime.datetime.now().strftime("%H:%M:%S"))
                CupDao().insert(cup)
                cups = CupDao().all()
                data = "" + datetime.datetime.now().strftime("%d/%m/%Y")
                copos = 0
                for copo in cups:
                    if (copo[2] == user.getId() and copo[3] == data):
                        copos += copo[1]
                label1["text"] = "Copos hoje:                     "+str(copos)
                label3["text"] = "Data:                           "+data
        button = ttk.Button(painel, text="Adicionar", command=adicionar)
        button.place(x=x, y=y + 200)

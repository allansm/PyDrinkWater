from persistence.UserDao import *
from persistence.CupDao import *
import datetime

def test():
    while(True):
        try:
            print("1: login 2: cadastro")
            q = input("escolha:")
            if(q == "1"):
                user = User()
                user.setLogin(input("login:"))
                user.setPassword(input("passoword:"))
                fetch = UserDao().autenticate(user)
                user.setId(fetch[0])
                user.setLogin(fetch[1])
                user.setPassword(fetch[2])
                while(True):
                    cups = CupDao().all()
                    data = ""+datetime.datetime.now().strftime("%d/%m/%Y")
                    copos = 0
                    for copo in cups :
                        if(copo[2] == user.getId() and copo[3] == data):
                            copos += copo[1]
                    print("copos hoje:"+str(copos))
                    print("usuario:"+user.getLogin())
                    print("data:"+data)
                    print("1: Adicionar Copo 2: Sair")
                    q = input("escolha:")
                    if(q == "1"):
                        times = int(input("copos:"))
                        if(times >= 1):
                            cup = Cup()
                            cup.setTimes(times)
                            cup.setUser_id(user.getId())
                            cup.setCupdate(datetime.datetime.now().strftime ("%d/%m/%Y"))
                            cup.setCupTime(datetime.datetime.now().strftime ("%H:%M:%S"))
                            CupDao().insert(cup)
                            print("Copos adicionados")
                        else:
                            print("valor invalido")
                    if(q == "2"):
                        return 0
            if(q == "2"):
                try:
                    user = User()
                    user.setLogin(input("login:"))
                    user.setPassword(input("passoword:"))
                    csenha = input("confirmação de senha")
                    if(user.getPassword() == csenha):
                       UserDao().insert(user)
                       print("usuario cadastrado")
                    else:
                        print("senha invalida")
                except:
                    print("erro : usuario ja existe")
        except:
            print("usuario não encontrado ou erro")
test()


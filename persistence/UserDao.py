from connection.Connection import Connection
from entity.User import User

class UserDao:
    def autenticate(self,user):
        con = Connection.getConnection(self)
        cursor = con.cursor()
        cursor.execute("select * from tbl_users where login=%s and password=md5(%s)",(user.getLogin(),user.getPassword()))
        return cursor.fetchone()
    def insert(self,user):
        con = Connection.getConnection(self)
        cursor = con.cursor()
        cursor.execute("insert into tbl_users(login,password) values(%s,md5(%s))",(user.getLogin(),user.getPassword()))
        con.commit()


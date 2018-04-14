from connection.Connection import Connection
from entity.Cup import Cup

class CupDao:
    def all(self):
        con = Connection().getConnection()
        cursor = con.cursor()
        cursor.execute("select * from tbl_cups")
        return cursor.fetchall()
    def insert(self,cup):
        con = Connection().getConnection()
        cursor = con.cursor()
        cursor.execute("insert into tbl_cups(times,user_id,cupdate,cuptime) values(%s,%s,%s,%s)",(cup.getTimes(),cup.getUser_id(),cup.getCupDate(),cup.getCupTime()))
        con.commit()

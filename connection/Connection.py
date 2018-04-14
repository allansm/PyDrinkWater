import pymysql

class Connection:
    def getConnection(self):
        return pymysql.connect("localhost","root","","drinkwater")
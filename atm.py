import mysql.connector

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    passwd = "",
    database = "myproject"    
)
#print(mydb)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE myproject")
# mycursor.execute("SHOW DATABASES")

# for db in mycursor:
#     print(db)
#mycursor.execute("CREATE TABLE bankusers (name VARCHAR(50), phonenumber INT(11), pin INT(4), amount VARCHAR(100))")
# mycursor.execute("SHOW TABLES")
# for tb in mycursor:
#     print(tb)
sqlFormula = "INSERT INFO bankusers (name, phonenumber, pin, amount) VALUES (%s, %s)"
bankusers = ("omololamuhammed, 08183632046, 1234, 500000")
            

mycursor.executemany(sqlFormula, bankusers)

mydb.commit()


print("welcome to labaks bank")
class mine():
    def __init__(self):
        self.m = "1111"
        self.lolly()
    def lolly(self):
        for i in range(3):

             self.name = input("ur pin")

             if self.name == self.m:
                 print("1. withdrawal \n 2. deposit \n 3. enquiry \n 4. quickteller")
             else:
                    print("incorrect pin")


mine()

def withdrawal():
    one = "1"
    pin = input("select an option")
    if one == pin:
        print("1.20000\n 2.10000\n 3.5000\n 4.1000\n 5.others")
    else:
        print("you have not selected a correct option")

withdrawal()


def deposit():
    one = "2"
    pin = input("select an option")
    if one == pin:
        print("1.labaks bank\n 2.other banks\n 3.others")
    else:
        print("you have not selected a correct option")

deposit()


def enquiry():
    one = "3"
    pin = input("select an option")
    if one == pin:
        print("Ledger balance is 20,165\n Available balance 20,000")
    else:
        print("you have not selected a correct option")

enquiry()



def quickteller():
    one = "4"
    pin = input("select an option")
    if one == pin:
        print("1.transfer\n 2.open an account\n 3.change pin\n 4.use fingerprint banking\n 5.others")
    else:
        print("you have not selected a correct option")

quickteller()
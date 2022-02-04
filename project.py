# from _typeshed import Self


class Reg_db():
    def __init__(self):
        import mysql.connector
        self.database = mysql.connector.connect( host = "127.0.0.1", user = "root", passwd = "", database = "REGISTIRATION")
        self.my_database = self.database.cursor()
        self.my_database.execute("CREATE DATABASE REGISTRATION")
        self.my_database.execute( """ create table student_info (S_N INT AUTO_INCREMENT PRIMARY KEY,
            Fisrt_name varchar(10), middel_name varchar(10), last_name varchar(10), Email varchar(20), phone int(11),
            Username varchar(10), password varchar(10), address varchar(50), pin int(4) )""" )
        self.my_database.execute("alter Table student_into add unique (phone)")
        self.my_database.execute("alter table student_into add unique (username)")
        print("""
                    WELCOME TO YOUR REGISTIRATION PAGE
             please make sure you enter all informations correctly
                                            >>>""")
        self.first_name = input("first name >> ").upper()
        self.middle_name = input("middle Name >>").upper()
        self.last_Name = input("last Name >>").upper()
        self.email = input("email address>>")
        self.phone = int(input("enter your phonenumber >> +234"))
        self.username = input("create a username >>").capitalize()
        self.password = input("create password >>").lower()
        self.address = input("home address >>")
        self.pin = int(input("create your unique pin >>"))
        print("REGISTRATION SUCCESSFULL")
        self.data = """insert into student_info (first_name, Middle_name, Last_name, Email, phone,
                    Username, password, Address, Pin) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,)"""
        self.val = (self.first_name,self.middle_name,self.last_name,self.email,self.phone,self.username,self.password,self.address,self.pin)
        self.my_database.execute(self.data,self.val)
        self.database.commit()

mm = Reg_db()        

# import mysql.connector

# mydb=mysql.connector.connect(
#     host = "127.0.0.1",
#     user = "root",
#     password = "",
#     database = "usmandb"
# )
# # print(mydb)

# mycursor = mydb.cursor()
# # mycursor.execute("CREATE DATABASE usman")
# # mycursor.execute("SHOW DATABASES")
# # for db in mycursor:
# #     print(db)
# # mycursor.execute("CREATE TABLE atm (name VARCHAR(255), pin INTEGER(10), phonenumber INTEGER(20), amout INTEGER(30))")
# # mycursor.execute("SHOW TABLES")
# # for tb in mycursor:
# #     print(tb)
# sqlfomula = "INSENT INTO atm (name, pin, phonenumber, amout) VALUES (%s, %s, %s, %s)"
# user1 = ("ope", 2344, 8035142067, 2000)
# mycursor.execute(sqlfomula, user1)
# mydb.commit()
  
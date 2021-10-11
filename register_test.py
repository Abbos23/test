import os
import platform 
import sys
import mysql.connector

def clear_everything():
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")
    else:
        print("Sorry we do not now this system")

my_db = mysql.connector.connect(
    host="localhost",
    user="abbos",
    password="12345678",
    database="dang"
)
my_cursor = my_db.cursor()
my_cursor.execute("create table if not exists login_passowrd(id int(6) unsigned auto_increment primary key, name varchar(20), surname varchar(20), login varchar(20), password varchar(20))")
my_db.commit()


class Register:
    def __init__(self):
        self.menu()

    def menu(self):
        answer = input("""
What do you want
Please choose one of them
        Sign in [1]
        Log in  [2]
        Exit    [3]   
:""")
        self.choosed(answer)

    def choosed(self, chose):
        if chose == '1':
            clear_everything()
            self.register()
        elif chose == '2':
            clear_everything()
            self.log_in()
        else:
            print("Bye ;)")
            exit()


    def register(self):
        pass
    def log_in(self):
        pass
    def update_password(self):
        pass
    def update_login(self):
        pass
    def delete_account(self):
        pass
    def error(self):
        pass
    def back(self):
        pass



user1 = Register()


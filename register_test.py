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

class Register:
    def __init__(self):
        pass

    def menu(self):
        pass

    def choosed(self):
        pass

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

    


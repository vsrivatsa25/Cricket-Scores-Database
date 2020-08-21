import PySimpleGUI as sg      
import hashlib
import os
import sqlite3
login=sqlite3.connect("admin.db")
c=login.cursor()
def PasswordMatches(password, hash):      
    password_utf = password.encode('utf-8')      
    sha1hash = hashlib.sha1()      
    sha1hash.update(password_utf)      
    password_hash = sha1hash.hexdigest()      
    if password_hash == hash:      
        return True      
    else:
         return False

user,password = [sg.PopupGetText('User'),sg.PopupGetText('Password', password_char='*')]
sqlite_search = """SELECT password from 'Login' where (username = ?);"""
c.execute(sqlite_search, (user,))
login.commit()
record = c.fetchall()[0][0]
c.close()
if PasswordMatches(password, record) and user=='admin':      
    print('Login SUCCESSFUL')
    os.system('menu.py')
elif PasswordMatches(password, record) and user!='admin':      
    print('Login SUCCESSFUL')
    os.system('usermenu.py')

else:      
    print('Login FAILED!!')

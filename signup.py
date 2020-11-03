import PySimpleGUI as sg      
import hashlib
import os
import sqlite3
login=sqlite3.connect("admin.db")
c=login.cursor()
user,password,confirm = sg.PopupGetText('User'),sg.PopupGetText('Password', password_char='*'),sg.PopupGetText('Confirm Password', password_char='*')
sqliteConnection = sqlite3.connect('admin.db')
cursor = sqliteConnection.cursor()
print("Database Connected! Ready to Add Login Details")
password_utf = password.encode('utf-8')      
sha1hash = hashlib.sha1()      
sha1hash.update(password_utf)      
password = sha1hash.hexdigest()
password_utf = confirm.encode('utf-8')      
sha1hash = hashlib.sha1()      
sha1hash.update(password_utf)      
confirm = sha1hash.hexdigest()
sqlite_search = """SELECT username from 'login' where (username = ?);"""
cursor.execute(sqlite_search, (user,))
sqliteConnection.commit()
records = cursor.fetchall()
r=len(records)
if r==0:
    sqlite_insert_with_param = """INSERT INTO 'Login'
                      ('Username', 'Password') 
                      VALUES (?, ?);"""
    data_tuple = (user,password)
    if confirm==password :
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("User successfullly registered. Please login now.")
        cursor.close()
        window.close()
        os.system('start.py')
    else:
        sg.Popup("Passwords do not match. Try Again")
        print("Cancelling: Passwords do not match")
        window.close()
        os.system('signup.py')        
else:
    print("User already exists")

import PySimpleGUI as sg
import sqlite3
import random
import os
def SearchPlayer(pname):
    try:
        sqliteConnection = sqlite3.connect('example.db')
        cursor = sqliteConnection.cursor()
        print("Database Connected! Ready to Search Umpire")

        sqlite_search = """SELECT * from 'Stadium' where (name like ?);"""
        cursor.execute(sqlite_search, (pname,))
        sqliteConnection.commit()
        records = cursor.fetchall()
        print(records)
        sg.Popup("Name: "+records[0][1],"Country: "+records[0][2],"Capacity: "+str(records[0][3]),"Matches Hosted: "+str(records[0][4]))
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to find umpire in sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")
sqliteConnection = sqlite3.connect('example.db')
cursor = sqliteConnection.cursor()
sqlite_search = """SELECT name from 'Stadium';"""
cursor.execute(sqlite_search,)
conn = sqlite3.connect('example.db')
sqliteConnection.commit()
name = cursor.fetchall()
names=[]
for i in name:
    names.append(i[0])
layout = [[sg.Text('Select Stadium')],
          [sg.InputCombo((names), size=(20, 1)),sg.Button('Search')],
          [sg.Button('Main Menu')]]
# Create the Window
window = sg.Window('Search Stadium Details', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    print(values[0])
    if event=='Main Menu':
        window.close()
        os.system('menu.py')
        break
    print('You entered ', values[0])
    SearchPlayer(values[0])
window.close()

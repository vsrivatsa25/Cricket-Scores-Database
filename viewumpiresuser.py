import PySimpleGUI as sg
import sqlite3
import random
import os
def SearchPlayer(pname):
    try:
        sqliteConnection = sqlite3.connect('example.db')
        cursor = sqliteConnection.cursor()
        print("Database Connected! Ready to Search Umpire")

        sqlite_search = """SELECT * from 'Umpires' where (name like ?);"""
        cursor.execute(sqlite_search, (pname,))
        sqliteConnection.commit()
        records = cursor.fetchall()
        print(records)
        sg.Popup("Name: ",records[0][0],"Matches ",records[0][2])               
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to find umpire in sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")
sqliteConnection = sqlite3.connect('example.db')
cursor = sqliteConnection.cursor()
sqlite_search = """SELECT name from 'umpires';"""
cursor.execute(sqlite_search,)
sqliteConnection.commit()
teams = cursor.fetchall()
layout = [[sg.Text('Select Umpire')],
          [sg.InputCombo(teams, size=(20, 1)),sg.Button('Search')],          
          [sg.Button('Main Menu')]]
# Create the Window
window = sg.Window('Search Umpire Details', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    print(values[0])
    if event=='Main Menu':
        window.close()
        os.system('usermenu.py')        
        break
    print('You entered ', values[0][0])
    SearchPlayer(values[0][0])    
window.close()

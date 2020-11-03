import PySimpleGUI as sg
import sqlite3
import random
import os


def insertVaribleIntoTable(vals):
    try:
        sqliteConnection = sqlite3.connect('example.db')
        cursor = sqliteConnection.cursor()
        print("Database Connected! Ready to Add Player")

        sqlite_insert_with_param = """INSERT INTO 'teams'
                          ('name','team_id') 
                          VALUES (?, ?);"""

        data_tuple = (vals[0],vals[1])
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Team details inserted successfully into table")
        cursor.close()

    except sqlite3.Error as error:
        sg.Popup(error)
        cursor.close()
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")
temp=random.randint(100000,999999)
layout = [  [sg.Text('Name'), sg.InputText()],
            [sg.Text('Team ID'), sg.Text(temp,key="ID")],
            [sg.Button('Add Team'),sg.Button('Main Menu')]]

# Create the Window
window = sg.Window('ADD TEAM', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    values[1]=temp
    temp=random.randint(100000,999999)
    #window['ID'].Update(values['temp'])
    window.Element('ID').Update(temp)
    if event=='Main Menu':
        window.close()
        os.system('menu.py')        
        break
    print('You entered ', values[0])    
    insertVaribleIntoTable(values)
window.close()



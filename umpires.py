import PySimpleGUI as sg
import sqlite3
import random
import os

def insertVaribleIntoTable(vals):
    try:
        sqliteConnection = sqlite3.connect('example.db')
        cursor = sqliteConnection.cursor()
        print("Database Connected! Ready to Add Umpire")

        sqlite_insert_with_param = """INSERT INTO 'Umpires'
                          ('Name','Matches','U_ID') 
                          VALUES (?, ?,?);"""

        data_tuple = (vals[0],vals[1],vals[2])
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Umpire details inserted successfully into table")
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
            [sg.Text('Umpire ID'), sg.Text(temp,key="ID")],
            [sg.Text('Matches'), sg.InputText()],
            [sg.Button('Add Umpire'),sg.Button('Main Menu')]]

# Create the Window
window = sg.Window('Add Umpire', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    values[2]=temp
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



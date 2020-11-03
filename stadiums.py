import PySimpleGUI as sg
import sqlite3
import random
import os

def insertVaribleIntoTable(vals):
    try:
        sqliteConnection = sqlite3.connect('example.db')
        cursor = sqliteConnection.cursor()
        print("Database Connected! Ready to Add Stadium")

        sqlite_insert_with_param = """INSERT INTO 'Stadium'
                          ('Std_ID','Name','Country','Capacity','Matches_Hosted') 
                          VALUES (?, ?,?,?,?);"""

        data_tuple = (vals[4],vals[0],vals[1],vals[2],vals[3])
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
            [sg.Text('Std ID'), sg.Text(temp,key="ID")],
            [sg.Text('Country'), sg.InputText()],
            [sg.Text('Capacity'), sg.InputText()],
            [sg.Text('Matches Hosted'), sg.InputText()],
            [sg.Button('Add Stadium'),sg.Button('Main Menu')]]

# Create the Window
window = sg.Window('Add Stadium', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    values[4]=temp
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
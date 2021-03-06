import PySimpleGUI as sg
import sqlite3
import random
import os


def insertVaribleIntoTable(vals):
    try:
        sqliteConnection = sqlite3.connect('example.db')
        cursor = sqliteConnection.cursor()
        print("Database Connected! Ready to Add Player")

        sqlite_insert_with_param = """INSERT INTO 'players'
                          ('name', 'country', 'Matches_Played','INNINGS', 'runs', 'balls_faced', 'fours', 'sixes', 'balls_bowled', 'wickets', 'runs_given', 'catches', 'player_id') 
                          VALUES (?, ?, ?, ?,?,?,?,?,?,?,?,?,?);"""

        data_tuple = (vals[0],vals[1],vals[2],vals[3],vals[4],vals[5],vals[6],vals[7],vals[8],vals[9],vals[10],vals[11],vals[12])
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Player details inserted successfully into table")
        cursor.close()

    except sqlite3.Error as error:
        sg.Popup(error)
        cursor.close()
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("An error occured the SQLite connection is closed")
temp=random.randint(100000,999999)
layout = [  [sg.Text('Name'), sg.InputText()],
            [sg.Text('Country'), sg.InputText()],
            [sg.Text('Matches Played'), sg.InputText()],
            [sg.Text('Innings'), sg.InputText()],
            [sg.Text('Runs'), sg.InputText()],
            [sg.Text('Balls Faced'), sg.InputText()],
            [sg.Text('Fours'), sg.InputText()],
            [sg.Text('Sixes'), sg.InputText()],
            [sg.Text('Balls Bowled'), sg.InputText()],
            [sg.Text('Wickets'), sg.InputText()],
            [sg.Text('Runs Given'), sg.InputText()],
            [sg.Text('Catches'), sg.InputText()],
            [sg.Text('Player ID'), sg.Text(temp,key="ID")],
            [sg.Button('Add Player'),sg.Button('Main Menu')]]

# Create the Window
window = sg.Window('Add Player', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    values[12]=temp
    temp=random.randint(100000,999999)
    #window['ID'].Update(values['temp'])
    window.Element('ID').Update(temp)
    print(values)
    if event=='Main Menu':
        window.close()
        os.system('menu.py')        
        break
    print('You entered ', values[0])
    insertVaribleIntoTable(values)
    
window.close()



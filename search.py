import PySimpleGUI as sg
import sqlite3
import random
import os

login=sqlite3.connect("example.db")
c=login.cursor()

def SearchPlayer(pname):
    try:
        sqliteConnection = sqlite3.connect('example.db')
        cursor = sqliteConnection.cursor()
        print("Database Connected! Ready to Search Player")

        sqlite_search = """SELECT * from 'players' where (name like ?);"""
        cursor.execute(sqlite_search, (pname,))
        sqliteConnection.commit()
        records = cursor.fetchall()
        
        #print(records)
        if len(records)>0:
            if records[0][2]!=0:
                avg=round(records[0][4]/records[0][3],4)
            else:
                avg="NaN"
            if records[0][4]!=0:
                sr=round(records[0][4]*100/records[0][5],4)
            else:
                sr="NaN"
            sg.Popup("Name: "+records[0][0],"Country: "+records[0][1],"Matches Played: "+str(records[0][2]),"Innings: "+str(records[0][3]),
                     "Runs Scored: "+str(records[0][4]),"Average: "+str(avg),"Strike Rate: "+str(sr),"Balls Faced: "+str(records[0][5]),"Fours: "+
                     str(records[0][6]),"Sixes: "+str(records[0][7]),"High Score"+str(records[0][8]),
                     "Balls Bowled: "+str(records[0][9]),"Wickets: "+str(records[0][10]),"Runs Given: "+str(records[0][11]),
                     "Catches:"+str(records[0][12])
                     )
        else:
            sg.Popup("Player not found")
        cursor.close()
        

    except sqlite3.Error as error:
        print("Failed to find player in sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

layout = [[sg.Text('Enter Player Name')],
          [sg.InputText(),sg.Button('Search')],
          
          [sg.Button('Main Menu')]]
# Create the Window
window = sg.Window('Search Player Details', layout)
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



import PySimpleGUI as sg
import sqlite3
import random
import os
login=sqlite3.connect("example.db")
l=login.cursor()
sqliteConnection = sqlite3.connect('example.db')
cursor = sqliteConnection.cursor()
sqlite_search = """SELECT name from 'teams';"""
cursor.execute(sqlite_search,)
sqliteConnection.commit()
ts = cursor.fetchall()
teams=[]
for i in ts:
    teams.append(i[0])
sqlite_search = """SELECT name from 'umpires';"""
cursor.execute(sqlite_search,)
sqliteConnection.commit()
umps = cursor.fetchall()
umpires=[]
for i in umps:
    umpires.append(i[0])
sqlite_search = """SELECT name from 'stadium';"""
cursor.execute(sqlite_search,)
sqliteConnection.commit()
stad = cursor.fetchall()
stadium=[]
for i in stad:
    stadium.append(i[0])
cursor.close()
def insertVaribleIntoTable(vals):
    try:
        sqliteConnection = sqlite3.connect('example.db')
        cursor = sqliteConnection.cursor()
        print("Database Connected! Ready to Add Match")

        sqlite_insert_with_param = """INSERT INTO 'Matches'
                          ('Date','Match_ID','Team1','Team2','Umpire','Stadium') 
                          VALUES (?, ?,?,?,?,?);"""
        data_tuple = (vals[4],vals[5],vals[0],vals[1],vals[2],vals[3])
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Umpire details inserted successfully into table")
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")
temp=random.randint(100000,999999)
layout = [  [sg.Text('Select the two teams playing the match')],
            [sg.InputCombo((teams), size=(20, 1)),sg.InputCombo((teams), size=(20, 1))],
            [sg.Text('Match ID'), sg.Text(temp,key="ID")],
            [sg.Text('Select the umpires in charge')],
            [sg.InputCombo((umpires), size=(20, 1))],
            [sg.Text('Select the Venue')],
            [sg.InputCombo((stadium), size=(20, 1))],
            [sg.Text('Date'),sg.Input('dd-mm-yyyy')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
     
window = sg.Window('Add Match', layout, default_element_size=(40, 1), grab_anywhere=False)

event, values = window.Read()
if event=='Cancel':
    window.close()
    os.system('menu.py')
values[5]=temp
insertVaribleIntoTable(values)
sqliteConnection = sqlite3.connect('example.db')
cursor = sqliteConnection.cursor()
sqlite_search = """UPDATE 'umpires' set matches=matches+1 where name=?;"""
cursor.execute(sqlite_search,(values[2],))
sqliteConnection.commit()
sqlite_search = """UPDATE 'stadium' set Matches_Hosted=Matches_Hosted+1 where name=?;"""
cursor.execute(sqlite_search,(values[3],))
sqliteConnection.commit()
cursor.close()
print(values)
if event=='Ok':
    window.close()
    os.system('matchdetails.py')



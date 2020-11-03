import PySimpleGUI as sg
import sqlite3
import random
import os


sqliteConnection = sqlite3.connect('example.db')
cursor = sqliteConnection.cursor()
sqlite_search = """SELECT name from 'teams';"""
cursor.execute(sqlite_search,)
sqliteConnection.commit()
ts = cursor.fetchall()
teams=[]
for i in ts:
    teams.append(i[0])
layout = [  [sg.Text('Select a team')],
            [sg.InputCombo((teams), size=(30, 1))],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
     
window = sg.Window('View Team', layout, default_element_size=(40, 1), grab_anywhere=False)

event, values = window.Read()
if event=='Cancel':
    window.close()
    os.system('menu.py')
team=values[0]
window.close()
sqlite_search = """SELECT matches,wins,losses from 'teams' where name=?;"""
cursor.execute(sqlite_search,(team,))
sqliteConnection.commit()
teamdets = cursor.fetchall()
sqlite_search = """SELECT * from 'players' where country=?;"""
cursor.execute(sqlite_search,(team,))
sqliteConnection.commit()
teams = cursor.fetchall()
team='Matches: '+str(teamdets[0][0])+"\n"
team=team+'Wins: '+str(teamdets[0][1])+"\n"
team=team+'Losses: '+str(teamdets[0][2])+"\n"
team=team+'Players: \n'
for i in range(len(teams)):
    team=team+str(i+1)
    team=team+"."
    team=team+teams[i][0]
    team=team+"\n"
teamname=values[0]+" team"
if event=='Ok':
    sg.Popup(teamname,team)
    window.close()
    os.system('viewteams.py')
cursor.close()



import PySimpleGUI as sg
import sqlite3
import random
import os
login=sqlite3.connect("example.db")
l=login.cursor()
sqliteConnection = sqlite3.connect('example.db')
cursor = sqliteConnection.cursor()
sqliteConnection = sqlite3.connect('example.db')
cursor = sqliteConnection.cursor()
sqlite_search = """SELECT name from 'teams';"""
cursor.execute(sqlite_search,)
sqliteConnection.commit()
ts = cursor.fetchall()
teams=[]
for i in ts:
    teams.append(i[0])
layout = [  [sg.Text('Select the two teams playing the match')],
            [sg.InputCombo((teams), size=(20, 1)),sg.InputCombo((teams), size=(20, 1))],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
     
window = sg.Window('Add Match', layout, default_element_size=(40, 1), grab_anywhere=False)

event, values = window.Read()
if event=='Ok':
    sqlite_search = """SELECT Team1,Team2,team1score,team1wickets,team2score,team2wickets,date,winner from 'matches' where live=0 and team1=? and team2=?;"""
    data=(values[0],values[1])
    cursor.execute(sqlite_search,data)
    sqliteConnection.commit()
    matchdets = cursor.fetchall()
    if len(matchdets)>0:
        matchdets=matchdets[0]
        team1=matchdets[0]
        team2=matchdets[1]
        txt=team1+' vs ' + team2+' on '+str(matchdets[6])
        score1=str(matchdets[0])+':'+str(matchdets[2])+'/'+str(matchdets[3])
        score2=str(matchdets[1])+':'+str(matchdets[4])+'/'+str(matchdets[5])
        winner='Winner:'+str(matchdets[-1])
        sg.Popup(txt,score1,      score2,winner)
    else:
        sg.Popup('No Matches Found')
    if event=='Ok':
        os.system('usermenu.py')
else:
    os.system('usermenu.py')

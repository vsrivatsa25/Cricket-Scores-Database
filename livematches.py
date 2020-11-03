import PySimpleGUI as sg
import sqlite3
import random
import os
login=sqlite3.connect("example.db")
l=login.cursor()
sqliteConnection = sqlite3.connect('example.db')
cursor = sqliteConnection.cursor()
sqlite_search = """SELECT Team1,Team2,team1score,team1wickets,team2score,team2wickets,date from 'matches' where live=1;"""
cursor.execute(sqlite_search,)
sqliteConnection.commit()
matchdets = cursor.fetchall()[0]
print(matchdets)
team1=matchdets[0]
team2=matchdets[1]
txt=team1+' vs ' + team2+' on '+str(matchdets[6])
score1=str(matchdets[0])+':'+str(matchdets[2])+'/'+str(matchdets[3])
score2=str(matchdets[1])+':'+str(matchdets[4])+'/'+str(matchdets[5])
layout = [[sg.Text(txt, auto_size_text=True)],
          [sg.Text(score1, auto_size_text=True)],
          [sg.Text(score2, auto_size_text=True)],
          [sg.Button('Main Menu'),sg.Button('Refresh'),sg.Quit()]]
window = sg.Window('Live details', layout)
event, value = window.Read()
if event=='Main Menu':
    window.close()
    os.system('usermenu.py')
if event=='Refresh':
    window.close()
    os.system('livematches.py')

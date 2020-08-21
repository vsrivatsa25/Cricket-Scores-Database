import PySimpleGUI as sg
import sqlite3
import random
import os

sqliteConnection = sqlite3.connect('example.db')
cursor = sqliteConnection.cursor()
sqlite_search = """SELECT Match_ID,date from 'matches' where live=1;"""
cursor.execute(sqlite_search,)
sqliteConnection.commit()
matchdets = cursor.fetchall()[0]
match=matchdets[0]
date=matchdets[1]
sqliteConnection = sqlite3.connect('example.db')
cursor = sqliteConnection.cursor()
sqlite_search = """SELECT team1,team2 from 'matches' where (live=1 and Match_ID=?);"""
cursor.execute(sqlite_search,(match,))
sqliteConnection.commit()
teams = cursor.fetchall()[0]
team1=teams[0]
team2=teams[1]
sqliteConnection = sqlite3.connect('example.db')
cursor = sqliteConnection.cursor()
sqlite_search = """SELECT name from 'players' where (country=?);"""
cursor.execute(sqlite_search,(team1,))
sqliteConnection.commit()
p1 = cursor.fetchall()
sqlite_search = """SELECT name from 'players' where (country=?);"""
cursor.execute(sqlite_search,(team2,))
sqliteConnection.commit()
p2 = cursor.fetchall()
players2=[]
for i in p2:
    players2.append(i[0])
players1=[]
for i in p1:
    players1.append(i[0])
print(players1,players2)
#print(teams)
sqliteConnection = sqlite3.connect('example.db')
cursor = sqliteConnection.cursor()
sqlite_search = """SELECT team1score from 'matches' where live=1 and team1=?;"""
cursor.execute(sqlite_search,(team1,))
sqliteConnection.commit()
targt=cursor.fetchall()[0][0]

top=[sg.Text(str("Match ID:"+str(match))),sg.Text(str("Date:"+str(date))),sg.Text('Second Innings Details:'),sg.Text(("Target: ")+str(int(targt)+1))]
bottom=[sg.Text('Bowling Details:'),sg.Text(str(team1)+" bowling second")]
player=['']*21
line=[sg.Text("-"*150)]
player[12]=line
player[13]=bottom
player[0]=top
#print(player)
for i in range(1,12):
    player[i] = [sg.Text(i,size=(2,1)),sg.Text('Name'), sg.InputCombo((players2), size=(10, 1)),
                sg.Text('Runs'), sg.InputText(size=(3,1),default_text='0'),
                sg.Text('Balls Faced'), sg.InputText(size=(3,1),default_text='0'),
                sg.Text('Fours'), sg.InputText(size=(2,1),default_text='0'),
                sg.Text('Sixes'), sg.InputText(size=(2,1),default_text='0'),sg.Checkbox('Out', size=(2,1))]
for i in range(14,20):
    player[i] = [sg.Text(i-13,size=(2,1)),sg.Text('Name'), sg.InputCombo((players1), size=(10, 1)),
                sg.Text('Balls Bowled'), sg.InputText(size=(3,1),default_text='0'),
                sg.Text('Runs'), sg.InputText(size=(3,1),default_text='0'),
                sg.Text('Wickets'), sg.InputText(size=(2,1),default_text='0')]
#print(player)
player[20]=[sg.Button('Save'),sg.Button('Main Menu')]
# Create the Window
window = sg.Window('Match Details',player)
event, values = window.Read()
totalscore=0
wickets=0
print(values)
for i in range(11):
    totalscore+=int(values[6*i+1])
    sqlite_search = """UPDATE 'players' set Runs=Runs+? where name=?;"""
    data_tuple = (int(values[6*i+1]),values[6*i])
    cursor.execute(sqlite_search,data_tuple)
    sqliteConnection.commit()
    sqlite_search = """UPDATE 'players' set balls_faced=balls_faced+? where name=?;"""
    data_tuple = (int(values[6*i+2]),values[6*i])
    cursor.execute(sqlite_search,data_tuple)
    sqliteConnection.commit()
    sqlite_search = """UPDATE 'players' set fours=fours+? where name=?;"""
    data_tuple = (int(values[6*i+3]),values[6*i])
    cursor.execute(sqlite_search,data_tuple)
    sqliteConnection.commit()
    sqlite_search = """UPDATE 'players' set sixes=sixes+? where name=?;"""
    data_tuple = (int(values[6*i+4]),values[6*i])
    cursor.execute(sqlite_search,data_tuple)
    sqliteConnection.commit()
    sqlite_search = """UPDATE 'players' set high_score=? where name=? and runs>high_score;"""
    data_tuple = (int(values[6*i+1]),values[6*i])
    cursor.execute(sqlite_search,data_tuple)    
    sqliteConnection.commit()
    sqlite_search = """UPDATE 'matches' set team2score=? where team2=?;"""
    data_tuple = (totalscore,team2)
    cursor.execute(sqlite_search,data_tuple)
    sqliteConnection.commit()
    sqlite_search = """UPDATE 'matches' set team2wickets=team2wickets+1 where ?='True';"""
    data_tuple = (str(values[6*i+5]),)
    cursor.execute(sqlite_search,data_tuple)
    sqliteConnection.commit()
    sqlite_search = """UPDATE 'players' set innings=innings+1 where name=? and ?='True';"""
    data_tuple = (values[6*i][0],str(values[6*i+5]))
    cursor.execute(sqlite_search,data_tuple)
    sqliteConnection.commit()
print(players1,players2)
for i in range(5):
    sqlite_search = """UPDATE 'players' set balls_bowled=balls_bowled+? where name=?;"""
    data_tuple = (int(values[66+4*i+1]),str(values[66+4*i]))
    cursor.execute(sqlite_search,data_tuple)
    sqliteConnection.commit()
    sqlite_search = """UPDATE 'players' set runs_given=runs_given+? where name=?;"""
    data_tuple = (int(values[66+4*i+2]),str(values[66+4*i]))
    cursor.execute(sqlite_search,data_tuple)
    sqliteConnection.commit()
    sqlite_search = """UPDATE 'players' set wickets=wickets+? where name=?;"""
    data_tuple = (int(values[66+4*i+3]),str(values[66+4*i]))
    cursor.execute(sqlite_search,data_tuple)
    sqliteConnection.commit()

if totalscore>targt-1:
    sg.Popup('Match Details Added. '+team2+' wins');
    sqlite_search = """UPDATE 'matches' set winner=? where live=1;"""
    data_tuple = (team2)
    cursor.execute(sqlite_search,data_tuple)
    sqliteConnection.commit()
elif totalscore==targt-1:
    sg.Popup('Match Details Added. Its a tie');
    sqlite_search = """UPDATE 'matches' set winner=? where live=1;"""
    data_tuple = ('tie')
    cursor.execute(sqlite_search,data_tuple)
    sqliteConnection.commit()
else:
    sg.Popup('Match Details Added. '+team1+' wins');
    sqlite_search = """UPDATE 'matches' set winner=? where live=1;"""
    data_tuple = (team1)
    cursor.execute(sqlite_search,data_tuple)
    sqliteConnection.commit()
sqlite_search = """UPDATE 'matches' set live=0 where live=1;"""
cursor.execute(sqlite_search)
sqliteConnection.commit()
os.system('menu.py')




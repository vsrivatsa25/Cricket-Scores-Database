import PySimpleGUI as sg
import os
import sqlite3

def button1():
    sqliteConnection = sqlite3.connect('example.db')
    cursor = sqliteConnection.cursor()
    sqlite_search = """SELECT Team1,Team2,team1score,team1wickets,team2score,team2wickets,date from 'matches' where live=1;"""
    cursor.execute(sqlite_search, )
    sqliteConnection.commit()
    if cursor.fetchall():
        os.system('livematches.py')
    else:
        sg.Popup("No live match")
        cursor.close()
        os.system('usermenu.py')

def button3():    
    os.system('oldmatches.py')
    
def button4():
    os.system('searchuser.py')

def button5():
    os.system('viewteamsuser.py')
    
func_dict = {'View Live Matches':button1,'View Old Matches':button3,'Search Player Details':button4,'View Teams':button5 }
layout = [[sg.Text('Please choose an option', auto_size_text=True)],
          [sg.Button('View Live Matches')],
          [sg.Button('View Old Matches')],
          [sg.Button('Search Player Details'), sg.Button('View Teams'), sg.Quit()]]
window = sg.Window('Cricket Statistics', layout)
event, value = window.Read()
window.Close()
try:
    func_to_call = func_dict[event]
    func_to_call()                    
except:
    pass


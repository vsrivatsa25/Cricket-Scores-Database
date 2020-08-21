import PySimpleGUI as sg
import os

def button1():    
    os.system('matches.py')

def button2():
    os.system('players.py')

def button3():
    os.system('teams.py')
    
def button4():
    os.system('search.py')

def button8():
    os.system('umpires.py')

def button5():
    os.system('viewteams.py')
    
def button6():
    os.system('start.py')
    
def button7():
    os.system('viewumpires.py')
    
func_dict = {'Add Match':button1,'Add Umpire':button8, 'Add Player':button2,'Add Teams':button3,'Search Player Details':button4,'View Teams':button5
             ,'Logout':button6, 'View Umpires':button7 }
layout = [[sg.Text('Please choose an option', auto_size_text=True)],
          [sg.Button('Add Match'), sg.Button('Add Player'), sg.Button('Add Teams'),sg.Button('Add Umpire')],
          [sg.Button('Search Player Details'), sg.Button('View Teams'),sg.Button('View Umpires')],
          [sg.Button('Logout'),sg.Quit()]]
window = sg.Window('Cricket Statistics', layout)
event, value = window.Read()
window.Close()
try:
    func_to_call = func_dict[event]
    func_to_call()                    
except:
    pass


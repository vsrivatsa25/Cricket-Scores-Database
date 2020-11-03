import PySimpleGUI as sg
import os

def button1():
    os.system('login.py')

def button2():
    os.system('start.py')
func_dict = {'Admin':button1, 'Spectator':button2 }
layout = [[sg.Text('Please choose an option', size=(30,1))],
[sg.Button('Admin',size=(8,1)), sg.Button('Spectator',size=(8,1))]]
window = sg.Window('Welcome to Cricket Database', layout)
event, value = window.Read()
window.Close()
try:
    func_to_call = func_dict[event]
    func_to_call()
except:
    pass
import PySimpleGUI as sg
import os

def button1():    
    os.system('login.py')

def button2():
    os.system('signup.py')
func_dict = {'Login':button1, 'Sign Up':button2 }
layout = [[sg.Text('Please choose an option', size=(30,1))],
[sg.Button('Login',size=(8,1)), sg.Button('Sign Up',size=(8,1))]]
window = sg.Window('Cricket Statistics', layout)
event, value = window.Read()
window.Close()
try:
    func_to_call = func_dict[event]
    func_to_call()                    
except:
    pass

import PySimpleGUI as sg
# from dice import Dice as d
from random import randint 



def d(die):
    return randint(1,die)

sg.theme('DarkTeal4')
roll="-"

layout=[
            [sg.Text("Roll:"),sg.Text(roll,k='-RESULT-')],
            [
                sg.Button("D6",k='-D6-'),
                sg.Button("D10",k='-D10-'),
                sg.Button("D20",k='-D20-')
            ]
        ]
window = sg.Window('DICE ROLLER').Layout(layout)

while True:
        event, values = window.Read()
        if event == sg.WIN_CLOSED or event == 'Close':
                break 
        if event == '-D6-':
                roll=d(6)
                window['-RESULT-'].update(roll)
                print(roll)
        if event == '-D10-':
                roll=d(10)
                window['-RESULT-'].update(roll)
        if event == '-D20-':
                roll=d(20)
                window['-RESULT-'].update(roll)
window.close()
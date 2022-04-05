import PySimpleGUI as sg
from dice import Dice

sg.theme('DarkTeal4')
roll="-"

layout=[
        [sg.Text("Roll:"),sg.Text(roll,k='-RESULT-')],
        [sg.Button("D6",k='-ROLL-')]
        ]
window = sg.Window('DICE ROLLER').Layout(layout)

while True:
        event, values = window.Read()
        if event == sg.WIN_CLOSED or event == 'Close':
                break 
        if event == '-ROLL-':
                roll=Dice.D6()
                window['-RESULT-'].update(roll)
window.close()
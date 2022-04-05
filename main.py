import PySimpleGUI as sg
from random import randint 


#basic dice roller function
def d(die):
    return randint(1,die)


#gui
sg.theme('DarkTeal4')
roll="-"
total=0
add= False

layout=[
            [sg.Text("Roll:"),sg.Text(roll,k='-RESULT-')],
            [sg.Text("Total:"),sg.Text(total,k='-TOTAL-')],
            [
                sg.Button("D6",k='-D6-'),
                sg.Button("D10",k='-D10-'),
                sg.Button("D20",k='-D20-')
            ],
            [sg.Button("+",k="-ADD-", button_color=('white','gray')), sg.Text("add?: ",add)]
        ]
window = sg.Window('DICE ROLLER').Layout(layout)

#loop
while True:
        event, values = window.Read()
        if event == sg.WIN_CLOSED or event == 'Close':
                break 
            
        if event == '-ADD-':
            if add == False:
                add = True
                window.FindElement('-ADD-').Update(button_color=('white', 'green'))
                print(add)
            else: 
                add = False
                window.FindElement('-ADD-').Update(button_color=('white', 'gray'))
                print(add)
                
        if event == '-D6-':
                roll=d(6)
                total += roll
                
                print(roll)
                
        if event == '-D10-':
                roll=d(10)
                total += roll

                
        if event == '-D20-':
                roll=d(20)
                total += roll
                
        if add == False:
            total = 0
        window['-RESULT-'].update(roll)
        window['-TOTAL-'].update(total)

window.close()
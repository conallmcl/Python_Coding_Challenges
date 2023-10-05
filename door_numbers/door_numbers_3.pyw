import PySimpleGUI as sg

def doorNumbers(start, end, problem_numbers):
    count = 0
    for number in range(start, end + 1):
        for char in str(number):
            if char in problem_numbers:
                count += 1
    return count

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Please input start value of range: '), sg.InputText(key = 'start_range')],
            [sg.Text('Please input end value of range: '), sg.InputText(key = 'end_range')],
            [sg.Text('Please enter the problem number: '), sg.InputText(key = 'problem_numbers')],
            [sg.Text('Result: '), sg.Text(key = 'count')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Manufacturing Issues Console', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == 'Ok':
        start_range = int(values['start_range'])
        end_range = int(values['end_range'])
        problem_numbers = values['problem_numbers'].replace(" ", "").split(",")
        count = doorNumbers(start_range, end_range, problem_numbers)
        window['count'].update(value=count)
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

window.close()
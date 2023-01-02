
'''
Example of (almost) all widgets, that you can use in PySimpleGUI.
'''

import PySimpleGUI as sg

sg.change_look_and_feel('GreenTan')

# ------ Menu Definition ------ #
menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Help', '&About...'], ]

# ------ Column Definition ------ #
column1 = [[sg.Text('Column 1', background_color='lightblue', justification='center', size=(10, 1))],
           [sg.Spin(values=('Spin Box 1', '2', '3'),
                    initial_value='Spin Box 1')],
           [sg.Spin(values=('Spin Box 1', '2', '3'),
                    initial_value='Spin Box 2')],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('NetEye Tool', size=(
        30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE) ],
    [sg.Text('Enter IP or URL to perform enumeration:')],
    [sg.InputText('')],
    [sg.Frame(layout=[
        [sg.CBox('Scan FTP server', size=(15, 1)),
         sg.CBox('Scan HTTP server', default=True)],
        [sg.Radio('Use VirusTotal API     ', "RADIO1", default=True, size=(10, 1)),
         sg.Radio('Use abuseIP API', "RADIO1")]], title='Options',
             title_color='red',
             relief=sg.RELIEF_SUNKEN,
             tooltip='Use these to set flags')],
    [sg.MLine(default_text='Port Scan Started At :', size=(35, 3)),
     sg.MLine(default_text='Scan Report For 10.10.176.76', size=(35, 3))],
    
    [sg.OptionMenu(('Select Yes or No', 'Yes', 'No'))],
    
    [sg.Text('_' * 80)],
    [sg.Text('Choose A File to Scan', size=(35, 1))],
    [sg.Text('Your Folder', size=(15, 1), justification='right'),
     sg.InputText('Default Folder'), sg.FolderBrowse()],
    [sg.Submit(tooltip='Click to submit this form'), sg.Cancel()]]

window = sg.Window('Neteye GUI', layout,
    default_element_size=(40, 1), grab_anywhere=False)

event, values = window.read()
sg.popup('Title',
         'The results of the window.',
         'The button clicked was "{}"'.format(event),
         'The values are', values)
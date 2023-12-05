import PySimpleGUI as sg
from core.states import VendState
from core.states import IdleState
from core.transitions import StateTransition

def main_gui(vending_machine):
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 480

    layout = [
        [sg.Text('Make Selection', font=('Helvetica', 20))],
        [sg.Button('', image_filename='gui/9oz_honey_jar.png', border_width=0, key='9oz', image_size=(134, 198))],
        [sg.Button('Exit')]
    ]

    window = sg.Window('Honey Vendor', layout, no_titlebar=True, keep_on_top=True, finalize=True)
    window.Size = (SCREEN_WIDTH, SCREEN_HEIGHT)

    while True:
        event, values = window.read()

        if event == '9oz':
            vending_machine.purchase_item(item='9 oz', quantity=1)
        elif event == sg.WIN_CLOSED or event == 'Exit':
            break

    window.close()

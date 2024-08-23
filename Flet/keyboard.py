import flet as ft
from flet import Page, Row, Text, KeyboardEvent

def main(page: Page) ->None:
    page.title = 'Keyboard Pro'
    page.spacing = 30
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.theme_mode = 'dark'
    
    
    key: Text = Text('Key', size= 30)
    shift: Text = Text('Shift', size= 30, color = 'red')
    ctrl: Text = Text('Ctrl', size= 30, color = 'blue')
    alt: Text = Text('Alt', size= 30, color = 'green')
    
    def on_keyboard(e:KeyboardEvent) -> None:
        key.value = e.key
        shift.visible = e.shift
        ctrl.visible = e.ctrl
        alt.visible = e.alt
        print(e.data)
        page.update()
    
    page.on_keyboard_event = on_keyboard
     
    page.add(
        Text('Press any combinations of keys'),
        Row(controls = [key, shift, ctrl, alt],
            alignment= ft.MainAxisAlignment.CENTER)
    )
    
if __name__ == '__main__' :
    ft.app(target=main)
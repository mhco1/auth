from textual.screen import Screen
from textual.containers import Vertical, Horizontal
from textual.widgets import Button, Tree, Static, Log

class S_remove_pass(Screen):
    def __init__(self, screen_uuid):
        super().__init__()
        self.screen_uuid = screen_uuid

    def compose(self):
        yield Static(f'You would like remove this pass "{self.app.user["pass"]}"')
        yield Horizontal(
            Button('yes','success', id='y'),
            Button('no','error', id='n'),
        )

    def on_button_pressed(self, event):
        op = event.button.id
        
        if op == 'y':
            id = self.app.user['id']
            psw = self.app.user['pass']
            self.app.cmd(f"pass rm '{id}' '{psw}'")
            self.app.goto('home')
            return
        
        if op == 'n':
            self.app.goto('back')
            return
        return
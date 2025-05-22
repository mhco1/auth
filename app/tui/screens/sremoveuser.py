from textual.screen import Screen
from textual.containers import Vertical, Horizontal
from textual.widgets import Button, Tree, Static, Log

class S_remove_user(Screen):
    def __init__(self, screen_uuid):
        super().__init__()
        self.screen_uuid = screen_uuid

    def compose(self):
        yield Static(f'You would like remove this user "{self.app.user["name"]}"')
        yield Horizontal(
            Button('yes','success', id='y'),
            Button('no','error', id='n'),
        )

    def on_button_pressed(self, event):
        op = event.button.id
        
        if op == 'y':
            self.app.cmd(f"user rm '{self.app.user['id']}'")
            self.app.user = {
                "name": '',
                "id": '',
                "pass": '',
                "tag": '',
            }
            self.app.goto('home')
            return
        
        if op == 'n':
            self.app.goto('back')
            return
        return
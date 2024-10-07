from textual.screen import Screen
from textual.containers import Vertical, Horizontal
from textual.widgets import Static, Input, Button, Collapsible, Checkbox

from utils import serialize

class S_creat_auth(Screen):
    def __init__(self, screen_uuid):
        super().__init__()
        self.screen_uuid = screen_uuid
        self.token = Input(password=True)

    def compose(self):
        yield Static('Token:')
        yield Horizontal(
            self.token,
            Button('show/hidden'),
        )
        yield Horizontal(
            Button('edit','success'),
            Button('exit','error')
        )
    
    def on_button_pressed(self, event):
        op = event.button.label.plain

        if op == 'show/hidden':
            self.token.password = not self.token.password
        if op == 'edit':
            profile = self.app.getSelect()
            token = serialize(self.token.value.replace(" ",""))
            self.app.cmd(f'set-auth {profile} "{token}"')
            self.app.goHomeScreen()
        if op == 'exit':
            self.app.goHomeScreen()

        return
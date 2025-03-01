import pyperclip

from textual.screen import Screen
from textual.containers import Vertical, Horizontal
from textual.widgets import Static, Input, Button, Collapsible, Checkbox

from utils import unserialize

class S_generate_auth(Screen):
    def __init__(self, screen_uuid):
        super().__init__()
        self.screen_uuid = screen_uuid
        self.code = Static(self.generate())

    def generate(self):
        profile = self.app.getSelect()
        key = self.app.cmd(f'get-auth {profile}')
        code = self.app.cmd(f'gen-auth {key}')
        pyperclip.copy(code)
        return code

    def compose(self):
        yield Static('Your code is:')
        yield self.code
        yield Horizontal(
            Button('generate','primary'),
            Button('exit','error')
        )

    def on_button_pressed(self, event):
        op = event.button.label.plain

        if op == 'generate':
            self.code.update(self.generate())
        if op == 'exit':
            self.app.goHomeScreen()
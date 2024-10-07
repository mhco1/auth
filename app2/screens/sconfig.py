import json
from os import path

from textual.screen import Screen
from textual.containers import Vertical, Horizontal
from textual.widgets import Static, Input, Button, Collapsible, Checkbox

from utils import serialize

class S_config(Screen):
    def __init__(self, screen_uuid):
        super().__init__()
        self.screen_uuid = screen_uuid
        self.storage = Input(self.app.conf['dir']['profile'])

    def compose(self):
        yield Static('Local-storage')
        yield self.storage
        yield Horizontal(
            Button('edit','success'),
            Button('back','primary')
        )

    def on_button_pressed(self, event):
        op = event.button.label.plain

        if op == 'edit':
            self.app.conf['dir']['profile'] = path.realpath(path.expanduser(path.normpath(self.storage.value)))

            with open(path.realpath(path.join(self.app.dir, 'conf.json')), mode="w", encoding="utf-8") as f:
                json.dump(self.app.conf, f)
            
            self.app.goHomeScreen()
        if op == 'back':
            self.app.goHomeScreen()
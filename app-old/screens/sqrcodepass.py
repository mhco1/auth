from os import path, removedirs, listdir, unlink

import qrcode
from rich_pixels import Pixels
from rich.console import Console

from textual.screen import Screen
from textual.containers import Vertical, Horizontal
from textual.widgets import Button, Tree, Static, Log

from utils import unserialize

class S_qrcode_pass(Screen):
    def __init__(self, screen_uuid):
        super().__init__()
        self.screen_uuid= screen_uuid
        profile = self.app.getSelect()
        psw = unserialize(self.app.cmd(f'get-pass {profile}'))
        img = qrcode.make(psw)
        self.qr = Pixels.from_image(img,(60,60))

    def compose(self):
        yield Static(self.qr)
        yield Button('back')

    def on_button_pressed(self, event):
        op = event.button.label.plain

        if op == 'back':
            return self.app.goHomeScreen()
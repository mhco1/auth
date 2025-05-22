import qrcode
from rich.text import Text
from rich_pixels import Pixels

from textual.screen import Screen
from textual.widgets import Button, Static

from utils import serialize, unserialize

class S_pass_show(Screen):
    def __init__(self, screen_uuid):
        super().__init__()
        id = self.app.user['id']
        psw = self.app.user['pass']

        self.screen_uuid = screen_uuid
        self.psw = self.app.cmd(f"pass get '{id}' '{psw}'")
        self.psw = unserialize(self.psw)

        if psw == 'otp':
            self.psw = self.app.cmd(f"pass otp '{self.psw}'")

        img = qrcode.make(self.psw)
        self.qr = Pixels.from_image(img,(30,30))

    def compose(self):
        yield Static(self.qr, markup=False)
        yield Static('')
        yield Static("password: ")
        yield Static(self.psw, markup=False)
        yield Button(
            label='>back<',
            variant='primary',
            id='btn-back',
        )

    def on_button_pressed(self, event):
        op = event.button.id

        if op == 'btn-back':
            self.app.goto('back')
            return

        return
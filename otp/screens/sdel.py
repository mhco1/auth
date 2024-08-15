from textual.containers import Vertical, Horizontal
from textual.screen import Screen
from textual.widgets import Static, Button

from utils import cmd


class S_del(Screen):
    def compose(self):
        yield Static(f'You would like delete "{self.app.service}"')
        yield Horizontal(
            Button.success('yes'),
            Button.error('no'),
        )

    def on_button_pressed(self, event):
        op = event.button.label.plain

        if op == 'yes':
            cmd(self.app, f"remove {self.app.service}")
            self.app.g_log.write(f"remove {self.app.service}")

        self.app.goHomeScreen('del')
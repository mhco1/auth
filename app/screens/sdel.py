from textual.screen import Screen
from textual.containers import Vertical, Horizontal
from textual.widgets import Button, Tree, Static, Log

from utils import cmd


class S_del(Screen):
    def compose(self):
        yield Static(f"You would like delete {self.app.getTreeOp('all')}")
        yield Horizontal(
            Button.success('yes'),
            Button.error('no'),
        )

    def on_button_pressed(self, event):
        op = event.button.label.plain

        if op == 'yes':
            cmd(self.app, f"remove {self.app.getTreeOp('all')} {self.app.getTreeOp('root')}")
            self.app.g_log.write(f"remove {self.app.getTreeOp('all')} {self.app.getTreeOp('root')}")

        self.app.goHomeScreen('del')
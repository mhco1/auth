from textual.screen import Screen
from textual.containers import Vertical, Horizontal
from textual.widgets import Static, Button, Input, Log

from utils import cmd


def Input1 (title,placeholder,password,id):
    return Vertical(
        Static(title),
        Input(placeholder=placeholder,password=password,id=id),
    )

class S_add(Screen):
    def compose(self):

        log = Log(id="log")
        log.write('Log...\n')

        yield Horizontal(
            Vertical(
                Input1('Name','name...',False, 'name'),
                Input1('keyword','kerword...', False, 'keyword'),
            ),
            log,
            classes='l1'
        )
        yield Horizontal(
            Button.success('add'),
            Button.error('cancel'),
        )

    def on_button_pressed(self, event):
        op = event.button.label.plain
        i_name = self.query_one('#name').value
        i_keyword = self.query_one('#keyword').value

        if op == 'add':
            cmd(self.app, f'insert "{i_name}" "{i_keyword}"')
            self.app.g_log.write(f"add {i_name}\n")

        self.app.goHomeScreen('add')
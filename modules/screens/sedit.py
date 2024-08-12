from textual.screen import Screen
from textual.containers import Vertical, Horizontal
from textual.widgets import Button, Static, Input, Log

from ..utils import cmd


def Input1 (title,placeholder,password,id):
    return Vertical(
        Static(title),
        Input(placeholder=placeholder,password=password,id=id),
    )

class S_edit(Screen):
    def compose(self):

        log = Log(id="log")
        log.write('Log...\n')

        yield Horizontal(
            Vertical(
                Input1('Name','name...',False,'name'),
                Input1('Password','password...',True,'psw'),
                Input1('Repeat password','password...',True,'psw2'),
            ),
            log,
            classes='l1'
        )
        yield Horizontal(
            Button.success('edit'),
            Button.error('cancel'),
        )

    def on_button_pressed(self, event):
        op = event.button.label.plain
        log = self.query_one('#log')
        i_name = self.query_one('#name').value
        i_psw = self.query_one('#psw').value
        i_psw2 = self.query_one('#psw2').value
        
        if i_psw != i_psw2:
            log.write('wrong password\n')
            return
        
        if op == 'edit':
            cmd(self.app, f"insert {i_name} {i_psw}")
            self.app.g_log.write(f"edit {i_name}\n")

        self.app.goHomeScreen('edit')
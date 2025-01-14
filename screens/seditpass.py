import pyperclip
from os import makedirs, path

from textual.screen import Screen
from textual.containers import Vertical, Horizontal
from textual.widgets import Static, Input, Button, Collapsible, Checkbox

from utils import serialize, unserialize

class S_edit_pass(Screen):
    def __init__(self, screen_uuid):
        super().__init__()
        self.screen_uuid = screen_uuid
        psw = ''
        if self.app.select != '':
            profile = self.app.getSelect()
            psw = unserialize(self.app.cmd(f'get-pass {profile}'))
        self.info = Static('', classes='info')
        self.profile = Input(self.app.select)
        self.psw = Input(psw, password=True)
        self.psw1 = Input(psw, password=True)
        self.gen_len = Input('20', type='integer')
        self.gen_num = Checkbox('number',value=True)
        self.gen_char = Checkbox('special characters',value=True)
    
    def compose(self):
        yield self.info
        yield Static('Profile:')
        yield self.profile
        yield Static('Password:')
        yield Horizontal(
            self.psw,
            Button('show/hidden'),
            Button('copy'),
        )
        yield Static('Repeat password:')
        yield self.psw1
        yield Vertical(
            Static('Generate:'),
            Collapsible(
                Horizontal(
                    Vertical(
                        Static('Length:'),
                        self.gen_len,
                    ),
                    Vertical(
                        Static('Include:'),
                        self.gen_num,
                        self.gen_char,
                    ),
                ),
                Button('generate')
            )
        )
        yield Horizontal(
            Button('edit','success'),
            Button('exit','error')
        )

    def on_button_pressed(self, event):
        op = event.button.label.plain
        
        if op == 'generate':
            cmd = 's'
            if not self.gen_num.value:
                cmd += '0'
            if self.gen_char.value:
                cmd += 'y'
            psw = self.app.cmd(f'gen-pass {cmd} {self.gen_len.value}')
            self.psw.clear()
            self.psw.insert_text_at_cursor(psw)
            self.psw1.clear()
            self.psw1.insert_text_at_cursor(psw)
        if op == 'copy':
            pyperclip.copy(self.psw.value)
        if op == 'show/hidden':
            self.psw.password = self.psw1.password = not self.psw.password
        if op == 'edit':
            err = {
                'notProfile': self.profile.value == '',
                'notPsw': self.psw.value == '',
                'notPswEqual': self.psw.value != self.psw1.value,
            }

            if True in err.values():
                if err['notProfile']:
                    return self.info.update('profile is empty\n')
                if err['notPsw']:
                    return self.info.update('password is empty\n')
                if err['notPswEqual']:
                    return self.info.update('password is not equal\n')
            self.info.update('')
        
            self.app.select = path.normpath(self.profile.value)
            profile = self.app.getSelect()
            psw = serialize(self.psw.value)
            if not path.isdir(profile):
                makedirs(profile)
            self.app.cmd(f'set-pass {profile} "{psw}"')
            self.app.goHomeScreen()
            return

        if  op == 'exit':
            self.app.goHomeScreen()
        
        return

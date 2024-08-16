import os
from textual.screen import Screen
from textual.containers import Vertical, Horizontal
from textual.widgets import OptionList, Button, Static

from utils import cmd

from .sdel import S_del
from .sadd import S_add

class S_home(Screen):
    def compose(self):
        opList = OptionList(
            *os.listdir('/home/x/.2fa')
        )

        serviceLabel = Static(f"Label: {self.app.service}", id='service')

        yield Horizontal(
            Vertical(
                Static('Services:'),
                opList,
                self.app.g_log,
                classes='l1'
            ),
            Vertical(
                serviceLabel,
                Button('auth'),
                Button('add'),
                Button('del'),
                classes='l2'
            ),
        )

    def on_option_list_option_selected (self, event):
        serviceLabel = self.query_one('#service')
        setattr(self.app, 'service', event.option.prompt)
        serviceLabel.update(f'Label: {self.app.service}')

    def on_button_pressed(self, event) -> None:
        op = event.button.label.plain

        if op == 'add':
            self.app.changeScreen(S_add(), 'add')
            return

        if self.app.service == '':
            self.app.g_log.write('select one service\n')
            return

        if op == 'auth':
            code = cmd(self.app, f"generate {self.app.service}")
            self.app.g_log.write(f"generate {self.app.service}\n")
            self.app.g_log.write(f"code: {code}\n")
            return
        
        if op == 'del':
            self.app.changeScreen(S_del(), 'del')
            return
        
        return
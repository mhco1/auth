import pyperclip
from os import path

from textual.screen import Screen
from textual.widgets import Input, Button, Tree, Static, OptionList,Log
from textual.widgets.option_list import Option, Separator

from utils import unserialize
from screens.sremove import S_remove
from screens.seditpass import S_edit_pass
from screens.screatauth import S_creat_auth
from screens.sgenerateauth import S_generate_auth
from screens.sqrcodepass import S_qrcode_pass

class S_profile(Screen):

    def __init__(self, screen_uuid):
        super().__init__()
        self.screen_uuid = screen_uuid
        self.info = Static('',classes='info')
    
    def compose(self):
        yield self.info
        yield Static('Profile:')
        yield Static(self.app.select)
        yield OptionList(
            Separator(),
            Option('Profile',disabled=True),
            Separator(),
            Option('copy',id='op_c'),
            Option('back',id='op_b'),
            Option('remove',id='op_r'),
            Separator(),
            Option('Pass',disabled=True),
            Separator(),
            Option('edit',id='op_pe'),
            Option('copy',id='op_pc'),
            Option('qrcode', id='op_pq'),
            Separator(),
            Option('Auth',disabled=True),
            Separator(),
            Option('generate',id='op_ag'),
            Option('create',id='op_ac'),
            id='op'
        )

    def on_option_list_option_selected(self,event):
        op = event.option.id
        if op == 'op_c':
            profile = self.app.select.split('/')[-1]
            pyperclip.copy(profile);
            self.info.update('copy profile')
        if op == 'op_b':
            return self.app.goHomeScreen()
        if op == 'op_r':
            return self.app.changeScreen(S_remove)
        if op == 'op_pe':
            return self.app.changeScreen(S_edit_pass)
        if op == 'op_pc':
            profile = self.app.getSelect()
            psw = unserialize(self.app.cmd(f'get-pass {profile}'))
            pyperclip.copy(psw);
            self.info.update('copy pass')
        if op == 'op_pq':
            self.app.changeScreen(S_qrcode_pass)
        if op == 'op_ag':
            if not path.isfile(path.normpath(path.join(self.app.getSelect(),'./token'))):
                self.info.update('Token not create')
                return
            self.app.changeScreen(S_generate_auth)
        if op == 'op_ac':
            self.app.changeScreen(S_creat_auth)

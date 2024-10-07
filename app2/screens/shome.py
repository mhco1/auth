import re
import json
from os import path

from textual.screen import Screen
from textual.containers import Vertical, Horizontal
from textual.widgets import Input, Button, Tree, Static, OptionList,Log
from textual.widgets.option_list import Option, Separator

from utils import convertJsonToTree, getPathTree
from screens.sprofile import S_profile
from screens.seditpass import S_edit_pass
from screens.sconfig import S_config

class S_home(Screen):
    def __init__(self, screen_uuid):
        super().__init__()
        self.screen_uuid = screen_uuid
        self.info = Static('', classes='info')
        self.tree1 = Tree('/')
        self.search = Input()
        self.profile = Static(self.app.select)

    def compose(self):
        yield Horizontal(
            self.search,
            Button('search','primary'),
            Button('configure'),
        )
        yield self.info
        yield Static(' ')
        yield Horizontal(
            self.tree1,
            Vertical(
                Static('Profile:'),
                self.profile
            )
        )
        yield Static(' ')
        yield Horizontal(
            Button('new','success'),
            Button('select','primary')
        )

    def on_button_pressed(self, event):
        op = event.button.label.plain
        self.info.update('')

        if op == 'configure':
            self.app.changeScreen(S_config)
            return
        if op == 'search':
            if re.search(r'.key$', self.search.value):
                return
            search = re.sub(r'.key$','',self.app.getSelect(self.search.value))
            if not path.isdir(search):
                return
            treeJson = self.app.cmd(f"tree {search}")
            name = '/'
            if self.search.value != '':
                name = self.search.value
            convertJsonToTree(name, self.tree1, json.loads(treeJson))
            return
        if op == 'new':
            self.app.select = ''
            self.app.changeScreen(S_edit_pass)
            return
        if op == 'select':
            if self.app.select == '':
                return self.info.update('No one profile selected')               
            self.app.changeScreen(S_profile)
            return
    
    def on_tree_node_selected(self, event):
        isProfile = not event.node.allow_expand
        if isProfile:
            arrPath = getPathTree(event.node)
            self.app.select = path.normpath('/'.join(['./',*arrPath]))
            self.profile.update(self.app.select)
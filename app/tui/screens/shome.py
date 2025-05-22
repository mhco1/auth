from rich.text import Text

from textual.screen import Screen
from textual.containers import Vertical, Horizontal
from textual.widgets import Static, Input, Button, ListView, Collapsible, Label

from utils import convertToListView
from screens.suser import S_user

class S_home(Screen):
    def __init__(self, screen_uuid):
        super().__init__()
        self.screen_uuid = screen_uuid
        #self.info = Static(Text(''), classes='info')
        self.data_tag = []
    
    def compose(self):
        yield Static('',id='info')
        yield Horizontal(
            Input(id='input-add-user'),
            Button('>add user<','success',id='btn-add-user'),
            classes='lh'
        )
        yield Horizontal(
            Vertical(
                Horizontal(
                    Static('user: '),
                    Static('', id='select-user'),
                ),
                Horizontal(
                    Input(id='input-user'),
                    Button('>search<','primary',id='btn-search-user'),
                ),
                ListView(id='list-user'),
                Button('>select<','primary',id='btn-select-user'),
                classes='lv'
            ),
            Vertical(
                Horizontal(
                    Static('tag: '),
                    Static('', id='select-tag'),
                ),
                Horizontal(
                    Input(id='input-tag'),
                    Button('>search<','primary',id='btn-search-tag'),
                ),
                ListView(id='list-tag')
            ),
        )
    
    def on_button_pressed(self, event):
        op = event.button.id
        #self.info.update("")

        if op == 'btn-add-user':
            name = self.query_one('#input-add-user').value
            if name == '':
                self.query_one('#info').update('input is empty')
                return
            self.app.cmd(f"user add '{name}'")
            return
        if op == 'btn-search-user':
            term = self.query_one('#input-user').value
            tag = ' '.join(self.data_tag)
            res = self.app.cmd(f"search -n '{term}' {tag}")
            self.query_one('#list-user').clear()
            self.query_one('#list-user').insert(0, convertToListView(res, ['id']))
            return
        if op == 'btn-search-tag':
            term = self.query_one('#input-tag').value
            res = self.app.cmd(f"search -t -n '{term}'")
            self.query_one('#list-tag').clear()
            self.query_one('#list-tag').insert(0, convertToListView(res))
            return
        if op == 'btn-select-user':
            name = self.app.user['name']
            if name == '':
                self.query_one('#info').update('user not selected')
                return
            self.app.goto('new', S_user)
            return
        return
    
    def on_list_view_selected(self, event):
        op = event.list_view.id
        name = event.item.name

        if op == 'list-user':
            id = event.item.prop["id"]
            self.app.user['name'] = name
            self.app.user['id'] = id

            self.query_one("#select-user").update(name)
            self.query_one("#select-user").refresh()
            return
        if op == 'list-tag':
            if name in self.data_tag:
                self.data_tag.remove(name)
            else:
                self.data_tag.append(name)

            self.query_one("#select-tag").update(" ".join(self.data_tag))
            return

        return
import pyperclip

from textual.screen import Screen
from textual.containers import Vertical, Horizontal
from textual.widgets import Static, Button, ListView, ListItem, Input, Collapsible, Checkbox

from utils import convertToListView, unserialize, serialize
from screens.sremoveuser import S_remove_user
from screens.sremovepass import S_remove_pass
from screens.spassshow import S_pass_show

class S_user(Screen):
    def __init__(self, screen_uuid):
        super().__init__()
        self.screen_uuid = screen_uuid

    def compose(self):
        yield Horizontal(
            Static(f"user: "),
            Input(self.app.user['name'],id='input-user-name'),
            Button('>copy<','primary',id='btn-user-copy'),
            Button('>edit<','success',id='btn-user-edit'),
            Button('>remove<','error',id='btn-user-remove'),
            classes='lh'
        )
        yield Static('',id='info')
        # tag
        yield Vertical(
            # select
            Vertical(
                Horizontal(
                    Static('tag: '),
                    Static('', id='select-tag'),
                ),
                ListView(
                    *convertToListView(
                        self.app.cmd(f"tag ls '{self.app.user['id']}'")
                    ),
                    id='list-tag',
                ),
                Button('>remove<','error',id='btn-tag-remove'),
                classes='lh'
            ),
            Horizontal(
                Input('', id='form-input-tag'),
                Button('>add<','success',id='form-btn-tag-add')
            ),
            classes='lh',
        )
        # pass
        yield Vertical(
            # select
            Vertical(
                Horizontal(
                    Static('pass: '),
                    Static('',id='select-pass'),
                ),
                ListView(
                    *convertToListView(
                        self.app.cmd(f"pass ls '{self.app.user['id']}'")
                    ),
                    id='list-pass',
                ),
                Horizontal(
                    Button('>remove<','error',id='btn-pass-remove'),
                    Button('>copy<','primary',id='btn-pass-copy'),
                    Button('>show<','primary',id='btn-pass-show'),
                ),
                classes='lh'
            ),
            Horizontal(
                Static('type: '),
                Input('', id='form-input-pass-type'),
            ),
            Static('password:'),
            Horizontal(
                Input(password=True, id='form-input-pass'),
                Button('>show/hidden<','primary',id='form-btn-pass-show-hidden'),
                Button('>add<','success',id='form-btn-pass-add'),
            ),
            Static('repeat password:'),
            Input(password=True,id='form-input-pass2'),
            Collapsible(
                Horizontal(
                    Vertical(
                        Static('length'),
                        Input('20','integer',id='form-input-pass-gen'),
                    ),
                    Vertical(
                        Static('include:'),
                        Checkbox('number',True,id='form-ckbox-num'),
                        Checkbox('special characters',True,id='form-ckbox-symbol'),
                    ),
                ),
                Button('>generate<','primary',id='form-btn-pass-gen'),
                title='generate',
            ),
            classes='lh'
        )
        yield Button('back','primary',id='btn-back-screen')

    def on_button_pressed(self, event):
        op = event.button.id

        if op == 'btn-user-copy':
            pyperclip.copy(self.app.user['name'])
            self.query_one('#info').update('copy user')
            return
        if op == 'btn-user-edit':
            input_user_name = self.query_one('#input-user-name').value
            if input_user_name == self.app.user['name']:
                self.query_one('#info').update('name is the same')
                return
            self.app.cmd(f"user edit '{self.app.user['id']}' '{input_user_name}'")
            self.query_one('#info').update('change name')
            return
        if op == 'btn-user-remove':
            self.app.goto('new', S_remove_user)
            return
        if op == 'btn-tag-remove':
            id = self.app.user['id']
            tag = self.app.user['tag']
            self.app.cmd(f"tag rm '{id}' '{tag}'")
            res = self.app.cmd(f"tag ls '{id}'")
            self.query_one('#list-tag').clear()
            self.query_one('#list-tag').insert(0, convertToListView(res))
            return
        if op == 'form-btn-tag-add':
            id = self.app.user['id']
            tag = self.query_one('#form-input-tag').value
            self.app.cmd(f"tag add '{id}' '{tag}'")
            res = self.app.cmd(f"tag ls '{id}'")
            self.query_one('#list-tag').clear()
            self.query_one('#list-tag').insert(0, convertToListView(res))
            return
        if op == 'btn-pass-remove':
            self.app.goto('new', S_remove_pass)
            return
        if op == 'btn-pass-copy':
            id = self.app.user['id']
            psw = self.app.user['pass']

            if psw == '':
                self.query_one('#info').update('password not selected')
                return

            res = self.app.cmd(f"pass get '{id}' '{psw}'")
            res = unserialize(res)

            if psw == 'otp':
                res = self.app.cmd(f"pass otp '{res}'")

            pyperclip.copy(res)
            self.query_one('#info').update('copy password')
            return
        if op == 'btn-pass-show':
            if self.app.user['pass'] == '':
                self.query_one('#info').update('any password was not select')
                return
            self.app.goto('new', S_pass_show)
            return
        if op == 'form-btn-pass-show-hidden':
            self.query_one('#form-input-pass2').password = self.query_one('#form-input-pass').password = not self.query_one('#form-input-pass').password
            return
        if op == 'form-btn-pass-add':
            id = self.app.user["id"]
            pass_type = self.query_one('#form-input-pass-type').value
            psw = self.query_one('#form-input-pass').value
            psw2 = self.query_one('#form-input-pass2').value

            if pass_type == '':
                self.query_one('#info').update('type is empty')
                return
            if psw == '':
                self.query_one('#info').update('password is empty')
                return
            if psw != psw2:
                self.query_one('#info').update('password is not equal')
                return

            self.app.cmd(f"pass add '{id}' '{serialize(psw)}' '{pass_type}'")
            self.query_one('#info').update('pass add')
            res = self.app.cmd(f"pass ls '{id}'")
            self.query_one('#list-pass').clear()
            self.query_one('#list-pass').insert(0, convertToListView(res))
            return
        if op == 'form-btn-pass-gen':
            len = self.query_one('#form-input-pass-gen').value
            parms = ''
            if not self.query_one('#form-ckbox-num').value:
                parms += '-n '
            if not self.query_one('#form-ckbox-symbol').value:
                parms += '-s '
            res = self.app.cmd(f"pass gen {parms} '{len}'")
            self.query_one('#form-input-pass').value = res
            self.query_one('#form-input-pass2').value = res
            return
        if op == 'btn-back-screen':
            self.app.goto('home')
            return
        return

    def on_list_view_selected(self, event):
        op = event.list_view.id
        name = event.item.name

        if op == 'list-pass':
            self.app.user['pass'] = name
            self.query_one('#select-pass').update(name)
            return

        if op == 'list-tag':
            self.app.user['tag'] = name
            self.query_one('#select-tag').update(name)
            return
        return
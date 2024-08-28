from textual.screen import Screen
from textual.containers import Vertical, Horizontal
from textual.widgets import Button, Static, Input, Log, Collapsible, Checkbox

#from utils import cmd


def Input1 (title,placeholder,password,id,value=''):
    return Vertical(
        Static(title),
        Input(placeholder=placeholder,password=password,id=id,value=value),
    )

class S_edit(Screen):
    def compose(self):

        log = Log(id="log")
        log.write('Log...\n')

        name = self.app.getTreeOp('all')
        pass1 = self.app.cmd(f"get {self.app.getTreeOp('all')}") if self.app.getTreeOp('root') != '' else ''

        yield Horizontal(
            Vertical(
                Input1('Name','name...',False,'name',name),
                Horizontal(
                    Input1('Password','password...',True,'psw',pass1),
                    Button('\uf021'),
                ),
                Input1('Repeat password','password...',True,'psw2',pass1),
                Collapsible(Vertical(
                    Static('Length:'),
                    Input('30', type='integer',id='gen_len'),
                    Static('Include:'),
                    Checkbox('number',value=True,id='gen_num'),
                    Checkbox('special characters',value=True,id='gen_char'),
                )),
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
        i_name = self.query_one('#name')
        i_psw = self.query_one('#psw')
        i_psw2 = self.query_one('#psw2')

        if op == '\uf021':
            gen_len = self.query_one('#gen_len').value
            gen_num = self.query_one('#gen_num').value
            gen_char = self.query_one('#gen_char').value
            gen_cmd = 's'
            if not gen_num:
                gen_cmd += '0'
            if gen_char:
                gen_cmd += 'y'
            gen_pwd  = self.app.cmd(f'generate-key {gen_cmd} {gen_len}')
            i_psw.clear()
            i_psw.insert_text_at_cursor(gen_pwd)
            i_psw2.clear()
            i_psw2.insert_text_at_cursor(gen_pwd)
            return
        
        if op == 'edit':

            err = {
                'notPsw': i_psw.value == '',
                'notName': i_name.value == '',
                'notPswEqual': i_psw.value != i_psw2.value,
            }

            if True in err.values():
                if err['notName']: log.write('name is empty\n')
                if err['notPsw']: log.write('password is empty\n')
                if err['notPswEqual']: log.write('password is not equal\n')
                return

            self.app.cmd(f'insert {i_name.value} "{i_psw.value}"')
            self.app.g_log.write(f"edit {i_name.value}\n")
        
        self.app.goHomeScreen('edit')
        return
import json

from textual.screen import Screen
from textual.containers import Vertical, Horizontal
from textual.widgets import Button, Tree, Static, OptionList,Log
from textual.widgets.option_list import Option, Separator

from utils import convertJsonToTree, getPathTree
from screens.sedit import S_edit
from screens.sdel import S_del

#from .sdel import S_del
#from .sedit import S_edit

class S_home(Screen):

    tree_op = Static('')

    def Tree(self, name):
        tj = [{}]
        tjs = self.app.cmd(f'tree {name}')
        if tjs != '' : tj = json.loads(tjs)
        t = Tree(name)
        t.root.expand()
        convertJsonToTree(t, tj)
        return t

    def tree_op_update(self):
        root = self.app.tree_op['root']
        path = '/'.join(str(x) for x in self.app.tree_op['path'])
        self.tree_op.update(f"Type: {root}\nOption: {path}")
        return

    def compose(self):
        self.tree_op_update()

        yield Horizontal(
            Vertical(
                self.Tree('pass'),
                self.Tree('auth'),
                self.app.g_log,
                classes='l1'
            ),
            Vertical(
                self.tree_op,
                OptionList(
                    Option('\uf01e reset', id='op_r'),
                    Option('\U000f0306 auth', id='op_a', disabled=True),
                    Option('\uf007 copy user', id='op_cu', disabled=True),
                    Option('\uf023 copy pass', id='op_cp', disabled=True),
                    Option('\U000f1a7c edit', id='op_e',),
                    Option('\uf00d delete', id='op_d', disabled=True),
                    id='op'
                ),
                classes='l2'
            ),
        )

    def on_tree_node_selected(self, event):
        op = self.query_one('#op')
        isFolder = event.node.allow_expand
        isSelect = self.app.getTreeOp('root') != ''
        isDelete = not op.get_option('op_d').disabled

        if not isFolder:
            self.app.tree_op = getPathTree(event.node)
            root = self.app.tree_op['root']
            op.get_option('op_d').disabled = False
            op.get_option('op_cu').disabled = False
            
            if root == 'pass':
                op.get_option('op_cp').disabled = False
                op.get_option('op_a').disabled = True
            if root == 'auth':
                op.get_option('op_a').disabled = False
                op.get_option('op_cp').disabled = True
            self.tree_op_update()
    
        if isDelete and not isSelect:
            op.get_option('op_cu').disabled = True
            op.get_option('op_d').disabled = True

        return
    
    def on_option_list_option_selected(self ,event):
        op = event.option.id

        if op == 'op_r':
            op1 = self.query_one('#op')
            self.app.tree_op = {
                'root': '',
                'path': [],
            }
            op1.get_option('op_d').disabled = True
            op1.get_option('op_cu').disabled = True
            op1.get_option('op_cp').disabled = True
            op1.get_option('op_a').disabled = True
            self.tree_op_update()
            return
        
        if op == 'op_e':
            self.app.changeScreen(S_edit(), 'edit')
            return
        
        if self.app.getTreeOp() == '':
            self.app.g_log.write('select one first\n')
            return

        if op == 'op_d':
            self.app.changeScreen(S_del(), 'del')
            return

        if op == 'op_a':
            path = self.app.getTreeOp('all')
            code = self.app.cmd(f"generate-key-code {path}")
            self.app.g_log.write(f"generate code {path}\n")
            self.app.g_log.write(f"code: {code}\n")
            return        
        
        if op == 'op_cu':
            name = self.app.getTreeOp('last')
            self.app.cmd(f"copy-user {name}")
            self.app.g_log.write(f"copy user {name}\n")
            return
        
        if op == 'op_cp':
            path = self.app.getTreeOp('all')
            self.app.cmd(f"copy-key {path}")
            self.app.g_log.write(f"copy pass {path}\n")
            return

        return
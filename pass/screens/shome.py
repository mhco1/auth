import json

from textual.screen import Screen
from textual.containers import Vertical, Horizontal
from textual.widgets import Button, Tree, Static, Log

from utils import cmd, convertJsonToTree, getPathTree
from .sdel import S_del
from .sedit import S_edit

class S_home(Screen):
    def compose(self):
        treeJson = json.loads(cmd(self.app, 'tree'))
        tree = Tree('password-store')
        tree.root.expand()
        convertJsonToTree(tree, treeJson)

        pswLabel = Static('Label: ' + str(self.app.psw), id='psw')
        pswLabel.styles.padding = 0
        
        yield Horizontal(
            Vertical(
                tree,
                self.app.g_log,
                classes='l1'
            ),
            Vertical(
                pswLabel,
                Button('copy'),
                Button('edit'),
                Button('del'),
                classes='l2'
            ),
        )

    def on_tree_node_selected(self, event):
        isFolder = not event.node.allow_expand

        if(isFolder):
            pswLabel = self.query_one('#psw')
            setattr(self.app, 'psw', getPathTree(event.node))
            pswLabel.update('Label: ' + self.app.psw)
        return
    
    def on_button_pressed(self, event) -> None:
        op = event.button.label.plain

        if op == 'edit':
            self.app.changeScreen(S_edit(), 'edit')
            return

        if self.app.psw == '':
            self.app.g_log.write('select one passord\n')
            return

        if op == 'copy':
            cmd(self.app, f"copy {self.app.psw}")
            self.app.g_log.write(f"copy {self.app.psw}\n")
            return
        
        if op == 'del':
            self.app.changeScreen(S_del(), 'del')
            return

        return
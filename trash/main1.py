import json
import re
from os import popen
from textual.app import App, ComposeResult, RenderResult
from textual.containers import Vertical, Horizontal
from textual.widget import Widget
from textual.widgets import Button, Tree, Log


def getPass():
    cmd = 'tree -J ~/.password-store'
    return popen(cmd).read()

def convertJsonToTree(tree, jsonTree):
    jsonTree1 = jsonTree[0]
    tree1 = tree.root

    def recursive(t, j):
        if j['type'] == 'directory':
            tt = t.add(j['name'])

            for jj in j['contents']:
                recursive(tt, jj)

        if j['type'] == 'file':
            t.add_leaf(re.sub(r'.gpg', '', j['name']))

        return

    for x in jsonTree1['contents']:
        recursive(tree1, x)

    return

def getPathTree(node):
    def recursive(node, txt):
        txt1 = node.label.plain
        if(txt1 == 'password-store'): return txt[slice(-1)]
        txt = f"{txt1}/{txt}"
        return recursive(node.parent, txt)
    
    return recursive(node, '')

class Body(Widget):
    def compose(self) -> ComposeResult:
        treePassJson = json.loads(getPass())
        tree = Tree('password-store')
        tree.styles.width = "auto"
        tree.root.expand()
        convertJsonToTree(tree, treePassJson)

        yield Vertical(
            tree,
            classes='body'
        )

    def on_tree_node_selected(self, event):
        isFolder = not event.node.allow_expand

        if(isFolder):
            log = self.query_one('#log')
            self.myPassSelect = getPathTree(event.node)
            log.clear()
            log.write('Label: ' + self.myPassSelect)
        
        return


class Sidebar(Widget):
    def compose(self) -> ComposeResult:
        log = Log(id='log')
        log.write('Label: ')
        log.styles.height = 2

        yield Vertical(
            log,
            Button('edit'),
            classes='sidebar'
        )

class MyApp(App):
    CSS_PATH = 'main.css'

    def compose(self) -> ComposeResult:
        yield Horizontal(
            #Body(),
            Sidebar(),
        )

def main():
    app = MyApp()
    app.run()
    return


if __name__ == "__main__":
    main()

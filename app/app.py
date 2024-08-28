from os import popen

from textual.app import App, ComposeResult
from textual.widgets import Static, Log

from screens.shome import S_home

class MyApp(App):
    CSS_PATH = 'style.css'
    tree_op = {
        'root': '',
        'path': [],
    }
    g_log = Log(id='log')

    def cmd(self, c=''):
        res = None
        with self.suspend():
            cc = '$(pwd)/app/cmd.sh ' + str(c)
            res = popen(cc).read()
        return res
    
    def getTreeOp(self, op=''):
        if(op == 'root'): return self.tree_op['root']
        if(op == 'last'): return self.tree_op['path'][-1]
        return '/'.join([self.tree_op['root'] if op == 'all' else '',*self.tree_op['path']])

    def changeScreen(self, s_class, s_name):
        self.pop_screen()
        self.uninstall_screen('home')
        self.install_screen(s_class,s_name)
        self.push_screen(s_name)
        return

    def goHomeScreen(self, s_name):
        self.pop_screen()
        self.uninstall_screen(s_name)
        self.install_screen(S_home(), 'home')
        self.push_screen('home')
        return

    def compose(self) -> ComposeResult:
        self.g_log.write('Log...\n')
        self.install_screen(S_home(), 'home')
        self.push_screen('home')
        yield Static('')
    
def main():
    app = MyApp()
    app.run()
    return


if __name__ == "__main__":
    main()

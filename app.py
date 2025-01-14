import json
from uuid import uuid4
from os import popen, path

from textual.app import App, ComposeResult
from textual.widgets import Static, Log

from screens.shome import S_home

class MyApp(App):
    CSS_PATH = 'style.scss'

    def cmd(self, c=''):
        res = None
        with self.suspend():
            cc = f'/bin/bash {self.dir}/cmd.sh ' + str(c)
            res = popen(cc).read()
        return res

    def changeScreen(self, s_class):
        s = self.screen.screen_uuid
        new_s = str(uuid4())
        self.pop_screen()
        self.uninstall_screen(s)
        self.install_screen(s_class(screen_uuid=new_s),new_s)
        self.push_screen(new_s)
        return

    def goHomeScreen(self):
        self.select = ''
        s = self.screen.screen_uuid
        self.pop_screen()
        self.uninstall_screen(s)
        self.install_screen(S_home(screen_uuid='home'), 'home')
        self.push_screen('home')
        return
    
    def getSelect(self, select = ''):
        if select == '':
            select = self.select
        return path.realpath(path.join(self.conf['dir']['profile'], f'./{select}.key'))

    def compose(self) -> ComposeResult:
        self.select = ''
        self.dir = path.realpath(path.join(__file__, '../'))
        confPath = path.realpath(path.join(self.dir, 'conf.json'))
        with open(confPath) as f:
            self.conf = json.load(f)
        self.install_screen(S_home(screen_uuid='home'), 'home')
        self.push_screen('home')
        yield Static('')

def main():
    app = MyApp()
    app.run()
    return

if __name__ == "__main__":
    main()
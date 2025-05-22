from uuid import uuid4
from os import popen, path

from textual.app import App, ComposeResult
from textual.widgets import Static

from screens.shome import S_home

class MyApp(App):
    CSS_PATH = 'style.scss'

    def goto(self, op="", s_class={}):
        if op == 'new':
            id = str(uuid4())
            self.app.data_screen.append(id)
            self.install_screen(s_class(screen_uuid=id), id)
            self.push_screen(id)
            return id
            
        if op == 'home':
            while len(self.app.data_screen) > 0:
                id = self.app.data_screen.pop()
                self.pop_screen()
                self.uninstall_screen(id)
            self.pop_screen()
            self.uninstall_screen('home')
            self.install_screen(S_home('home'),'home')
            self.push_screen('home')
            return

        if op == 'back':
            id = self.app.data_screen.pop()
            self.pop_screen()
            self.uninstall_screen(id)
            return

        return

    def cmd(self, c=''):
        res = None
        with self.suspend():
            cc = f'/bin/bash {self.dir}/cmd/cmd.sh ' + str(c)
            res = popen(cc).read()
        return res

    def compose(self) -> ComposeResult:
        self.data_screen = []
        self.user = {
            "name": '',
            "id": '',
            "pass": '',
            "tag": '',
        }
        self.dir = path.realpath(path.join(__file__, '../../'))
        self.install_screen(S_home('home'), 'home')
        self.push_screen('home')
        yield Static('')

def main():
    app = MyApp()
    app.run()
    return

if __name__ == "__main__":
    main()
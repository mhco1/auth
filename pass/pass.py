from textual.app import App, ComposeResult
from textual.widgets import Static, Log

from screens.shome import S_home

class MyApp(App):
    CSS_PATH = 'pass.css'
    psw = ''
    g_log = Log(id='log')

    def changeScreen(self, s_class, s_name):
        self.pop_screen()
        self.uninstall_screen('home')
        self.install_screen(s_class,s_name)
        self.push_screen(s_name)

    def goHomeScreen(self, s_name):
        self.pop_screen()
        self.uninstall_screen(s_name)
        self.install_screen(S_home(), 'home')
        self.push_screen('home')

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

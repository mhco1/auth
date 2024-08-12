from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static

class Screen1(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]

    def compose(self) -> ComposeResult:
        yield Static("Screen 1")

class App(App):
    SCREENS = {"screen1": Screen1()}
    BINDINGS = [("b", "push_screen('screen1')", "Screen1")]


if __name__ == "__main__":
    app = App()
    app.run()
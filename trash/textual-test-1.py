from textual.app import App, ComposeResult
from textual.widgets import Button, Welcome

class WelcomeApp(App):
#    def compose(self) -> ComposeResult:
#        yield Welcome()

    async def on_key(self) -> None:
        await self.mount(Welcome())
        self.query_one(Button).label = "YES!" 

    def on_button_pressed(self) -> None:
        self.exit()

if __name__ == "__main__":
    app = WelcomeApp()
    app.run()
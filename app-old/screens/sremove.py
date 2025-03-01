from os import path, removedirs, listdir, unlink
from textual.screen import Screen
from textual.containers import Vertical, Horizontal
from textual.widgets import Button, Tree, Static, Log

class S_remove(Screen):
    def __init__(self, screen_uuid):
        super().__init__()
        self.screen_uuid = screen_uuid

    def compose(self):
        yield Static(f"You would like remove {self.app.select}")
        yield Horizontal(
            Button('yes','success'),
            Button('no','error'),
        )

    def on_button_pressed(self, event):
        op = event.button.label.plain

        if op == 'yes':
            profile = self.app.getSelect()
            for filename in listdir(profile):
                file_path = path.join(profile, filename)
                try:
                    if path.isfile(file_path) or path.islink(file_path):
                        unlink(file_path)
                    elif path.isdir(file_path):
                        removedirs(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
            removedirs(profile)
            self.app.select = ''

        self.app.goHomeScreen()
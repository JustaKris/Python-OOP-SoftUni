import sys


class Window:
    def exit(self):
        sys.exit(0)


class Document:
    def __init__(self, filename: str):
        self.filename = filename
        self.contents = "This file cannot be modified"

    def save(self):
        with open(self.filename, 'w') as file:
            file.write(self.contents)


class ToolbarDocument:
    def __init__(self, name: str, iconname: str):
        self.name = name
        self.iconname = iconname

    def click(self):
        self.command.execute()


class MenuItem:
    def __init__(self, menu_name: str, item_name: str):
        self.menu = menu_name
        self.item = item_name

    def click(self):
        self.command.execute()


class KeyboardShortcut:
    def __init__(self, key: str, modifier: str):
        self.key = key
        self.modifier = modifier

    def click(self):
        self.command.execute()


class SaveCommand:
    def __init__(self, document: Document):
        self.document = document

    def execute(self):
        self.document.save()


class ExitCommand:
    def __init__(self, window: Window):
        self.window = window

    def execute(self):
        self.window.exit()

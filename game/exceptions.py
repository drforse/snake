class SnakeCantBeCreated(Exception):
    def __init__(self, txt):
        self.txt = txt


class SnakeCantBeDeleted(Exception):
    def __init__(self, txt):
        self.txt = txt

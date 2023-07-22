class Parameter:
    def __init__(self, id: int, name: str, definition: str = ""):
        self.id = id
        self.name = name
        self.definition = definition

    def __str__(self):
        return f"Parameter({self.id}, {self.name}, {self.definition})"

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'definition': self.definition}
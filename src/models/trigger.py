class Trigger:
    def __init__(self, id: int, name: str, description: str = ""):
        self.id = id
        self.name = name
        self.description = description

    def __str__(self):
        return f"Trigger({self.id}, {self.name}, {self.description})"

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'description': self.description}
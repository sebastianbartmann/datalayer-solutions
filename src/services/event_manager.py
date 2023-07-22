from models.event import Event

class EventManager:
    def __init__(self):
        self.events = {}  # Key: event ID, value: Event instance

    def create_event(self, id: int, name: str, description: str = ""):
        event = Event(id, name, description)
        self.events[id] = event
        return event

    def get_event(self, id: int):
        return self.events.get(id)

    def update_event(self, id: int, name: str = None, description: str = None):
        event = self.get_event(id)
        if event is None:
            return None  # No event with this ID exists

        if name is not None:
            event.name = name
        if description is not None:
            event.description = description

        return event

    def delete_event(self, id: int):
        return self.events.pop(id, None)
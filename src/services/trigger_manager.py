from models.trigger import Trigger

class TriggerManager:
    def __init__(self):
        self.triggers = {}  # Key: trigger ID, value: Trigger instance

    def create_trigger(self, id: int, name: str, description: str = ""):
        trigger = Trigger(id, name, description)
        self.triggers[id] = trigger
        return trigger

    def get_trigger(self, id: int):
        return self.triggers.get(id)

    def update_trigger(self, id: int, name: str = None, description: str = None):
        trigger = self.get_trigger(id)
        if trigger is None:
            return None  # No trigger with this ID exists

        if name is not None:
            trigger.name = name
        if description is not None:
            trigger.description = description

        return trigger

    def delete_trigger(self, id: int):
        return self.triggers.pop(id, None)
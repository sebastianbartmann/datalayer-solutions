class EventTriggerMap:
    def __init__(self):
        self.map = {}

    def add_mapping(self, event_id, trigger_id):
        if event_id in self.map:
            self.map[event_id].append(trigger_id)
        else:
            self.map[event_id] = [trigger_id]

    def get_triggers_for_event(self, event_id):
        return self.map.get(event_id, [])
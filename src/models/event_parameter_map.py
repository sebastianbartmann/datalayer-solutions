class EventParameterMap:
    def __init__(self):
        self.map = {}

    def add_mapping(self, event_id, parameter_id):
        if event_id in self.map:
            self.map[event_id].append(parameter_id)
        else:
            self.map[event_id] = [parameter_id]

    def get_parameters_for_event(self, event_id):
        return self.map.get(event_id, [])
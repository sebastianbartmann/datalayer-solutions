

from src.models.event import Event
from src.models.event_parameter_map import EventParameterMap
from src.models.event_trigger_map import EventTriggerMap


def print_event_details(event: Event, event_parameter_map: EventParameterMap, event_trigger_map: EventTriggerMap, parameters: list, triggers: list):
    print(event)
    print("\nParameters:")
    for parameter_id in event_parameter_map.get_parameters_for_event(event.id):
        # Find the parameter with the given ID
        parameter = next((p for p in parameters if p.id == parameter_id), None)
        if parameter is not None:
            print(parameter)
    print("\nTriggers:")
    for trigger_id in event_trigger_map.get_triggers_for_event(event.id):
        # Find the trigger with the given ID
        trigger = next((t for t in triggers if t.id == trigger_id), None)
        if trigger is not None:
            print(trigger)

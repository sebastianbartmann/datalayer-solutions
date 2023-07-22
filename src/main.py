'''
from fastapi import FastAPI
from .models import event

app = FastAPI()

@app.post("/events/")
async def create_event(event: event.Event):
    # Your code here...
    return event
'''

# Create instances of events
from src.models.event import Event
from src.models.event_parameter_map import EventParameterMap
from src.models.event_trigger_map import EventTriggerMap
from src.models.parameter import Parameter
from src.models.trigger import Trigger
from src.services.utils.utils import print_event_details


event1 = Event(1, 'first_open',
               'This event is triggered when the user opens the app for the first time.')
event2 = Event(2, 'session_start',
               'This event is triggered when a user engagement starts.')
event3 = Event(3, 'in_app_purchase',
               'This event is triggered when a user makes an in-app purchase.')
event4 = Event(4, 'user_engagement',
               'This event is triggered when a user interacts with the app.')
event5 = Event(5, 'ad_impression',
               'This event is triggered when a user views an ad.')

# Create instances of parameters
parameter1 = Parameter(1, 'engage_time_msec',
                       'Engagement time in milliseconds.')
parameter2 = Parameter(2, 'session_id', 'Unique session identifier.')
parameter3 = Parameter(3, 'product_id', 'Unique product identifier.')
parameter4 = Parameter(4, 'ad_id', 'Unique ad identifier.')
parameter5 = Parameter(5, 'value', 'Value of the event.')

# Create instances of triggers
trigger1 = Trigger(1, 'App opened', 'Trigger when the user opens the app.')
trigger2 = Trigger(2, 'Session started', 'Trigger when a session starts.')
trigger3 = Trigger(3, 'Made purchase',
                   'Trigger when an in-app purchase is made.')
trigger4 = Trigger(4, 'User interaction',
                   'Trigger when there is user interaction.')
trigger5 = Trigger(5, 'Ad viewed', 'Trigger when an ad is viewed.')

# Create mappings
event_parameter_map = EventParameterMap()
event_trigger_map = EventTriggerMap()

# Associate the parameters and triggers with the events
event_parameter_map.add_mapping(event1.id, parameter1.id)
event_trigger_map.add_mapping(event1.id, trigger1.id)

event_parameter_map.add_mapping(event2.id, parameter2.id)
event_trigger_map.add_mapping(event2.id, trigger2.id)

event_parameter_map.add_mapping(event3.id, parameter3.id)
event_trigger_map.add_mapping(event3.id, trigger3.id)

event_parameter_map.add_mapping(event4.id, parameter4.id)
event_trigger_map.add_mapping(event4.id, trigger4.id)

event_parameter_map.add_mapping(event5.id, parameter5.id)
event_trigger_map.add_mapping(event5.id, trigger5.id)

# Assume you have the list of parameters and triggers
parameters = [parameter1, parameter2, parameter3, parameter4, parameter5]
triggers = [trigger1, trigger2, trigger3, trigger4, trigger5]

print_event_details(event1, event_parameter_map,
                    event_trigger_map, parameters, triggers)

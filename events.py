class Event:
    def __init__(self, event_group, event_type, **kwargs):
        self.group = event_group
        self.type = event_type
        self.kwargs = kwargs

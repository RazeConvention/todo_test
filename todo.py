"""Todo Class

Contains class definition of a todo function
"""
import time
import uuid
from events import Event


class Todo:
    def __init__(self, event_queue=None):
        self.events = event_queue or [Todo._create_new_event()]
        self.data_cache = {}

        for event in self.events:
            Todo.handle(event, self)

    def _create_new_event(self):
        uid = uuid.uuid4()
        cur_time = time.time()

        event = Event(
            'todo',
            'new',
            uid=uid,
            created=cur_time,
            modified=cur_time,
        )

    @property
    def modified(self):
        self.data_cache['modified']

    @staticmethod
    def handle(event, todo):
        if event.type == "edit":
            todo.data_cache.update(event.data_cache)
        else:
            raise ValueError(f'Event Type "{event.type}" Unknown')

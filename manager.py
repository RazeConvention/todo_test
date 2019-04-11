import uuid
from .async_worker import AsyncWorker
from collections import defaultdict
from asyncio import Queue


class TODOManager:
    def __init__(self):
        self.todos = {}
        self.todo_order = []
        self.events = []
        self.event_subscribers = defaultdict(list)
        self.event_queue = Queue()
        self.event_worker = AsyncWorker(self.process_events)

    def new(self, todo):
        """Add a new todo to be managed by the todo node"""
        self.todos[todo.uid] = todo
        self.todo_order.append(todo)

    def move(self, todo_index, todo_new_index):
        todo = self.todo_order.pop(todo_index)
        self.todo_order.insert(todo_new_index, todo)

    def get_todo(self, todo_uid):
        return self.todos[todo_uid]

    def delete_todo(self, todo_uid):
        for i, todo in enumerate(self.todo_order):
            if todo.uid == todo_uid:
                break

        del self.todos[todo_uid]
        self.todo_order.pop(0)

    def on(self, event, handler):
        """Allows subscription to a handler"""
        self.event_subscribers[event] = handler

    async def handle_event(self, event):
        if event.group == 'todo':
            TODO.handle(event, self.todos[event.kwargs["target_uid"]])
        elif event.group == "manager":
            if event.type == "add":
                pass
            elif event.type == "delete":
                pass
            elif event.type == "reorder":
                pass


    async def process_events(self):
        event = await self.event_queue.get()

        await self.handle_event(event)

        coros = [handler(event) self.event_subscribers[event.type]]
        coros += [handler(event) self.event_subscribers['*']]
        await asyncio.gather(*coros)

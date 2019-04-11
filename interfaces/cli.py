from ..manager import TODOManager
from ..events import Event

help_message = """TODO MEM: The Memory only todo App
Commands:
    add:\tnew [TITLE] [DESCRIPTION]\t Creates a new todo item
    edit: edit [UID] [FIELD] [VALUE]
    show:\t\tShows to current Todo items
"""


async def run_cli():
    manager = TODOManager()

    def process_event(event):
        handle_ui_event(manager, event)

    manager.on('*', process_event)
    quit = False
    while not quit:
        cmd = input().split()
        if cmd[0] in ['h', 'help']:
            print("""TODO MEM: The Memory only todo App
Commands:
    new:\tnew [TITLE] [DESCRIPTION]\t Creates a new todo item
    show:\t\tShows to current Todo items
""")
        elif cmd[0] in ['a', 'add']:
            _, title, description = cmd
            event = Event(
                'manager', 'add', title=title, description=description)

        elif cmd[0] in ['e', 'edit']:
            _, uid, field, value = cmd
            event = Event('todo', 'edit', target=uid, field=field, value=value)

        elif cmd[0] in ['r', 'reorder']:
            _, uid, new_index = cmd
            event = Event(
                'manager', 'reorder', target=uid, new_index=new_index)

        elif cmd[0] in ['d', 'delete']:
            _, uid, new_index = cmd
            event = Event('manager', 'delete', target=uid)

        manager.add_event(event)


def handle_ui_event(manager, event):
    if event.type == 'show':
        for todo in manager.todo_order:
            print(todo)

import asyncio
from interfaces import cli

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(cli.run_cli)

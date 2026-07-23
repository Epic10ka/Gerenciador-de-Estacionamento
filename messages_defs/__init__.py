from rich import print
from rich.panel import Panel
from rich.align import Align

def error(message):
    print(Align.center(Panel(f'{message}',title = f'<[red]ERROR[/]>')))


def try_int(num):

    while True:

        try:
            return int(num)
        except ValueError:
            pass


from ui import print
from language import language

def error(message):
    print(f'\n                                   <[red]ERROR[/]>\n                               [{message}]')


def try_int(msg, lang):

    num = input(msg)
    while True:
        try:
            return int(num)
        except ValueError:
            error(f'{language[lang]['INVALID_NUM_ERROR']}')


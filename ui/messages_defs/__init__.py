from rich import print
from rich.panel import Panel
from language import language

def error(message):
    print(Panel.fit(f'[{message}]', title = '<[red]ERROR[/]>'))


def try_int(msg, lang):

    num = input(msg)
    while True:
        try:
            return int(num)
        except ValueError:
            error(f'{language[lang]['INVALID_NUM_ERROR']}')


def again_question(lang, message):

    while True:
        q = input(message).strip().upper()[0]

        if q == '' or q == 'N': return False

        elif q == 'Y' or q == 'S': return True

        else:
            error(f'{language[lang]['INVALID_OPTION_ERROR']}')

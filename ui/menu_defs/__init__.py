from ui import print, Panel, Align
from language import language
from messages_defs import error
from datetime import datetime
from vehicles import Car


def get_valid_time(msg_prompt: str, lang) -> datetime:

    while True:
        time_str = input(msg_prompt)

        try:
            #trying to convert the str input to a datetime
            time_obj = datetime.strptime(time_str,'%H:%M')

            now = datetime.now()
            time_obj = time_obj.replace(year=now.year, month=now.month, day=now.day)

            return time_obj
        except ValueError:
            error(f'{language[lang]['INVALID_TIME']}')


def register_menu(lang):

    content = f'\n       [1] {language[lang]['ENTRANCE']}\n       [2] {language[lang]['EXIT']}'

    print()
    print(Align.center(Panel(content, title=f'{language[lang]['REGISTER VEHICLE']}', width= 30)))

    while True:

        tax_per_hour = 10.0

        menu_option = input('                                      > ')
        if menu_option == '': break

        try:
            menu_option = int(menu_option)
        except ValueError:
            error(f'{language[lang]['INVALID_NUM_ERROR']}')

        match menu_option:

            case 1:

                hour_str = get_valid_time(f'\n                             {language[lang]['ENTRY_TIME']}: ', lang)



            case 2:
                pass




register_menu('ptbr')
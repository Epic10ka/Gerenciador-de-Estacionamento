from ui.UI import print, Panel, sleep

from ui.messages_defs import try_int
from ui.menu_defs import register_menu, exit_menu, show_register_menu
from language import language

def language_selection():

    print(Panel('\n[[green1]1[/]] Brazilian portuguese\n\n[[blue]2[/]] English', width=30, title= '[bright_white]SELECT A LANGUAGE[/]'))
    while True:

        user_selection = input('\n     > ').strip()[0]

        match user_selection:

            case '1':
                sleep(0.2)
                return 'ptbr'

            case '2':
                sleep(0.2)
                return 'en'


def main_menu():

    temp_language = 'ptbr'

    while True:

        content = (f'\n            [1] {language[temp_language]['REGISTER_VEHICLE']}'
                   f'\n\n            [2] {language[temp_language]['EXIT']}'
                   f'\n\n            [3] {language[temp_language]['SHOW_REGISTERS']}'
                   f'\n\n            [4] {language[temp_language]['CHANGE_LANGUAGE']}')

        print(Panel(content, title = f'{language[temp_language]['PARKING SYS']}', width=50))

        menu_option = try_int('         > ', temp_language)

        int(menu_option)

        match menu_option:

            case 1:
                register_menu(temp_language)

            case 2:
                exit_menu(temp_language)

            case 3:
                show_register_menu(temp_language)

            case 4:
                temp_language = language_selection()


if __name__ == '__main__':
    main_menu()

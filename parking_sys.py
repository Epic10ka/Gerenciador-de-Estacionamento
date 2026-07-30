from ui.UI import print, Panel

from ui.messages_defs import try_int
from ui.menu_defs import register_menu, exit_menu
from language import language


temp_language = 'ptbr'

def language_selection():

    print(Panel('\n[[green1]1[/]] Brazilian portuguese\n\n[[blue]2[/]] English', width=30, title= '[bright_white]SELECT A LANGUAGE[/]'))
    while True:

        user_selection = input('\n                                    >').strip()[0]
        user_selection = try_int(user_selection, 'en')

        match user_selection:

            case 1:
                #clear()
                user_selection = 'ptbr'

            case 2:
                user_selection = 'en'

        return user_selection


def main_menu():


    content= (f'\n            [1] {language[temp_language]['REGISTER VEHICLE']}'
              f'\n\n            [2] {language[temp_language]['EXIT']}'
              f'\n\n            [3] {language[temp_language]['SHOW REGISTERS']}'
              f'\n\n            [4] {language[temp_language]['CHANGE_LANGUAGE']}')

    while True:

        print(Panel(content, title = f'{language[temp_language]['PARKING SYS']}', width=50))

        menu_option = try_int('         > ', temp_language)

        int(menu_option)

        match menu_option:

            case 1:
                register_menu(temp_language)

            case 2:
                exit_menu(temp_language)

            case 3:
                pass

            case 4:
                language_selection()


main_menu()

from ui.UI import print, Panel, error, again_question, uuid4, re, datetime, data_save, data_load, sleep
from language import language
from models.vehicle import Vehicle


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


def menu_option(opt, lang):

    while True:

        option = input('         > ').strip()

        if option == '':
            return ''

        if option == opt:
            return option

        error(language[lang]['INVALID_OPTION_ERROR'])


def plate_verify(lang):

    while True:



        print('   ┌─────────────┐')
        print(f'        {language[lang]['PLATE']}')
        print('   └─────────────┘')

        mercosul_pattern = re.compile(r'^[A-Z]{3}\d[A-Z]\d{2}$')

        while True:

            plate = input('         > ').strip().upper()

            if mercosul_pattern.match(plate):
                return plate
            error(language[lang]['INVALID_PLATE_ERROR'])


def id_gen():

    object_id = uuid4()
    final_id = str(object_id)
    print(Panel(f'  [yellow]{final_id}[/]', title= '[bright_white]ID[/]', width = 45))
    return final_id


def search_vehicle_id(vehicle_list, lang):

    """
    Asks user an ID and search the matching vehicle in the list.
    Allows user to search a complete ID or the first characters.
    """
    if not vehicle_list:

        print(Panel.fit(f'{language[lang]['NO_REGISTERED_VEHICLE']}'))
        return None

    while True:

        search_id = input('         ID > ').strip()
        if search_id == '':
            return None

        matches = [v for v in vehicle_list if v.tracking_id.startswith(search_id)]

        if len(matches) == 1:
            return matches[0]

        elif len(matches) > 1:
            error(f'{language[lang]['TYPE_MORE_CHARACTERS']}')

        else:
            error(f'{language[lang]['VEHICLE_NOT_FOUND']}')


# [1] MENU
def register_menu(lang):

    vehicle_list = data_load()

    content = f'       [1] {language[lang]['ENTRANCE']}'

    while True:

        print()
        print(Panel(content, title=f'[blue]{language[lang]['REGISTER_VEHICLE']}[/]', width= 30))

        select = menu_option('1', lang)

        if select == '':
            break

        hour = get_valid_time(f'\n   {language[lang]['ENTRY_TIME']}: ', lang)

        plate = plate_verify(lang)

        _id_ = id_gen()

        vehicle = Vehicle(hour, plate, _id_)

        vehicle_list.append(vehicle)
        data_save(vehicle_list)

        print(f'\n {language[lang]['REGISTRATION_SUCCESSFULLY_COMPLETED']}')

        again = again_question(lang, f'\n \033[1;97m{language[lang]['REGISTER_AGAIN']}: \033[m') #using my func to verify if again is in [Y or N] (Portuguese [S or N]

        if not again:
            break


# [2] MENU
def exit_menu(lang):

    vehicle_list = data_load()

    content = f'       [1] {language[lang]['EXIT']}'

    while True:

        print()
        print(Panel(content, title = f'[red]{language[lang]['REGISTER_EXIT']}[/]', width=30))


        select = menu_option('1', lang)

        if select == '':
            break


        vehicle = search_vehicle_id(vehicle_list, lang)

        if vehicle is None:
            continue

        print(f'{language[lang]['VEHICLE_FOUND']}: {vehicle.tracking_id}')
        sleep(1)

        if vehicle is None:
            continue

        exit_time = get_valid_time(f'\n   {language[lang]['EXIT_TIME']}: ', lang)


        if lang == 'ptbr':
            value = 'R$'
        else:
            value = '$'

        vehicle.calculate_price(exit_time)

        print(f'   {language[lang]['TOTAL_TIME']}: {vehicle.total_time}')
        print(f'   {language[lang]['TAX_VALUE']}: [green]{value}[/]{vehicle.tax:.2f}')
        sleep(1)

        vehicle_list.remove(vehicle)

        data_save(vehicle_list)


# [3] MENU
def show_register_menu(lang):

    vehicle_list = data_load()

    content = (f'\n     [1] {language[lang]['SHOW_REGISTER']}'
              f'\n\n     [2] {language[lang]['SEE_QUANTITY']}')

    while True:

        print(Panel(content, title = f'[blue]{language[lang]['REGISTERED_VEHICLES']}[/]', width=35))
        break
        #Building


show_register_menu('ptbr')
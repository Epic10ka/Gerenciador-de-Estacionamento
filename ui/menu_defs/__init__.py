from ui.UI import print, Panel, error, again_question, uuid4, re, datetime, data_save, data_load
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



def register_menu(lang):

    vehicle_list = data_load()

    content = f'       [1] {language[lang]['ENTRANCE']}'

    while True:

        print()
        print(Panel(content, title=f'[blue]{language[lang]['REGISTER VEHICLE']}[/]', width= 30))

        menu_option = input('         > ').strip()

        if menu_option == '':
            break

        if menu_option != '1':
            error(language[lang]['INVALID_OPTION_ERROR'])
            continue


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




register_menu('ptbr')
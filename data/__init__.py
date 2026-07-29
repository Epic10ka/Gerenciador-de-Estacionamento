import json
import os
from pathlib import Path
from models.vehicle import Vehicle


BASE_DIR = Path(__file__).parent
DEFAULT_FILEPATH = BASE_DIR / 'vehicles.json'


def data_save(vehicle_list, filepath=DEFAULT_FILEPATH):

    data = [vehicle.to_dict() for vehicle in vehicle_list]

    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def data_load(filepath = DEFAULT_FILEPATH):

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0: #Checks if the file exists, if not, returns an empty list.
        return []

    try:

        with open(filepath, 'r') as file:
            data = json.load(file)



        return [
            Vehicle(entry = v['entry_time'], plate = v['plate'], tracking_id= v['vehicle_id']
                    )
            for v in data
        ]

    except json.JSONDecodeError:
        return []



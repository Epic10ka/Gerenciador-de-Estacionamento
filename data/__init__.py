import json
import os
from models.vehicle import Vehicle

def data_save(vehicle_list, filepath='vehicles.json'):

    data = [vehicle.to_dict() for vehicle in vehicle_list]

    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def data_load(filepath = 'vehicles.json'):

    if not os.path.exists(filepath): #Checks if the file exists, if so, returns an empty list.
        return []

    with open(filepath, 'r', encoding = 'utf-8') as file:
        data = json.load(file)

    vehicle_list =  [Vehicle(v['entry_time'], v['plate'], v['vehicle_id']) for v in data]

    return vehicle_list


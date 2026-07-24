from datetime import datetime
import math


class Vehicle:

    def __init__(self, entrance_time, plate, tracking_id, exit_time, hourly_rate):

        self.entrance_time = entrance_time
        self.plate = plate
        self.tracking_id = tracking_id
        self.exit_time = exit_time
        self.hourly_rate = hourly_rate


    def calculate_price(self, exit_time):
        pass


class Car(Vehicle):
    pass
from datetime import datetime

class Vehicle:

    """
    This class creates a Vehicle that will be a father class of Vehicles (Bikes, cars, etc...)

    #Attributes
    -It has the parking entry time
    -Plate number
    -Parking tracking ID
    -Parking exit time
    -Default tax

    #Method
    -Calculate price: Calculates the price of parking time of the vehicles.
      It calculates using the difference between entry and exit time.
      For every hour, it adds $3/R$3 | If vehicle stay less than 15 minuts

    """

    def __init__(self, entry, plate: str, tracking_id):


        self.entry_time = datetime.strftime(entry, '%H:%M')
        self.plate = plate.upper()
        self.tracking_id = tracking_id
        self.exit_time = None
        self.tax =  15

    def calculate_price(self, exit_time):

        """
        Calculates total parking time in minutes.

        """

        self.exit_time = datetime.strptime(exit_time, '%H:%M')

        total_time = self.exit_time - self.entry_time
        total_minutes = total_time. total_seconds() / 60

        if total_minutes >= 60:

            hour = total_minutes/60 * 3

            self.tax = hour

        return self.tax


    def to_dict(self):
        return {
            'entry_time': self.entry_time.strftime('%H%M') if hasattr(self.entry_time, 'strftime') else self.entry_time, #hasattr -if self.entry_time has a method 'strftime' returns True
            'plate': self.plate,
            'vehicle_id': self.tracking_id
        }


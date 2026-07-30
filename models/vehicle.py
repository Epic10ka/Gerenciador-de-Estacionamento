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


        if isinstance(entry, str):      #if receive a string, will change it to datetime.
            self.entry_time = datetime.strptime(entry, '%H:%M')
        else:
            self.entry_time = entry     #if entry already is a datetime object, keep it the same.

        self.plate = plate.upper()
        self.tracking_id = tracking_id
        self.exit_time = None
        self.tax =  5  #Value per hour
        self.total_time = 0


    def calculate_price(self, exit_time):

        """
        Calculates total parking time and the value to be paid.

        """

        if isinstance(exit_time, str):
            temp_exit = datetime.strptime(exit_time, '%H:%M')
        else:
            temp_exit = exit_time

        self.exit_time = self.entry_time.replace(

            hour = temp_exit.hour,
            minute = temp_exit.minute,
            second = 0,
            microsecond = 0
        )



        total_time = self.exit_time - self.entry_time
        self.total_time = total_time

        total_minutes = total_time. total_seconds() / 60

        if total_minutes >= 60:

            hour = total_minutes/60 * self.tax

            self.tax = hour

        return self.tax


    def to_dict(self):

        """
        Turns the vehicle save into a dictionary to make it savable in JSON
        """

        return {
            "entry_time": (
                self.entry_time.strftime("%H:%M")
                if hasattr(self.entry_time, "strftime")  #hasattr - if self.entry_time has a method 'strftime' returns True
                else self.entry_time
            ),
            "plate": self.plate,
            "vehicle_id": self.tracking_id,
        }
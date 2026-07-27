from datetime import datetime, timedelta


class Vehicle:

    """
    This class creates a Vehicle that will be a father class of Vehicles (Bikes, cars, etc...)

    -It has the parking entry time
    -Plate number
    -Parking tracking ID
    -Parking exit time
    -Default tax
    """

    def __init__(self, entry, plate: str, tracking_id):


        self.entry_time = datetime.strptime(entry, '%H:%M')
        self.plate = plate.upper()
        self.tracking_id = tracking_id
        self.exit_time = None
        self.tax =  0
        #Default tax is 15

    def calculate_price(self, exit_time):

        self.exit_time = datetime.strptime(exit_time, '%H:%M')

        total_time = self.exit_time - self.entry_time
        total_minutes = total_time.total_seconds() / 60

        if total_minutes >= 60:

            hour = total_minutes/60 * 3

            self.tax = hour + 15

        return self.tax

#teste = Vehicle('08:25','abc2', 12)


#print(teste.calculate_price('10:25'))


#class Car(Vehicle):

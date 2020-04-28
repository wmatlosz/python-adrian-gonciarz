class Car:
    def __init__(self):
        self.car_dictionary = {
            'speed': 0,
            'driver': None,
            'passenger_list': [],
            'model': None,
            'year': None,
            'color': None,
            'max_passengers': None,
            'configured': False,
        }

    def set_car_data(self, model, year, max_passengers=6, **kwargs):
        self.car_dictionary['model'] = model
        self.car_dictionary['year'] = year
        self.car_dictionary['max_passengers'] = max_passengers
        self.car_dictionary['color'] = kwargs.get('color')
        self.car_dictionary['configured'] = True

    def drive(self, speed):
        print(f'Starting driving with speed  {speed}' if self.car_dictionary.get(
            'driver') and self.car_dictionary['configured'] else 'Cannot drive,there is no driver!')
        self.car_dictionary['speed'] = speed

    def stop(self):
        self.car_dictionary['speed'] = 0

    def board_people(self, driver, *passengers):
        self.car_dictionary['driver'] = driver
        self.car_dictionary['passenger_list'] = list(passengers[0:self.car_dictionary['max_passengers']])

    def add_passengers(self, *passengers):
        if self.car_dictionary['speed'] > 0:
            print('Cannot add passengers while car is moving!')
        elif len(self.car_dictionary['passenger_list']) == self.car_dictionary['max_passengers']:
            print('No free places for new passengers available!')
        else:
            self.board_people(self.car_dictionary['driver'], *(tuple(self.car_dictionary['passenger_list']) + passengers))

    def describe_car(self):
        if not self.car_dictionary['configured']:
            print('No description for this car is available')
        else:
            description = f'This is {self.car_dictionary["model"]} made in {self.car_dictionary["year"]}.\n'
            if self.car_dictionary["color"]:
                description += f'Color of this car is {self.car_dictionary["color"]}\n'
            description += f'Currently the driver is {self.car_dictionary["driver"]} and there are {len(self.car_dictionary["passenger_list"])} passengers boarded.\n '
            description += f'Current speed of the car is {self.car_dictionary["speed"]}.' if self.car_dictionary[
                                                                                                 'speed'] > 0 else 'The car is stopped now.'
            print(description)


car_object = Car()

car_object.drive(30)
car_object.set_car_data('Honda', 1998)
car_object.board_people('Kate', 'James', 'Nina', 'Mike', 'Bob')
car_object.drive(60)
car_object.describe_car()
car_object.add_passengers('Johnny', 'Betty')
car_object.describe_car()
car_object.stop()
car_object.add_passengers('Johnny', 'Betty')
car_object.describe_car()

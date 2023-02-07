class InvalidCityException(Exception):
    
    def __init__(self):
        self.message = 'The city name is invalid.'
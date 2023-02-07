import random
import string

cities = [
    'London',
    'Manchester',
    'Paris',
    'Lecce',
    'Budapest',
    'Berlin',
    'Prague',
    'Bratislava',
    'Palermo',
    'Tokyo',
    'Langkawi',
    'Milton Keynes'
]

def random_string(length: int = 15):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
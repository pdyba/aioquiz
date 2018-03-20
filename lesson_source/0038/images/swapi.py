import requests

BASE = 'http://swapi.co/api'


def get_planet_terrain(name):
    result = requests.get(f'{BASE}/planets?search={name}').json()
    if result['results']:
        return result['results'][0]['terrain']
    raise ValueError(f'Planet {name} not found')


def get_starship_ids(film_name='A New Hope'):
    result = requests.get(f'{BASE}/films?search={film_name}').json()
    if not result['results']:
        raise ValueError(f'Film {film_name} not found')

    ids = []
    for starship in result['results'][0]['starships']:
        ids.append(starship.split('/')[-2])
    return ids


def get_starship_count(film_name='A New Hope'):
    ship_ids = get_starship_ids(film_name)
    return len(ship_ids)


def get_vehicle_names(min_length=1000):
    result = []
    next_ = f'{BASE}/starships'
    while next_:
        resp = requests.get(next_).json()
        for vehicle in resp['results']:
            if vehicle['length'] != 'unknown' and float(vehicle['length'].replace(',', '.')) >= min_length:
                result.append(vehicle['name'])
        next_ = resp['next']
    return result

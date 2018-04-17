import requests

BASE = 'http://swapi.co/api'


def get_planet_terrain(name):
    result = requests.get('{}/planets?search={}'.format(BASE, name)).json()
    if result['results']:
        return result['results'][0]['terrain']
    raise ValueError('Planet {} not found'.format(name))


def get_starship_ids(film_name='A New Hope'):
    result = requests.get('{}/films?search={}'.format(BASE, film_name)).json()
    if not result['results']:
        raise ValueError('Film {} not found'.format(film_name))

    ids = []
    for starship in result['results'][0]['starships']:
        ids.append(starship.split('/')[-2])
    return ids


def get_starship_count(film_name='A New Hope'):
    ship_ids = get_starship_ids(film_name)
    return len(ship_ids)


def get_vehicle_names(min_length=1000):
    result = []
    next_ = '{}/starships'.format(BASE)
    while next_:
        resp = requests.get(next_).json()
        for vehicle in resp['results']:
            if vehicle['length'] != 'unknown' and float(vehicle['length'].replace(',', '.')) >= min_length:
                result.append(vehicle['name'])
        next_ = resp['next']
    return result

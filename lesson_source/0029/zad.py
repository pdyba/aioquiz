from collections import defaultdict
from collections import namedtuple
from datetime import datetime

import requests


def measure_time(func):
    def wrapped(*args, **kwargs):
        start = datetime.now()
        print(start)
        resp = func(*args, **kwargs)
        end = datetime.now()
        print(end)
        print(end - start)
        return resp
    return wrapped

def deko(funkcje):
    start = datetime.now()
    print(start)
    resp = funkcje()
    end = datetime.now()
    print(end)
    print(end - start)
    return resp


@measure_time
def zad191():
    wynik = []
    an_url = 'https://pylove.org/exercise/1_19_1'
    for d in set(requests.get(an_url).json()):
        if d.isalpha():
            wynik.append(d)
    wunik = (' '.join(wynik))
    print(wunik)
    return wunik


@measure_time
def zad192():
    an_url = 'https://pylove.org/exercise/1_19_2'
    data = requests.get(an_url).text
    zliczacz = defaultdict(int)
    for let in data:
        zliczacz[let] += 1
    slowo = ''
    for _ in range(6):
        a_max, a_let = 0, ''
        for k, v in zliczacz.items():
            if v > a_max:
                a_max, a_let = v, k
        del zliczacz[a_let]
        slowo += a_let
    print(slowo)
    return slowo

from collections import Counter

@measure_time
def zad194():
    an_url = 'https://pylove.org/exercise/1_19_2'
    data = requests.get(an_url).text
    zliczacz = Counter(data)
    slowo = ''
    for let in zliczacz.most_common(6):
        slowo += let[0]
    print(slowo)
    return slowo



Ojciec = namedtuple(
    'Ojciec',
    ['imie', 'naziwsko', 'data_ur']
)

piotr = Ojciec('Piotr', 'Dyba', '1231-12-12')
print(piotr)
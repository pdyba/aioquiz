#!/usr/bin/env python3
# encoding: utf-8
import asyncio

import models
from orm import Table

psql_cfg = {
    'user': 'aiopg',
    'database': 'postgres',
    'host': '127.0.0.1',
    'password': 'aiopg'
}


async def bootstrap_db():
    for cls_name in dir(models):
        if cls_name.startswith('_'):
            continue
        cls = getattr(models, cls_name)
        if issubclass(cls, Table) and cls != Table:
            await cls.create_table()
    print('bootstrap done')

async def admin():
    new_user = {
        'email': 'piotr@dyba.it',
        'password': 'test_1',
        'img': '0000000001.jpg',
        'description': 'Przykladowy opis',
        'motivation': 'Motivation opis',
        'what_can_you_bring': 'wiedze',
        'experience': 'spore',
        'mentor': True,
        'active': True,
        'organiser': True,
        'admin': True,
        'name': 'Piotr',
        'pyfunction': 'Chief Education Officer',
        'surname': 'Dyba',
        'linkedin': 'https://www.linkedin.com/in/pdyba',
        'twitter': 'https://twitter.com/dybacompl',
        'facebook': 'https://www.facebook.com/piotr.dyba.photo',
    }

    tbl = models.Users(**new_user)
    await tbl.create()
    await models.Users.get_by_id(1)
    print('Admin Created')

async def add_question():
    await models.Question(question='Jak masz na imie ?').create()
    await models.Question(question='Czy lubisz czekolade ?', qtype='bool').create(
        )
    await models.Question(
        question='Jakie jest twoje ulubione zwierze ?',
        answares=['pyton', 'pies', 'kot', 'krolik'],
        qtype='abcd'
    ).create()
    await models.Question(
        question='Jakie rozszerzenie zwyczajową mają pliki z kodem Pythonowym ?',
    ).create()
    await models.Question(
        question='Napisz kod który doda element "a" do listy ?moja_list = []'
    ).create()
    await models.Question(
        question='Napisz kod który doda klucz "ala" o wartosci "kot" do słownika ? mojs_slownik = {}'
    ).create()
    await models.Question(
        question='Napisz kod który zsumuje wszystkie wartości w liście: moja_list = [1, 2, 3, 999, 21, 13, 91212, 12312312312]'
    ).create()
    await models.Question(
        question='Napisz kod który polaczy dwa stringi: ala="ala" i ma_kota="ma kota"'
    ).create()
    await models.Question(
        question='Napisz kod który zamieni tuple na liste: moja_tupla=("abc", "egf")'
    ).create()
    await models.Question(
        question='Które słowo kluczowe nie występuje w pythonie ?',
        answares=['class', 'def', 'function', 'return'],
        qtype='abcd'
    ).create()
    await models.Question(
        question='Czy w pythonie jest żółwik (turtle) znany z jezyka Logo',
        qtype='bool'
    ).create()
    await models.Question(
        question='Czy w pythonie jest operator peirwiastkowania',
        qtype='bool'
    ).create()
    await models.Question(
        question='Podaj nazwa metody konstruktora w klasie:',
    ).create()
    await models.Question(
        question='Czy w Pythonie wystepuje polimofrizm ?',
        qtype='bool'
    ).create()
    await models.Question(
        question='Napisz list comprehension ktora z stworzy liste wszystkich cyfr text="7y2tgr3yudha98uq0298y28823323jajshdjahdk"'
    ).create()
    await models.Question(
        question='Które słowo kluczowe nie występuje w pythonie ?',
        answares=['finally', 'cancel', 'break', 'continue'],
        qtype='abcd'
    ).create()
    await models.Question(
        question=' Czy python jest językiem obiektowym  ?',
        qtype='bool'
    ).create()
    await models.Question(
        question='które polecenie NIE zwróci listy: data = [(9,0), (1,2),(3,4)]',
        answares=[
            "sorted(data, key=lambda a: a[0], reverse=False)",
            "max(data, key=lambda a: max(a))",
            "filter(lambda a: sum(a) >5, data)",
            "min(data, key=lambda a: max(a))",
        ],
        qtype='abcd'
    ).create()
    await models.Question(
        question='Co zwróci to polecenie: data = [(9,0), (1,2),(3,4), (7,5)] print(min(data, key=lambda a: max(a)))',
        answares=[
            "(9,0)",
            "(1,2)",
            "(3,4)",
            "(7,5)",
        ],
        qtype='abcd'
    ).create()
    await models.Question(
        question='Czy można nadać kolejność elementom w słowniku?',
        qtype='bool'
    ).create()
    await models.Question(
        question='Mając zdefiniowane klasy, stworzone obiekty i wywołane funkcje jak poniżej, co zostanie wypisane do konsoli?',
        answares=[
            "HiHiBonjourGo away",
            "HiBonjourGo away",
            "Hi, Hi, Bonjour, Go away",
            'TypeError: Can not convert "NoneType" object to str implicitly'
        ],
        qtype='abcd',
        img='20',
    ).create()
    await models.Question(
        question='Co wypisze to polecenie: a = "?PDYJTAHNOGNO" print(a[2::2])',
        answares=['DG', 'PYTHON', 'DJANGO', 'pusty string'],
        qtype='abcd',
    ).create()
    await models.Question(
        question='Jak wydobyć cyfrę 0? a = [1, 2, [7, 8, 9], 3, [4, 6, [1, 0]]]',
        answares=['a[5][3][2]', 'a[6][1]', 'a[4][2][1]', 'a[9]'],
        qtype='abcd',
    ).create()
    await models.Question(
        question='Jaka jest poprawna składnia: a = "aBcDeF"',
        answares=['a.upper()', 'upper(a)', 'a(upper)', 'a.upper'],
        qtype='abcd',
    ).create()
    await models.Question(
        question='Co zostanie wypisane do konsoli ?',
        answares=[
            'MyClass',
            'a',
            '<__main__.MyClass object at 0x0000000000ADAC50>',
            'abecadlo'
        ],
        qtype='abcd',
        img='24',
    ).create()
    await models.Question(
        question='Jak będzie wyglądała lista po poleceniach: nasza_lista = ["a", "b", "c"] nasza_lista.append("z") nasza_lista.pop() nasza_lista.pop(-2) nasza_lista.remove("c") print(nasza_lista)',
        answares=['["a"]', '["b"]', '["c"]', '["z"]'],
        qtype='abcd',
    ).create()
    await models.Question(
        question='Czy ten bląd zostanie dobrze obsłużony ?',
        qtype='bool',
        img='26',
    ).create()
    await models.Question(
        question='Która składnia jest niepoprawna ?',
        answares=[
            'import random',
            'from random import random',
            'from random import randint',
            'import randint'
        ],
        qtype='abcd',
    ).create()
    await models.Question(
        question='Jeżeli chcemy dopisać do pliku, nie nadpisując jego zawartości, użyjemy ?',
        answares=[
            'open(file_name, "w")',
            'open(file_name, "r")',
            'open(file_name, "a")',
            'open(file_name, "wb")'
        ],
        qtype='abcd',
    ).create()
    await models.Question(
        question='Jakie slowo kuczlowe pozowala nam pominac metode zamykajaca plik - file.close()',
    ).create()
    await models.Question(
        question='Czy podobal Ci sie quiz',
        qtype='bool',
    ).create()
    print('question added')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bootstrap_db())
    # loop.run_until_complete(bootstrap_db())
    # loop.run_until_complete(add_question())
    loop.run_until_complete(admin())

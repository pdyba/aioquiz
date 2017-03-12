# !/usr/bin/python3.5
class Question:
    def __init__(self, question, qtype='plain', answares=[], img=False):
        self.question = question
        self.answares = answares
        self.qtype = qtype
        self.img = img

    @property
    def answares(self):
        return self.__answares

    @answares.setter
    def answares(self, value):
        self.__answares = value

    @answares.getter
    def answares(self):
        if isinstance(self.__answares, list):
            return '<p>'.join(["<b>{}.</b> {}".format(l, a) for a, l in
                               zip(self.__answares, 'abcd')])
        else:
            return self.__answares

    @property
    def question(self):
        return self.__question

    @question.setter
    def question(self, value):
        self.__question = value

    @question.getter
    def question(self):
        if isinstance(self.__question, list):
            return '<p>'.join(self.__question)
        else:
            return self.__question


class Quiz:
    question_0 = Question('Jak masz na imie ?')
    question_1 = Question('Czy lubisz czekolade ?', qtype='bool')
    question_2 = Question(
        'Jakie jest twoje ulubione zwierze ?',
        answares=['pyton', 'pies', 'kot', 'krolik'],
        qtype='abcd'
    )
    question_3 = Question(
        'Jakie rozszerzenie zwyczajową mają pliki z kodem Pythonowym ?',
    )
    question_4 = Question(
        [
            'Napisz kod który doda element "a" do listy ?',
            "moja_list = []"
        ],
    )
    question_5 = Question(
        [
            'Napisz kod który doda klucz "ala" o wartosci "kot" do słownika ?',
            "mojs_slownik = {}"
        ],
    )
    question_6 = Question(
        [
            'Napisz kod który zsumuje wszystkie wartości w liście:',
            "moja_list = [1, 2, 3, 999, 21, 13, 91212, 12312312312]"
        ],
    )
    question_7 = Question(
        [
            'Napisz kod który polaczy dwa stringi:',
            "ala='ala' i ma_kota='ma kota'"
        ],
    )
    question_8 = Question(
        [
            'Napisz kod który zamieni tuple na liste:',
            "moja_tupla=('abc', 'egf')"
        ],
    )
    question_9 = Question(
        'Które słowo kluczowe nie występuje w pythonie ?',
        answares=['class', 'def', 'function', 'return'],
        qtype='abcd'
    )
    question_10 = Question(
        'Czy w pythonie jest żółwik (turtle) znany z jezyka Logo',
        qtype='bool'
    )
    question_11 = Question(
        'Czy w pythonie jest operator peirwiastkowania',
        qtype='bool'
    )
    question_12 = Question(
        'Podaj nazwa metody konstruktora w klasie:',
    )
    question_13 = Question(
        'Czy w Pythonie wystepuje polimofrizm ?',
        qtype='bool'
    )
    question_14 = Question(
        [
            'Napisz list comprehension ktora z stworzy liste wszystkich cyfr',
            "text='7y2tgr3yudha98uq0298y28823323jajshdjahdk'"
        ]
    )
    question_15 = Question(
        'Które słowo kluczowe nie występuje w pythonie ?',
        answares=['finally', 'cancel', 'break', 'continue'],
        qtype='abcd'
    )
    question_16 = Question(
        ' Czy python jest językiem obiektowym  ?',
        'bool'
    )
    question_17 = Question(
        [
            'które polecenie NIE zwróci listy:',
            'data = [(9,0), (1,2),(3,4)]'
        ],
        answares=[
            "sorted(data, key=lambda a: a[0], reverse=False)",
            "max(data, key=lambda a: max(a))",
            "filter(lambda a: sum(a) >5, data)",
            "min(data, key=lambda a: max(a))",
        ],
        qtype='abcd'
    )
    question_18 = Question(
        [
            "Co zwróci to polecenie:",
            "data = [(9,0), (1,2),(3,4), (7,5)]",
            "print(min(data, key=lambda a: max(a)))"
        ],
        answares=[
            "(9,0)",
            "(1,2)",
            "(3,4)",
            "(7,5)",
        ],
        qtype='abcd'
    )
    question_19 = Question(
        'Czy można nadać kolejność elementom w słowniku?',
        'bool'
    )
    question_20 = Question(
        'Mając zdefiniowane klasy, stworzone obiekty i wywołane funkcje jak poniżej, co zostanie wypisane do konsoli?',
        answares=[
            "HiHiBonjourGo away",
            "HiBonjourGo away",
            "Hi, Hi, Bonjour, Go away",
            "TypeError: Can't convert 'NoneType' object to str implicitly"
        ],
        qtype='abcd',
        img=True,
    )
    question_21 = Question(
        ['Co wypisze to polecenie:', "a = '?PDYJTAHNOGNO'", 'print(a[2::2])'],
        answares=['DG', 'PYTHON', 'DJANGO', 'pusty string'],
        qtype='abcd',
    )
    question_22 = Question(
        ["Jak wydobyć cyfrę 0?", "a = [1, 2, [7, 8, 9], 3, [4, 6, [1, 0]]]"],
        answares=['a[5][3][2]', 'a[6][1]', 'a[4][2][1]', 'a[9]'],
        qtype='abcd',
    )

    question_23 = Question(
        ['Jaka jest poprawna składnia:', "a = 'aBcDeF'"],
        answares=['a.upper()', 'upper(a)', 'a(upper)', 'a.upper'],
        qtype='abcd',
    )
    question_24 = Question(
        'Co zostanie wypisane do konsoli ?',
        answares=[
            'MyClass',
            'a',
            '<__main__.MyClass object at 0x0000000000ADAC50>',
            'abecadlo'
        ],
        qtype='abcd',
        img=True,
    )
    question_25 = Question(
        [
            'Jak będzie wyglądała lista po poleceniach:',
            "nasza_lista = ['a','b', 'c']",
            "nasza_lista.append('z')",
            'nasza_lista.pop()',
            'nasza_lista.pop(-2)',
            "nasza_lista.remove('c')",
            'print(nasza_lista)'
        ],
        answares=["['a']", "['b']", "['c']", "['z']"],
        qtype='abcd',
    )
    question_26 = Question(
        'Czy ten bląd zostanie dobrze obsłużony ?',
        qtype='bool',
        img=True,
    )
    question_27 = Question(
        'Która składnia jest niepoprawna ?',
        answares=[
            'import random',
            'from random import random',
            'from random import randint',
            'import randint'
        ],
        qtype='abcd',
    )
    question_28 = Question(
        'Jeżeli chcemy dopisać do pliku, nie nadpisując jego zawartości, użyjemy ?',
        answares=[
            "open(file_name, 'w')",
            "open(file_name, 'r')",
            "open(file_name, 'a')",
            "open(file_name, 'wb')"]
        ,
        qtype='abcd',
    )
    question_29 = Question(
        'Jakie slowo kuczlowe pozowala nam pominac metode zamykajaca plik - file.close()',
    )
    question_30 = Question(
        'Czy podobal Ci sie quiz',
        qtype='bool',
    )

    question_fin = Question(' To juz wszystko ! ', qtype='end')

    async def get(self, quid):
        return getattr(self, 'question_{}'.format(quid), self.question_fin)

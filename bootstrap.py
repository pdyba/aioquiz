#!/usr/bin/env python3.5
# encoding: utf-8
import argparse
import asyncio
from datetime import datetime
import os
import random
import shutil
import string
import types

import markdown
import yaml

import models
from orm import Table

from config import DEFAULT_USER
from utils import color_print


cls_to_skip = ('CommonTestTemplate', 'CommonTestQuestion', 'CommonTestAnswer', 'CommonTestStatus')


async def bootstrap_db():
    for cls_name in dir(models):
        if not cls_name.startswith('_'):
            try:
                cls = getattr(models, cls_name)
                if isinstance(cls, types.FunctionType) or cls_name in cls_to_skip:
                    color_print('skipping: ' + cls_name, color='yellow')
                    continue
                if issubclass(cls, Table) and cls != Table:
                    await cls.create_table()
            except TypeError:
                color_print(cls_name, color='red')
    color_print('DB bootstrap done', color='green')


async def gen_users():
    """
    For development only.
    """
    start = datetime.utcnow()

    def text():
        rdata = list(string.ascii_lowercase)
        random.shuffle(rdata)
        rdata = ''.join(rdata)
        return ' '.join([rdata[:random.randint(1, 9)] for _ in range(90)])

    def gen_email():
        rdata = list(string.ascii_lowercase)
        random.shuffle(rdata)
        rdata = ''.join(rdata)[:8]
        return rdata

    for _ in range(10):
        email = gen_email()
        new_user = {
            'email': 'user_' + email + '@test.pl',
            'password': 'test_1',
            'img': '0000000001.jpg',
            'description': text(),
            'motivation': text(),
            'what_can_you_bring': 'ciasteczka',
            'experience': text(),
            'mentor': False,
            'active': True,
            'organiser': False,
            'admin': False,
            'name': email[:8],
            'surname': email[9:],
            'linkedin': 'https://www.linkedin.com/in/' + email,
            'twitter': 'https://twitter.com/' + email,
            'facebook': 'https://www.facebook.com/' + email,
        }
        tbl = models.Users(**new_user)
        await tbl.create()
    print('Created 10 users in ' + str(datetime.utcnow() - start))


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
    color_print('Admin Created', color='green')


async def add_question(verbose=False):
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
        answers=['class', 'def', 'function', 'return'],
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
        answers=['finally', 'cancel', 'break', 'continue'],
        qtype='abcd'
    ).create()
    await models.Question(
        question=' Czy python jest językiem obiektowym  ?',
        qtype='bool'
    ).create()
    await models.Question(
        question='które polecenie NIE zwróci listy: data = [(9,0), (1,2),(3,4)]',
        answers=[
            "sorted(data, key=lambda a: a[0], reverse=False)",
            "max(data, key=lambda a: max(a))",
            "filter(lambda a: sum(a) >5, data)",
            "min(data, key=lambda a: max(a))",
        ],
        qtype='abcd'
    ).create()
    await models.Question(
        question='Co zwróci to polecenie: data = [(9,0), (1,2),(3,4), (7,5)] print(min(data, key=lambda a: max(a)))',
        answers=[
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
        answers=[
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
        answers=['DG', 'PYTHON', 'DJANGO', 'pusty string'],
        qtype='abcd',
    ).create()
    await models.Question(
        question='Jak wydobyć cyfrę 0? a = [1, 2, [7, 8, 9], 3, [4, 6, [1, 0]]]',
        answers=['a[5][3][2]', 'a[6][1]', 'a[4][2][1]', 'a[9]'],
        qtype='abcd',
    ).create()
    await models.Question(
        question='Jaka jest poprawna składnia: a = "aBcDeF"',
        answers=['a.upper()', 'upper(a)', 'a(upper)', 'a.upper'],
        qtype='abcd',
    ).create()
    await models.Question(
        question='Co zostanie wypisane do konsoli ?',
        answers=[
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
        answers=['["a"]', '["b"]', '["c"]', '["z"]'],
        qtype='abcd',
    ).create()
    await models.Question(
        question='Czy ten bląd zostanie dobrze obsłużony ?',
        qtype='bool',
        img='26',
    ).create()
    await models.Question(
        question='Która składnia jest niepoprawna ?',
        answers=[
            'import random',
            'from random import random',
            'from random import randint',
            'import randint'
        ],
        qtype='abcd',
    ).create()
    await models.Question(
        question='Jeżeli chcemy dopisać do pliku, nie nadpisując jego zawartości, użyjemy ?',
        answers=[
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


HEADER = """
<link rel="stylesheet" href="css/codehilite.css">
<div class="container">
    <div class="row">
        <div class="col-lg-12">
"""

FOOTER = """
        </div>
    </div>
    <exercises></exercises>
</div>
"""


class GlobalCounter:
    added_lessons = 0
    updated_lessons = 0
    error_lessons = 0


class LessonCounter:
    lesson_outcome = ''
    lesson_imgs_done = 0
    lesson_imgs_errors = 0
    quiz_outcome = ''
    quiz_details_done = 0
    quiz_details_error = 0
    exercise_outcome = ''
    exercise_details_created = 0
    exercise_details_updated = 0
    exercise_details_error = 0

    def __str__(self):
        return """Lesson: {}
    Images:
        Done: {}
        Errors: {}
Quiz: {}
    Done: {}
    Errors: {}
Exercises: {}
    Created: {}
    Updated: {}
    Errors: {}
        """.format(
            self.lesson_outcome,
            self.lesson_imgs_done,
            self.lesson_imgs_errors,
            self.quiz_outcome,
            self.quiz_details_done,
            self.quiz_details_error,
            self.exercise_outcome,
            self.exercise_details_created,
            self.exercise_details_updated,
            self.exercise_details_error,
        )


async def create_html_lessons(lang='pl', lesson=None, verbose=False):
    counter = GlobalCounter()

    async def process(a_dir, lang=lang):
        less_counter = LessonCounter()
        if a_dir.startswith('.') or a_dir.startswith('_'):
            return
        path = os.path.abspath('lesson_source/{}'.format(a_dir)) + '/'
        images = path + 'images'
        path += lang
        l_path = path + '.md'
        e_path = path + '.exercises'
        m_path = path + '.meta'
        q_path = path + '.quiz'
        try:  # lesson generation will BE detracted
            with open(l_path) as file:
                html = markdown.markdown(
                    file.read(),
                    extensions=[
                        'markdown.extensions.codehilite',
                        'markdown.extensions.tables'
                    ]
                )
        except FileNotFoundError:
            return
        with open('static/lessons/{}.html'.format(a_dir), 'w') as file:
            file.write(HEADER + html + FOOTER)
        with open(m_path) as file:
            meta = yaml.load(file.read())
        meta['author'] = DEFAULT_USER
        meta['file'] = '{}.html'.format(a_dir)
        meta['lesson_no'] = int(a_dir)
        try:
            with open(q_path) as file:
                questions = yaml.load(file.read())
            less_counter.quiz_outcome = 'found'
        except Exception as err:
            questions = False
            less_counter.quiz_outcome = 'none'
        if questions:
            quiz = models.Quiz(title=meta['title'], users=DEFAULT_USER, description=meta['description'])
            quiz_id = await quiz.update_or_create('title')
            meta['quiz'] = quiz_id
            question_order = 1
            for _, val in questions.items():
                try:
                    question = models.Question(**val)
                    qid = await question.update_or_create(*val.keys())
                    qq = models.QuizQuestions(quiz=quiz_id, question=qid, question_order=question_order)
                    question_order += 1
                    await qq.update_or_create('question', 'quiz')
                    less_counter.quiz_details_done += 1
                except Exception as err:
                    print(err)
                    less_counter.quiz_details_error += 1
        try:
            lesson = models.Lesson(**meta)
            lid, updated = await lesson.update_or_create('lesson_no', verbose=True)
            less_counter.lesson_outcome = 'found'
            if updated:
                less_counter.lesson_outcome = 'updated'
                counter.updated_lessons += 1
            else:
                less_counter.lesson_outcome = 'created'
                counter.added_lessons += 1
        except Exception as err:
            print(err)
            less_counter.lesson_outcome += 'error'
            counter.error_lessons += 1
        try:
            with open(e_path) as file:
                exe = yaml.load(file)
                less_counter.exercise_outcome = 'found'
        except Exception as err:
            exe = False
            less_counter.exercise_outcome = 'not found'
            print(err)
        if exe:
            try:
                for val in exe.values():
                    exercise = models.Exercise(lesson=lid, **val)
                    id, updated = await exercise.update_or_create(*val.keys(), verbose=True)
                    if updated:
                        less_counter.exercise_details_updated += 1
                    else:
                        less_counter.exercise_details_created += 1
            except Exception as err:
                print('error creating exercise')
                less_counter.exercise_details_error += 1
                print(exe)
                print(err)
        dest = os.path.abspath('static/images/')
        if os.path.exists(images):
            for file in os.listdir(images):
                src = os.path.join(images, file)
                if os.path.isfile(src):
                    dst = dest + '/' + file
                    shutil.copy(src, dst)
                    less_counter.lesson_imgs_done += 1
                else:
                    less_counter.lesson_imgs_errors += 1
        return less_counter

    async def inner_process(a_lesson):
        try:
            resp = await process(a_lesson)
            color_print(a_lesson, color='green')
            if verbose:
                print(resp)
            return resp
        except Exception as err:
            print(err)
            color_print(a_lesson, color='red')
        return False

    color_print('Processing lessons', color='blue')
    if lesson:
        await inner_process(lesson)
    else:
        for a_dir in os.listdir("./lesson_source/"):
            inner_process(a_dir)
    color_print('Processing lessons ---> Done', color='blue')
    color_print('ADDED: ', counter.added_lessons, color='green')
    color_print('UPDATED: ', counter.updated_lessons, color='yellow')
    color_print('ERRORS: ', counter.error_lessons, color='red')


def get_parser():
    a_parser = argparse.ArgumentParser()
    a_parser.add_argument("-l", "--lesson", help="Add lesson with given id, example: --lesson 0024")
    a_parser.add_argument("-v", "--verbose", help="Verbose mode", action="store_true")
    a_parser.add_argument("--alllessons", help="Add all lessons", action="store_true")
    a_parser.add_argument("--addquestion", help="Add all question", action="store_true")
    a_parser.add_argument("--bootstrap", help="Bootstrap the DB", action="store_true")
    a_parser.add_argument("--admin", help="Create admin account in the DB", action="store_true")
    a_parser.add_argument(
        "--devusers",
        help="Generate 10 user accounts for development purposes in the DB",
        action="store_true"
    )
    return a_parser


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    parser = get_parser()
    args = parser.parse_args()
    if args.devusers:
        loop.run_until_complete(gen_users())
    if args.bootstrap:
        loop.run_until_complete(bootstrap_db())
        ans = input('Have You seen any errors (red) - y/n ')
        if ans.lower() == 'y':
            loop.run_until_complete(bootstrap_db())
    if args.lesson:
        loop.run_until_complete(create_html_lessons(lesson=args.lesson, verbose=args.verbose))
    if args.alllessons:
        loop.run_until_complete(create_html_lessons(verbose=args.verbose))
    if args.addquestion:
        loop.run_until_complete(add_question(verbose=args.verbose))
    if args.admin:
        loop.run_until_complete(admin())
    loop.close()
    color_print('ALL Done', color='green')

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
from orm import UniqueViolationError

from config import DEFAULT_USER
from utils import color_print


cls_to_skip = ('CommonTestTemplate', 'CommonTestQuestion', 'CommonTestAnswer', 'CommonTestStatus')

LESSON_COUNTER = """
Lesson: {}
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
        return LESSON_COUNTER.format(
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


async def add_question(qpath="./bootstrap_data/questions.question", verbose=False):
    try:
        with open(qpath) as file:
            questions = yaml.load(file.read())
    except (FileNotFoundError, FileExistsError):
        color_print('No questions found')
        return
    except Exception as err:
        print(err)
        color_print('Issue with reading questions data')
        return
    for _, val in questions.items():
        try:
            question = models.Question(**val)
            await question.update_or_create('question')
        except Exception as err:
            if UniqueViolationError:
                color_print('question already existed', color='blue')
                continue
            print(err)
            return
    color_print('Created {} questions'.format(len(questions)), color='green')


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
        try:  # lesson generation will be deprecated in future
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
                    id, updated = await exercise.update_or_create('title', verbose=True)
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


async def add_exam(e_path, verbose=False):
    print(verbose)
    try:
        with open(e_path) as file:
            meta = yaml.load(file.read())
        questions = meta['questions']
        del meta['questions']
    except (FileNotFoundError, FileExistsError):
        color_print('No exam found')
        return
    except Exception as err:
        print(err)
        color_print('Issue with reading exam data')
        return
    exam = models.Exam(title=meta['title'], users=DEFAULT_USER, description=meta['description'])
    exam = await exam.update_or_create('title', get_insta=True)
    question_order = 1
    for _, val in questions.items():
        try:
            question = models.Question(**val)
            qid = await question.update_or_create('question')
            await exam.add_question(question_id=qid, order=question_order)
            question_order += 1
        except Exception as err:
            if UniqueViolationError:
                color_print('question already existed', color='blue')
                continue
            print(err)
            return
    color_print('Exam id: {} added with {} questions'.format(exam.id, len(questions)), color='green')


def get_parser():
    a_parser = argparse.ArgumentParser()
    a_parser.add_argument("-l", "--lesson", help="Add lesson with given id, example: --lesson 0024")
    a_parser.add_argument("-e", "--exam", help="Add exam from path")
    a_parser.add_argument("-q", "--questions", help="Add questions from path")
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
    if args.exam:
        loop.run_until_complete(add_exam(args.exam, verbose=args.verbose))
    if args.questions:
        loop.run_until_complete(add_question(args.questions, verbose=args.verbose))
    if args.alllessons:
        loop.run_until_complete(create_html_lessons(verbose=args.verbose))
    if args.addquestion:
        loop.run_until_complete(add_question(verbose=args.verbose))
    if args.admin:
        loop.run_until_complete(admin())
    loop.close()
    color_print('ALL Done', color='green')

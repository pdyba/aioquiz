# !/usr/bin/python3.5
from collections import namedtuple

question = namedtuple('question', ['qid', 'question', 'answares', 'qtype'])


class Quiz:
    question_1 = question(1, 'Jakie rozszerzenie zwyczajową mają pliki z kodem Pythonowym ?', [], 'plain')
    question_2 = question(2, 'Które słowo kluczowe nie występuje w pythonie ?', ['finally', 'cancel', 'break', 'continue'], 'abcd')
    question_3 = question(3, ' Czy python jest językiem obiektowym  ?', [], 'bool')
    # question_4 = question(4, ' Czy python jest językiem obiektowym  ?', [], 'bool')

    question_fin = question(999, ' To juz wszystko ! ', [], 'end')

    async def get(self, quid):
        return getattr(self, 'question_{}'.format(quid), self.question_fin)

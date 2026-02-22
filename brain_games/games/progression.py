import random

RULES = 'What number is missing in the progression?'


def get_question_and_answer():
    length_of_p = random.randint(5, 10)
    items = []
    item = random.randint(1, 100)
    step = random.randint(1, 9)
    i = 0
    while i < length_of_p:
        items.append(item)
        item += step
        i += 1
    threedots = random.randint(0, (length_of_p - 1))
    correct = items[threedots]
    items[threedots] = '..'
    result = ' '.join(str(x) for x in items)
    return result, str(correct)

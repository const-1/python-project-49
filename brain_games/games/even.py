# brain-even logic
#
#
import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    number = random.randint(1, 100) # NOSONAR
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return str(number), correct_answer


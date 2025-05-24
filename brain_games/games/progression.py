# brain games: progression logic
#
#
import random


DESCRIPTION = "What number is missing in the progression?"


def generate_progression(start: int, step: int, length: int) -> list:
    return [str(start + i * step) for i in range(length)]


def generate_round():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    length = random.randint(5, 15)
    progression = generate_progression(start, step, length)

    hidden_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."

    question = " ".join(progression)
    return question, correct_answer

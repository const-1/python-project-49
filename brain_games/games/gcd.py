# brain games: greatest common divisor logic
#
#
import random


DESCRIPTION = "Find the greatest common divisor of given numbers."


def find_gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def generate_round():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = str(find_gcd(num1, num2))
    question = f"{num1} {num2}"
    return question, correct_answer

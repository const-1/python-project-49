# brain games: prime number logic
#
#
import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_round():
    number = random.randint(2, 100)  # Generate number from 2 to 100
    correct_answer = "yes" if is_prime(number) else "no"
    return str(number), correct_answer

# brain games: calculation logic
#
#
import random


DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    a = random.randint(1, 100)    # NOSONAR
    b = random.randint(1, 100)    # NOSONAR
    operation = random.choice(["+", "-", "*"])   # NOSONAR
    
    match operation:
        case "+":
            correct_answer = a + b
        case "-":
            correct_answer = a - b
        case "*":
            correct_answer = a * b
        case _:
            raise ValueError("Invalid operation")
    
    return f"{a} {operation} {b}", str(correct_answer)


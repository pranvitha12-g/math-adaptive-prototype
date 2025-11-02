import random

def generate_puzzle(level):
    if level == 'Easy':
        a, b = random.randint(1, 10), random.randint(1, 10)
        op = random.choice(['+', '-'])
    elif level == 'Medium':
        a, b = random.randint(10, 50), random.randint(1, 20)
        op = random.choice(['+', '-', '*'])
    else:  # Hard
        a, b = random.randint(20, 100), random.randint(2, 10)
        op = random.choice(['*', '/'])

    question = f"{a} {op} {b}"
    try:
        answer = eval(question)
    except ZeroDivisionError:
        return generate_puzzle(level)
    return question, round(answer, 2)

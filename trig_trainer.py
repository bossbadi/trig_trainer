import random
import requests

PROBLEMS = """
sin(0 deg)
sin(30 deg)
sin(60 deg)
sin(90 deg)
sin(120 deg)
sin(135 deg)
sin(150 deg)
sin(180 deg)
sin(210 deg)
sin(225 deg)
sin(240 deg)
sin(270 deg)
sin(300 deg)
sin(315 deg)
sin(330 deg)
sin(360 deg)
cos(0 deg)
cos(30 deg)
cos(60 deg)
cos(90 deg)
cos(120 deg)
cos(135 deg)
cos(150 deg)
cos(180 deg)
cos(210 deg)
cos(225 deg)
cos(240 deg)
cos(270 deg)
cos(300 deg)
cos(315 deg)
cos(330 deg)
cos(360 deg)
tan(0 deg)
tan(30 deg)
tan(60 deg)
tan(90 deg)
tan(120 deg)
tan(135 deg)
tan(150 deg)
tan(180 deg)
tan(210 deg)
tan(225 deg)
tan(240 deg)
tan(270 deg)
tan(300 deg)
tan(315 deg)
tan(330 deg)
tan(360 deg)
sec(0 deg)
sec(30 deg)
sec(60 deg)
sec(90 deg)
sec(120 deg)
sec(135 deg)
sec(150 deg)
sec(180 deg)
sec(210 deg)
sec(225 deg)
sec(240 deg)
sec(270 deg)
sec(300 deg)
sec(315 deg)
sec(330 deg)
sec(360 deg)
csc(0 deg)
csc(30 deg)
csc(60 deg)
csc(90 deg)
csc(120 deg)
csc(135 deg)
csc(150 deg)
csc(180 deg)
csc(210 deg)
csc(225 deg)
csc(240 deg)
csc(270 deg)
csc(300 deg)
csc(315 deg)
csc(330 deg)
csc(360 deg)
sin(-30 deg)
sin(-60 deg)
sin(-90 deg)
sin(-120 deg)
sin(-135 deg)
sin(-150 deg)
sin(-180 deg)
sin(-210 deg)
sin(-225 deg)
sin(-240 deg)
sin(-270 deg)
sin(-300 deg)
sin(-315 deg)
sin(-330 deg)
sin(-360 deg)
cos(-30 deg)
cos(-60 deg)
cos(-90 deg)
cos(-120 deg)
cos(-135 deg)
cos(-150 deg)
cos(-180 deg)
cos(-210 deg)
cos(-225 deg)
cos(-240 deg)
cos(-270 deg)
cos(-300 deg)
cos(-315 deg)
cos(-330 deg)
cos(-360 deg)
tan(-30 deg)
tan(-60 deg)
tan(-90 deg)
tan(-120 deg)
tan(-135 deg)
tan(-150 deg)
tan(-180 deg)
tan(-210 deg)
tan(-225 deg)
tan(-240 deg)
tan(-270 deg)
tan(-300 deg)
tan(-315 deg)
tan(-330 deg)
tan(-360 deg)
sec(-30 deg)
sec(-60 deg)
sec(-90 deg)
sec(-120 deg)
sec(-135 deg)
sec(-150 deg)
sec(-180 deg)
sec(-210 deg)
sec(-225 deg)
sec(-240 deg)
sec(-270 deg)
sec(-300 deg)
sec(-315 deg)
sec(-330 deg)
sec(-360 deg)
csc(-30 deg)
csc(-60 deg)
csc(-90 deg)
csc(-120 deg)
csc(-135 deg)
csc(-150 deg)
csc(-180 deg)
csc(-210 deg)
csc(-225 deg)
csc(-240 deg)
csc(-270 deg)
csc(-300 deg)
csc(-315 deg)
csc(-330 deg)
csc(-360 deg)
sin(0)
sin(pi/6)
sin(pi/4)
sin(pi/3)
sin(pi/2)
sin(2pi/3)
sin(3pi/4)
sin(5pi/6)
sin(pi)
sin(7pi/6)
sin(5pi/4)
sin(4pi/3)
sin(3pi/2)
sin(5pi/3)
sin(7pi/4)
sin(11pi/6)
cos(0)
cos(pi/6)
cos(pi/4)
cos(pi/3)
cos(pi/2)
cos(2pi/3)
cos(3pi/4)
cos(5pi/6)
cos(pi)
cos(7pi/6)
cos(5pi/4)
cos(4pi/3)
cos(3pi/2)
cos(5pi/3)
cos(7pi/4)
cos(11pi/6)
tan(0)
tan(pi/6)
tan(pi/4)
tan(pi/3)
tan(pi/2)
tan(2pi/3)
tan(3pi/4)
tan(5pi/6)
tan(pi)
tan(7pi/6)
tan(5pi/4)
tan(4pi/3)
tan(3pi/2)
tan(5pi/3)
tan(7pi/4)
tan(11pi/6)
sec(0)
sec(pi/6)
sec(pi/4)
sec(pi/3)
sec(pi/2)
sec(2pi/3)
sec(3pi/4)
sec(5pi/6)
sec(pi)
sec(7pi/6)
sec(5pi/4)
sec(4pi/3)
sec(3pi/2)
sec(5pi/3)
sec(7pi/4)
sec(11pi/6)
csc(0)
csc(pi/6)
csc(pi/4)
csc(pi/3)
csc(pi/2)
csc(2pi/3)
csc(3pi/4)
csc(5pi/6)
csc(pi)
csc(7pi/6)
csc(5pi/4)
csc(4pi/3)
csc(3pi/2)
csc(5pi/3)
csc(7pi/4)
csc(11pi/6)
cot(0)
cot(pi/6)
cot(pi/4)
cot(pi/3)
cot(pi/2)
cot(2pi/3)
cot(3pi/4)
cot(5pi/6)
cot(pi)
cot(7pi/6)
cot(5pi/4)
cot(4pi/3)
cot(3pi/2)
cot(5pi/3)
cot(7pi/4)
cot(11pi/6)
sin(-pi/6)
sin(-pi/4)
sin(-pi/3)
sin(-pi/2)
sin(-2pi/3)
sin(-3pi/4)
sin(-5pi/6)
sin(-pi)
sin(-7pi/6)
sin(-5pi/4)
sin(-4pi/3)
sin(-3pi/2)
sin(-5pi/3)
sin(-7pi/4)
sin(-11pi/6)
cos(-pi/6)
cos(-pi/4)
cos(-pi/3)
cos(-pi/2)
cos(-2pi/3)
cos(-3pi/4)
cos(-5pi/6)
cos(-pi)
cos(-7pi/6)
cos(-5pi/4)
cos(-4pi/3)
cos(-3pi/2)
cos(-5pi/3)
cos(-7pi/4)
cos(-11pi/6)
tan(-pi/6)
tan(-pi/4)
tan(-pi/3)
tan(-pi/2)
tan(-2pi/3)
tan(-3pi/4)
tan(-5pi/6)
tan(-pi)
tan(-7pi/6)
tan(-5pi/4)
tan(-4pi/3)
tan(-3pi/2)
tan(-5pi/3)
tan(-7pi/4)
tan(-11pi/6)
sec(-pi/6)
sec(-pi/4)
sec(-pi/3)
sec(-pi/2)
sec(-2pi/3)
sec(-3pi/4)
sec(-5pi/6)
sec(-pi)
sec(-7pi/6)
sec(-5pi/4)
sec(-4pi/3)
sec(-3pi/2)
sec(-5pi/3)
sec(-7pi/4)
sec(-11pi/6)
csc(-pi/6)
csc(-pi/4)
csc(-pi/3)
csc(-pi/2)
csc(-2pi/3)
csc(-3pi/4)
csc(-5pi/6)
csc(-pi)
csc(-7pi/6)
csc(-5pi/4)
csc(-4pi/3)
csc(-3pi/2)
csc(-5pi/3)
csc(-7pi/4)
csc(-11pi/6)
cot(-pi/6)
cot(-pi/4)
cot(-pi/3)
cot(-pi/2)
cot(-2pi/3)
cot(-3pi/4)
cot(-5pi/6)
cot(-pi)
cot(-7pi/6)
cot(-5pi/4)
cot(-4pi/3)
cot(-3pi/2)
cot(-5pi/3)
cot(-7pi/4)
cot(-11pi/6)
"""

FILENAME = 'problems.txt'
API = 'https://api.mathjs.org/v4/?expr={}'
WELCOME = """
Welcome to Trig Trainer by bossbadi
√ is "sqrt()"
π is "pi"
Enter "quit" to quit"""


def check_answer(problem, answer):
    try:
        actual = requests.get(API.format(problem))
        answer = requests.get(API.format(answer))
        actual = round(float(actual.text), 2)
        answer = round(float(answer.text), 2)

        if actual == answer:
            print('correct')
        else:
            print("that's wrong idiot")
            print('The correct answer is', actual)
    except Exception:
        print('error')


problems = PROBLEMS.strip().split('\n')
print(WELCOME)

while True:
    print()
    problem = random.choice(problems)
    answer = input(problem + ' = ')

    if answer == 'quit':
        break
    else:
        check_answer(problem, answer)

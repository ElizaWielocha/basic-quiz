import os
import random
from question_base import question_promps

def clear():
    os.system( 'cls' )

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question(question_promps[0], 'b'),
    Question(question_promps[1], 'c'),
    Question(question_promps[2], 'a'),
    Question(question_promps[3], 'a'),
    Question(question_promps[4], 'b'),
    Question(question_promps[5], 'c'),
    Question(question_promps[6], 'b'),
    Question(question_promps[7], 'a'),
    Question(question_promps[8], 'c'),
    Question(question_promps[9], 'a'),
    Question(question_promps[10], 'c'),
    Question(question_promps[11], 'a'),
    Question(question_promps[12], 'b'),
    Question(question_promps[13], 'c')
]


def start_quiz(questions):
    print("LET'S START!")
    guesses = 0
    score = 0
    used = list()
    while guesses < len(questions):
        randomquest = random.choice(questions)
        if randomquest not in used:
            answer = input(randomquest.prompt)
            if answer == randomquest.answer:
                score = score + 1
            guesses = guesses + 1
            used.append(randomquest)
            clear()
    print("KONIEC!")
    print(f'Twoj wynik: {score}/{len(questions)}!')


score = start_quiz(questions)



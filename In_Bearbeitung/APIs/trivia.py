"""
First API Game, using Trivia API
20.03.2025
"""
import requests as re
import random
import html

print("Welcome to the Trivia Game!")
while True:
    try:
        amount = int(input("How many questions would you like to answer? "))
    except ValueError:
        print("Please enter a valid number")
        continue
    else:
        break


while True:
    try:
        difficulty = input("Please enter the difficulty level (easy, medium, hard): ")
        if difficulty not in ["easy", "medium", "hard"]:
            raise ValueError
    except ValueError:
        print("Please enter a valid difficulty level")
        continue
    else:
        break

while True:
    score = 0
    trivia = re.get(f"https://opentdb.com/api.php?amount={amount}&difficulty={difficulty}&type=multiple")

    #print(trivia.json())

    for i in range(amount):
        question = html.unescape(trivia.json()["results"][i]["question"])
        correct_answer = trivia.json()["results"][i]["correct_answer"]
        incorrect_answers = trivia.json()["results"][i]["incorrect_answers"]
        answers = incorrect_answers + [correct_answer]
        random.shuffle(answers)
        print(f"This question is of the category: {trivia.json()['results'][i]['category']}")
        print(f"Question {i+1}: {question}")
        for j in range(4):
            print(f"{j+1}: {html.unescape(answers[j])}")
        while True:
            try:
                answer = int(input("Please enter the number of the correct answer: "))
                if answer not in [1, 2, 3, 4]:
                    raise ValueError
            except ValueError:
                print("Please enter a valid number")
                continue
            else:
                break
        if answers[answer-1] == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect!\n The correct answer was: ", html.unescape(correct_answer), "\n")

    print(f"Your score is: {score}/{amount}")
    input("Press ENTER to continue...")
    while True:
        try:
            play_again = input("Would you like to play again? (yes/no): ")
            if play_again not in ["yes", "no", "y", "n"]:
                raise ValueError
        except ValueError:
            print("Please enter a valid answer")
            continue
        else:
            if play_again in ["yes", "y"]:
                break
            else:
                print("Thank you for playing!")
                exit()

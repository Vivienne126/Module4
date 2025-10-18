import requests
import random
import html

api_url="https://opentdb.com/api.php?amount=10&category=9&type=multiple"

def get_education_question():
    response=requests.get(api_url)
    if response.status_code==200:
        data=response.json()
        if data["response_code"]==0 and data["results"]:
            return data["results"]
    return None

def run_quiz():
    questions=get_education_question()
    if not questions:
        print("Failed to fetch education questions")
        return
    score=0
    print("Welcome to the educational quiz")
    for i,q in enumerate(questions , 1):
        #Decode HTML entities and provide options
        question=html.unescape(q["question"])
        correct=html.unescape(q["correct_answer"])
        incorrect=[html.unescape(a) for a in q["incorrect_answers"]]

        #Create and shuffle questions
        options=incorrect+[correct]
        random.shuffle(options)

        #Display questions
        print(f"Question{i} : {question}")
        for idx,option in enumerate(options,1):
            print(f"{idx}.{option}")
        #Get an validate answer
        while True:
            try:
                choice=int(input("Enter your answer between 1 to 4"))
                if 1<=choice<=4:
                    break
            except ValueError:
                pass
            print("Invalid input please enter between 1 to 4")

        #Check answer
        if options[choice-1]==correct:
            print("Correct")
            score=score+1
        else:
            print("Wrong answer")
        print(f"Final score is {score}")

run_quiz()

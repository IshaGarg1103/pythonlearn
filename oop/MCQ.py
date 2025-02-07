from Question import Question

question_prompts=["What are the colors of apples?\na) Red/Green\nb) Yellow\nc) Purple\n\n","What are the colors of banana?\na) Teal\nb) Magenta\nc) Yellow\n\n","What is the color of Strawberries?\na) Purple\nb) Red\nc) Green\n\n"]
questions=[
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"b")
]
def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score+=1
    print("You got "+str(score) + "/" + str(len(questions))+" correct")

run_test(questions)
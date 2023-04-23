from Question import Question

question_prompt = [
    "What color are apples?\n(a) Red\Green\t(b) Purple\t(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\t(b) Magenta\t(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\t(b) Red\t(c) Blue\n\n"
]
questions =[
    Question(question_prompt[0],"a" ),
    Question(question_prompt[1],"c"),
    Question(question_prompt[2],"b")

]
def run_test(questions):
    score =0
    for i in questions:
        answer = input(i.prompt)
        if answer == i.answer:
            score+= 1
    print("You got "+ str(score)+"/"+ str(len(questions))+ "correct")

run_test(questions)
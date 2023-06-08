from question import question


question_prompts = [
"what colour are apples?\n (a)green/red\n (b) purple\n (c)yellow\n\n",
"what colour is banana?\n (a)blue\n (b)yellow\n (c)magenta\n\n",
"what colour is the Nigerian flag?\n (a)bala blu\n (b)Bla bulu\n (c)green and white\n\n"
]

questions = [
       question( question_prompts[0], "a"),
       question( question_prompts[1], "b"),
       question( question_prompts[2], "c")
 ]
 
def run_test(questions):
      score = 0
      for question in questions:
            answer = input(question.prompt)
            if answer == question.answer:
             score += 1
             
      print("you got " + str(score) + "/" + str(len(questions)) + " correct"
      )
             
run_test(questions)
         
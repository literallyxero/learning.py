from main import AnonymousSurvey

#Make the question
question = "Best video game ever?"
survey = AnonymousSurvey(question)

#Shows the Question
survey.show_question()
print("Enter 'q' anytime to quit.")
while True:
    response = input("Answer: ")
    if response == "q":
        break
    survey.store_response(response)

#Show the results
survey.show_results()
print("Thank you for participating!")

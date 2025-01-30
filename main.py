score = 0
 
question = "what is the capital of ecuador?"
print(question)
user_answer = input("your answer: ")
score += 1
if user_answer.lower() == "quito":
    print("Correct!")
 
else:
    print("oops! the correct answer is quito")
print(f"your score is: {score}")
 
score = 0
 
question = "what is the capital of the USA?"
print(question)
user_answer = input("your answer: ")
score += 1
if user_answer.lower() == "dc":
    print("Correct!")
 
else:
    print("oops! the correct answer is dc")
print(f"your score is: {score}")
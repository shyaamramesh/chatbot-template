import random
import webbrowser
from random import randint

greetings = ['hello', 'hi']
random_greeting = random.choice(greetings)

question = ['whats your name','how are you']
responses = ['i dont have one',"I'm fine"]

task = ['open firefox', 'give me a random number']
run_code = ["webbrowser.open_new('https://www.google.com/')", "print(randint(0,100000))"]

while True:
	userInput = raw_input(">>> ")
	if userInput in greetings:
		print(random_greeting)
	elif userInput in question:
		print(responses[question.index(userInput)])
	elif userInput in task:
		exec(run_code[task.index(userInput)])
	else:
		print("I did not understand what you said")

# import necessary modules
import random

# define list of thrombosis symptoms
symptoms = ['pain or swelling in the leg', 'shortness of breath', 'chest pain or pressure', 'headache', 'dizziness or fainting']

# define list of thrombosis prevention tips
prevention_tips = ['maintain a healthy weight', 'exercise regularly', "don't smoke", 'drink alcohol in moderation', 'maintain a healthy diet']

# define list of false answers for symptoms
false_symptoms = ['cough', 'runny nose', 'sore throat', 'fever', 'nausea']

# define list of false answers for prevention tips
false_prevention_tips = ['take vitamin supplements', 'drink lots of water', 'get plenty of sleep', 'wash your hands frequently', 'avoid contact with sick people']

# define function to start game
def start_game():
  print("Welcome to the Thrombosis Awareness Game!")
  print("In this game, you will learn about thrombosis and how to prevent it.")
  print("You will be presented with a series of symptoms, and your task is to determine whether they are associated with thrombosis or not.")
  print("Let's get started!")

# define function to present symptom and ask for user input
def present_symptom(symptom):
  print("Symptom: " + symptom)
  response = input("Is this a symptom of thrombosis? (yes/no) ")
  if response.lower() == 'yes':
    if symptom in symptoms:
      print("Correct! This is a symptom of thrombosis.")
    else:
      print("Incorrect. This is not a symptom of thrombosis.")
  else:
    if symptom in false_symptoms:
      print("Correct! This is not a symptom of thrombosis.")
    else:
      print("Incorrect. This is a symptom of thrombosis.")

# define function to present prevention tip and ask for user input
def present_prevention_tip(prevention_tip):
  print("Prevention Tip: " + prevention_tip)
  response = input("Is this a way to prevent thrombosis? (yes/no) ")
  if response.lower() == 'yes':
    if prevention_tip in prevention_tips:
      print("Correct! This is a way to prevent thrombosis.")
    else:
      print("Incorrect. This is not a way to prevent thrombosis.")
  else:
    if prevention_tip in false_prevention_tips:
      print("Correct! This is not a way to prevent thrombosis.")
    else:
      print("Incorrect. This is a way to prevent thrombosis.")

# define main game loop
def play_game():
  while True:
    # randomly choose between presenting a symptom or prevention tip
    if random.choice([True, False]):
      # present a random symptom and ask for user input
      present_symptom(random.choice(symptoms + false_symptoms))
    else:
      # present a random prevention tip and ask for user input
      present_prevention_tip(random.choice(prevention_tips))
    # ask if user wants to play again
    response = input("Would you like to play again? (yes/no) ")
    if response.lower() == 'no':
      break

# start the game
start_game()
# start the main game loop
play_game()

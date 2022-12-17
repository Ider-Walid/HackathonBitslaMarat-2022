import tkinter as tk
from tkinter import Label
import random
import webbrowser

symptoms = ['pain or swelling in the leg', 'shortness of breath', 'chest pain or pressure', 'headache', 'dizziness or fainting', 'pain or tenderness in the abdomen', 'sudden coughing or coughing up blood', 'rapid or irregular heartbeat', 'vision changes', 'weakness or numbness on one side of the body']

prevention_tips = ['maintain a healthy weight', 'exercise regularly', "don't smoke", 'drink alcohol in moderation', 'maintain a healthy diet', 'avoid long periods of sitting or standing', 'wear graduated compression stockings', 'manage conditions that increase your risk of blood clots, such as diabetes, heart disease, or cancer', 'take blood thinners as prescribed by your doctor', 'avoid hormone therapy or use it at the lowest effective dose', 'consider prophylactic measures when traveling long distances or during extended periods of immobility', "don't use tobacco products", 'maintain a healthy blood pressure and cholesterol levels', 'get vaccinated against influenza and pneumococcal infections']

false_symptoms = ['cough', 'runny nose', 'sore throat', 'fever', 'nausea', 'back pain', 'constipation', 'diarrhea', 'fatigue', 'muscle aches']

false_prevention_tips = ['take vitamin supplements', 'drink lots of water', 'get plenty of sleep', 'wash your hands frequently', 'avoid contact with sick people', 'avoid stress', 'use natural remedies', 'drink herbal teas', 'use essential oils', 'avoid processed foods']


def open_link():
    webbrowser.open_new_tab('https://activatt.com/')


# define function to present symptom and ask for user input
def present_symptom(symptom):
    global correct_answer
    symptom_label.config(text="Symptom: " + symptom)
    yes_button.config(state='normal')
    no_button.config(state='normal')
    if symptom in symptoms:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

def present_prevention_tip(prevention_tip):
    global correct_answer
    symptom_label.config(text="Prevention Tip: " + prevention_tip)
    yes_button.config(state='normal')
    no_button.config(state='normal')
    if prevention_tip in prevention_tips:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'


score = 0

def check_answer(user_answer):
  global score  # make sure to use the global score variable
  if user_answer == correct_answer:
    result_label.config(text='Correct!', fg='green')
    score += 100  # increment the score by 100 for correct answers
  else:
    result_label.config(text='Incorrect.', fg='red')
    score -= 50  # decrement the score by 20 for incorrect answers
  # update the score label with the current score
  score_label.config(text='Score: ' + str(score))
  # check if the score has reached 1000 and display the "Congratulations" message if it has
  if score >= 1000:
    result_label.config(text='Congratulations, you are now an expert!')
  # disable yes and no buttons
  yes_button.config(state='disabled')
  no_button.config(state='disabled')
  # schedule a callback function to click the "Start the game" button after 5 seconds
  if score <1000:
    root.after(2000, start_button.invoke)
  # exit the loop if the user clicks 'No'
  while 1:
      if user_answer == 'no' or user_answer=="yes":
        break




# define main game loop
def play_game():
    global stop_game
    result_label.config(text='')  # reset result label text
    questions_asked = 0
    max_questions = 5  # modify this to control the number of questions asked
    while questions_asked < max_questions:
    # randomly choose between presenting a symptom or prevention tip
        if random.choice([True, False]):
          # present a random symptom and ask for user input
            present_symptom(random.choice(symptoms + false_symptoms))
        else:
          # present a random prevention tip and ask for user input
            present_prevention_tip(random.choice(prevention_tips))
        questions_asked += 1

def stop_game():
    root.destroy()



# create main window
root = tk.Tk()
root.title('Thrombosis Awareness Game')
root.geometry("1200x200")
root.resizable(False, False)


# create start game button
start_button = tk.Button(root, text='Start the game', command=play_game)
start_button.pack()

# create stop game button
stop_button = tk.Button(root, text='Stop the game', command=root.destroy)
stop_button.pack()

# create label to display symptom or prevention tip
symptom_label =Label(root, text='', font=('Arial', 20))
symptom_label.pack()



#Link button
link_button = tk.Button(root, text="Learn more about the Activita'TT Association", command=open_link)
link_button.pack(side='bottom')


# create label to display the score
score_label = tk.Label(root, text='Score: 0', font=('Arial', 16))
score_label.pack()

# create yes and no buttons
yes_button = tk.Button(root, text='Yes', command=lambda: (check_answer('yes'), stop_game), state='disabled')
yes_button.pack(side='left')
no_button = tk.Button(root, text='No', command=lambda: (check_answer('no'), stop_game), state='disabled')
no_button.pack(side='right')

yes_button.config(fg='green')
no_button.config(fg='red')
start_button.config(fg='blue', bg='black')


# create label to display result
result_label = tk.Label(root, text='', font=('Arial', 20))
result_label.pack()

# start the main loop
root.mainloop()

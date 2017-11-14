from random import choice
from time import sleep

state_capitals = {
    'Afghanistan': 'Kabul',
    'Albania': 'Tirana',
    'Algeria': 'Algiers',
    'Australia': 'Canberra',
    'Bahrain': 'Manama',
    'Bangladesh': 'Dhaka',
    'Belgium': 'Brussels',
    'Bhutan': 'Thimphu',
    'Bulgaria': 'Sofia',
    'Chile': 'Santiago',
    'China': 'Beijing',
    'Pakistan': 'Islamabad',
    'Iran': 'Tehran',
    'Iraq': 'Baghdad',
    'Libya': 'Tripoli',
    'Malaysia': 'Kualalumpur',
    'NewZealand': 'Wellington',
    'India': 'New delhi',
    'Panama': 'Panama city',
    'Qatar': 'Doha',
    'Saudi Arabia': 'Riyadh',
    'Syria': 'Damascus',
    'Japan': 'Tokyo'

}

states = list(state_capitals.keys())
score = 0
correct_ans = 0
wrong = 0
for state in states:
    state = choice(states)
    print("What is the capital of " + state + " ?")
    user_input = str(input()).capitalize()

    if state_capitals[state] == user_input:
        print("Correct! Great job ")
        score += 5
        correct_ans += 1
    else:
        print("Incorrect  The capital of " + state + " was " + state_capitals[state])
        wrong += 1

print("Quiz Completed plz Wait for the Result")
sleep(2)
print("\n--------------------")
sleep(1)
print("Total Questions were asked: " + str(len(states)))
print("Correct Answers: ", correct_ans)
print("Wrong Answers: ", wrong)
print("Total Score: ", score)
print("--------------------")


# SAME PROGRAM WITH WHILE LOOP

# q = 0
#
# while q < len(states):
#     qst = random.choice(states)
#     print("What is the capital of " + qst + " ?")
#     user_input = str(input()).capitalize()
#     if state_capitals[qst] == user_input:
#         print("Correct! ")
#         score += 5
#
#     else:
#         print("Sorry  The Answer was " + state_capitals[qst])
#     q += 1

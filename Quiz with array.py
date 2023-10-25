'''
---------------
A Quiz Program
---------------

Specification:
1) Ask the user for their name and use that in showing the score 
2) The quiz has 5 questions
3) Each question must be asked until either it is correct or the user has had three attempts
4) A score must be kept and displayed at the end (You may also display the score so far as you are going through the quiz)
'''

# 1) Get the users's name & store it

userName=input("What is your name? ")

# 2) Create the questions

'''
Set up an array of questions and an array of answers, or a two dimensional array
'''
questions=[["France", "Paris"],["Spain","Madrid"],["UK","London"],["USA","Washington"],["Russia","Moscow"]]

#3) Loop though the questions:

score=0

for i in range (0,5):
    continueLoop="Yes"
    correct="No"
    askQuestionCount=0
    while continueLoop=="Yes":
        if askQuestionCount>=3:
            print("You've had all your chances")
            continueLoop="No"
        else:
            answer=input("what is the capital of " + questions[i][0]+"? ")
            if answer==questions[i][1]:
                print("Correct")
                score+=1
                correct="Yes"
                continueLoop="No"
            else:
                print ("Sorry you got that wrong")
                askQuestionCount+=1
'''

# 4) Print final score

'''
print(userName + ", your final score is " + str(score) + "/5")



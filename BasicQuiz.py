''' A Basic Quiz '''

# Initialise variables
score=0

# Question 1
question1="What is the capital of France? "
answer1="Paris"
yourAnswer1=input(question1)
if yourAnswer1==answer1:
         print("Correct")
         score+=1
else:
         print("Sorry you got that wrong, the answer is " + answer1)

# Question 2
question2="What is the capital of Spain? "
answer2="Madrid"
yourAnswer2=input(question2)
if yourAnswer2==answer2:
         print("Correct")
         score+=1
else:
         print("Sorry you got that wrong, the answer is " + answer2)

# Question 3
''' Copy and paste the code from question 1 and
then alter variables and questions/answer pairs
to contain Q3 information etc.'''

# Question 4
''' Copy and paste the code from question 1 and
then alter variables and questions/answer pairs
to contain Q3 information etc.'''

# Question 5
''' Copy and paste the code from question 1 and
then alter variables and questions/answer pairs
to contain Q3 information etc.'''

# Show final Score

print("You got " + str(score) + "/5)")

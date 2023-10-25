# Set up Global Variables
number1=0
number2=0
operator=""

# Functions
def plus(num1, num2):
         return num1+num2
def minus():
         answer=number1-number2
         print(answer)
def times():
         answer=number1*number2
         print(answer)
def divide():
         answer=number1/number2
         print(answer)
         
# Main loop

continueThis="Y"
while continueThis=="Y":
         menuChoice=input("What do you want to do, new Calculation (N) or Quit (Q)? ")
         if menuChoice=="N":
                  number1=float(input("Give me a number "))
                  number2=float(input("Give me another number "))
                  operator=input("Give me an operator (+, - * or / ")
                  if operator=="+":
                           add()
                  elif operator=="-":
                           minus()
                  elif operator=="*":
                           times()
                  elif operator=="/":
                           divide()
                  else:
                           print("invalid operator")

         else:
              print("OK, Goodbye")
              continueThis="N"    

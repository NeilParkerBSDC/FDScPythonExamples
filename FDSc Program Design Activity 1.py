'''
Specification
I want a command line Calculation program that:

1) Starts with the following menu items “What do you want to do, display a Times table (T),Do An Arithmetic Calculation (A) , Convert a measurement (C) or Quit (Q)
2) If T is chosen the program asks “What times table do you want to produce”, you enter a number and it shows you the times table
3) If  A is chosen  the programs asks you to enter 2 numbers and an operator, it then does the requested calculation
4) If C is chosen you are given a further choice of conversions (e.g. mass (lb to Kg etc.), length (feet to meters etc.)
5) If Q is selected the program says “goodbye” and closes down
'''

# Set up Global Variables
''' This is not really needed for this program'''
number1=0
number2=0
operator=""

# Functions

# Time Table Function
def TimesTable():
         TT = input("Which times table do you want to show? ")
         for i in range (1,13):
                  answer=i*int(TT)
                  print(str(i) +" times " + TT +" = " + str(answer))

# Caluclation Function


def plus(No1,No2):
         answer=No1+No2
         return(answer)
def minus(No1,No2):
         answer=No1-No2
         return(answer)
def times(No1,No2):
         answer=No1*No2
         return(answer)
def divide(No1,No2):
         answer=No1/No2
         return(answer)
         
def Calc():

         number1=float(input("Give me a number "))
         number2=float(input("Give me another number "))
         operator=input("Give me an operator (+, - * or / ) ")
         if operator=="+":
                  print(plus(number1,number2))
         elif operator=="-":
                  print(minus(number1,number2))
         elif operator=="*":
                  print(times(number1,number2))
         elif operator=="/":
                  print(divide(number1,number2))
         else:
                  print("invalid operator")

# Conversion Function

def mileToKM(miles):
         km=miles*1.6
         return km

def KMToMile(km):
         miles=km*0.62
         return miles

def Convert():
         whichConv=input("Which conversion do you want to do? Miles to KM (M) or KM to Miles (K)? ")
         if whichConv==("M"):
                  distance=float(input("How many miles? "))
                  print(str(distance) + " is " + str(mileToKM(distance)) + " KM ")
         elif whichConv==("K"):
                  distance=float(input("How many KM? "))
                  print(str(distance) + " is " + str(KMToMile(distance)) + " Miles ")
                  

# Main Loop

continueThis="Y"
while continueThis=="Y":
         menuChoice=input("What do you want to do, display a Times table (T),Do An Arithmetic Calculation (A) , Convert a measurement (C) or Quit (Q) ")
         if menuChoice=="T":
                  TimesTable()
         elif menuChoice=="A":
                  Calc()
         elif menuChoice=="C":
                  Convert()
         elif menuChoice=="Q":
                  #print("OK, Goodbye!")
                  continueThis="N"
         else:
                  print("You have not entered a valid menu choice - enter T, A, C or Q")

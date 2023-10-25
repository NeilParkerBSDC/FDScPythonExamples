'''
===========================================================================
Task 3
The authorities have a file of known vehicle registrations and the vehicle’s owner.
Those vehicles with standard registrations can be looked up in this file and a
fine automatically sent out. A new file is created by comparing the information
from the average speed recording system with the file of registered vehicles and
their owners’ details. This new file should include the owner’s name and address
details, the registration of the vehicle and the average speed of the vehicle in
the section of road.

Analyse the requirements for this system and design, develop, test and evaluate
a program for creating a file of details for vehicles exceeding the speed limit
set for a section of road. You will need to create a suitable file with test
data, including standard registrations and vehicle owner information.
===========================================================================
'''
#Import Libraries
import random
import csv

#Initialise variables
Registrations=[]
Owners=[]
MakeOfVehicleList=[]
ModelOfVehicleList=[]
Addresses=[]

#Step 1: Create a CSV file with standard registrations and car ownership details (the 'Global List')
#           This should have the following fields: Registration, Owner, Make of Vehicle, Address
#           see e.g. http://www.generatedata.com/ for automatically generated dummy data

#Step 2: Get details from the 'Global List'

with open('GlobalList.csv', newline='') as csvfile:
    GlobalList = csv.reader(csvfile, delimiter=',', quotechar='"')
    # pull off the details for each record in the CSV file and assign to a variable
    for EachReg in GlobalList:
        Registration=EachReg[0]
        Owner=EachReg[1]
        MakeOfVehicle=EachReg[2]
        ModelOfVehicle=EachReg[3]
        Address=EachReg[4]
        #print(Owner)
        # Create lists for each 'field' in the CSV file
        Registrations.append(Registration)
        Owners.append(Owner)
        MakeOfVehicleList.append(MakeOfVehicle)
        ModelOfVehicleList.append(ModelOfVehicle)
        Addresses.append(Address)
        #print(Owners)

#Step 3: Create random number to select from list
RegistrationsLength=len(Registrations)-1
OffenderIndex=random.randint(1,RegistrationsLength)

#Step 4: Pick out all this offenders details:
OffenderRegistration=Registrations[OffenderIndex]
OffenderOwner=Owners[OffenderIndex]
OffenderMakeOfVehicle=MakeOfVehicleList[OffenderIndex]
OffenderModelOfVehicle=ModelOfVehicleList[OffenderIndex]
OffenderAddress=Addresses[OffenderIndex]

#Step5: Simulate the offender's captured speed by randomly generating it:
OffenderSpeed=random.randint(70,150)

#Step 6: Write the Registration, owner details, and speed to a new file called 'Speeder.csv'

try:
    with open('Speeder.csv') as file:
        pass
        with open('Speeder.csv', 'a', newline='') as csvfile:
            Regwriter = csv.writer(csvfile, delimiter=',')
            Regwriter.writerow([OffenderRegistration] +
                               [OffenderOwner] +
                               [OffenderMakeOfVehicle] +
                               [OffenderModelOfVehicle] +
                               [OffenderAddress] +
                               [OffenderSpeed])
except IOError as e:
    with open('Speeder.csv', 'w', newline='') as csvfile:
        Regwriter = csv.writer(csvfile, delimiter=',')
        Regwriter.writerow(['Registration'] +
                           ['Owner'] +
                           ['Make Of Vehicle'] +
                           ['Model Of Vehicle'] +
                           ['Address'] +
                           ['Speed'])
        Regwriter.writerow([OffenderRegistration] +
                           [OffenderOwner] +
                           [OffenderMakeOfVehicle] +
                           [OffenderModelOfVehicle] +
                           [OffenderAddress] +
                           [OffenderSpeed])
# Print output to screen so the user knows something has been done!
print('------------------------------------------------------------')
print('The following details have been added to the Speeders file: ')
print('------------------------------------------------------------')
print('Registration: ' + OffenderRegistration)
print('Owner: ' +OffenderOwner)
print('Make of  Vehicle: ' + OffenderMakeOfVehicle)
print('Model of Vehicle: ' + OffenderModelOfVehicle)
print('Address: ' + OffenderAddress)
print('Speed: ' + str(OffenderSpeed))
print('------------------------------------------------------------')

#end



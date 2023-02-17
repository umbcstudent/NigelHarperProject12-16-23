#Print a line of equal sign
print("======================")
#Print a blank line
print()
#Display the company logo
print("Welcome to the UMBC")
print("Car Customization Form!")
#Print a blank line
print()
#Print a line of equal signs
print("=======================")
#Print a blank line
print()
print()
#Explain the Custom's Car selection process and how to navigate thru the website
print("(For multiple choice selections, please enter the letter of the selection you're looking for")
print("~ Make & Model ~")
#Get the Make of customer car
print("1. What Make or Model are you currently looking for")
#Show the four selections that are currently avaiable
print("  a. Maserati Grecale")
print("  b. Mercedes-Benz GLB Class")
print("  c. Porsche Macan")
print("  d. Genesis GV90")
#Ask the customer to prompt their selection in the box
rezz = input("Please enter 'a'-'d': ")
print()
#Print a blank line
print()
#Ask the customer to question
print("2.  Would you like to upgrade from RWD option to the AWD? ")
#Ask the customer to prompt the their answer
option = input("Please enter 'yes' or 'no': ")
#Display the customer's request
print()
#Print a blank line
print()
#Ask the next question on the car's selection
print("~ Exterior ~")
print("3.  What color would you like your car to be? :")
#Request an answer of the Car's color
bezz = input("You may enter the name of any color you'd like: ")
#Display the customer's color request
print()
#Print a blank line
print()
# Ask the customer about performance package
print("4.  Would you like the deluxe weather package? ")
#Prompt the customer's request
fezz = input("Please enter 'yes' or 'no':") 
#Display the customer request on package
print()
#Print a blank line
print()
#Introduce the Interior portion
print(" ~ Interior ~ ")
#Print a blank line
print()
#Ask the question about engine interior
print("5.  Which Engine would you like your car to have? ")
#Prompt the customer's request on engine interior and options
print("  a. 3.0 Entry Engine")
print("  b. 3.5 Performance Engine")
print("  c. Eco Engine")
#Ask the customer to selection one of the options
customEngine = input("Please enter 'a'-'c' :")
#Print the customer's selection
print()
#Print a blank line
print()
# Ask the question about heated seats
print("6.  Would you like heated seats? ")
#Prompt the question to result in an answer
seat = input("Please enter 'yes' or no: ")
#Print the customer's answer
print()
#Print a blank line twice
print()
print()
#Print a line of equal signs
print("================================")
#Print a blank line
print()
#Print the summay report
print("  ~  Summary  ~ ")
#Print the entire order in chronically order
print(f'Model Option: {rezz}')
print(f'Upgrade to AWD:{option}')
print(f'Desired Color: {bezz}')
print(f'Upgrade to Deluxe Weather:{fezz}')
print(f'Engine Option:{customEngine}')
print(f'Upgrade to Heated Seated:{seat}')
print()
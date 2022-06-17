#****************************************************************
#Name: GOODNEWS GOODNEWS

#
#ANA1001 Lab 4
#****************************************************************


#############								   	                  
#Question #1							
#############
'''Create a series of 7 conditional tests. In each test, print your prediction and the result. In your 7 tests, include examples of: 
tests for equality and inequality with strings,
tests using the lower() method,
numerical tests for equality and inequality,
greater than and less than, greater than or equal to, and less than and equal to
tests that use and / or keyword operators
test if the item is in a list
test if the item is not in a list 
This will look like:

pizza = 'mushroom'
print('Is the pizza == mushroom? I predict True.')
print(pizza == 'mushroom')

Make sure you understand the difference between = , != and == and why your statements are evaluating to True or False'''

#7 conditional tests
food = 'cake'
print("Is food == cake? I predict True") #tests for equality and inequality with strings
print(food == "cake")

print("Is food not equal to cake? I predict False")
print(food != "cake")

print("Is food not equal to cake? I predict True")#tests using the lower() method,
print(food.lower() == "cake")

hour = 60
print("Is an hour equal to 60 seconds? I predict True" )
print(hour == 60)

print("Is hour greater than 50 seconds? I predict True")
print(hour > 50)

print("Is hour less than 50 seconds? I predict False")
print(hour < 50)

print("Is hour between 50 to 70 seconds? I predict True")
print(hour >50 and hour <70)

list = ['cloths', "phone", "shoes", "key"]
print("key in the list I predict True")
print("key" in list )#test if the item is in a list

print("computer in the list I predict False")#test if the item is not in a list
print("computer" in list )


#############								   	                  
#Question #2							
#############
'''Make a game called paper, rock, scissors. The game has two players, you, and the computer. You will pick an option. The computer will pick a random option. Import the random package on the first line of your python file.. Using if/elif/else statements, compare the options and determine if its a win, loss, or tie, and have python print out the results'''

#A game called paper, rock, scissors
import random
mychoice = "scissors"
game = ['rock', 'paper', 'scissors']
computer = random.choice(game)
if mychoice == "scissors" and computer == "paper":
  print("computer wins")
elif mychoice == "scissors" and computer == "rock":
  print("I win")
elif mychoice == "paper" and computer == "scissors":
  print("computer wins")
elif mychoice == "paper" and computer == "rock":
  print("I win")
elif mychoice == "rock" and computer == "scissors":
  print("computer wins")
elif mychoice == "rock" and computer == "paper":
  print("I win")
else:
  print("There is a tie")



#############								   	                  
#Question #3							
#############
'''Going back to your dog years program, you now have a new challenge. Your vacation costs $10,000, but for every twenty year span of your age in dog years, you get a 5% discount. Assign the cost to a variable, and do the same with your age. Then write an if-elif-else chain to determine what discount you get, based on your age range. Have a message print out using an fstring explaining how much the original trip cost, what your discount is, and the final price of the trip based on your age in dog years.  This could look like

0-19 no discount
20-40 5% discount
41-60 10% discount
61-80 15% discount
81-100 20% discount ... and so on'''

#dog years program, calculating the total cost of trip with each dogyear discount 
v_costs = 10000
age = 27
dogyears = age * 7
if dogyears <=19:
  discount = 0
elif dogyears <=40:
  discount = 5
elif dogyears <=60:
  discount = 10
elif dogyears <=80:
  discount = 15
elif dogyears <=100:
  discount = 20
else:
  discount = 0
print(f"The initial cost of the trip {v_costs}\nTotal discount {v_costs * discount/100}\nTotal cost of the trip is {v_costs - (v_costs * discount/100)}")


#############								   	                  
#Question #4							
#############
'''Research BMI (Body Mass Index) formulas and create a program that calculates BMI based on weight ranges. This page has the ranges and BMI based on weight https://www.canada.ca/en/health-canada/services/food-nutrition/healthy-eating/healthy-weights/canadian-guidelines-body-weight-classification-adults/quick-reference-tool-professionals.html

See https://www.diabetes.ca/managing-my-diabetes/tools---resources/body-mass-index-(bmi)-calculator#:~:text=Body%20Mass%20Index%20is%20a,range%20is%2018.5%20to%2024.9.'''

#calculating BMI by defining the BMI function and returning the function to the script 
def BMI(height, weight): 
  bmi = weight/(height**2) 
  return bmi 

#Numbers here will change the Health Status
height = 2 
weight = 200

bmi = BMI(height, weight) 
print("The BMI is", format(bmi))
print("Health status = ",end="") #assigned health status to appear in every print in the if-elif-else chain.
if (bmi < 18.5): 
  print("Underweight and health risk increased") 
elif ( bmi >= 18.5 and bmi < 24.9): 
  print("Healthy and health risk is least") 
elif ( bmi >= 24.9 and bmi < 29.9): 
  print("Overweight and health risk is increased") 
elif ( bmi >=30 and bmi < 34.9): 
  print("You are suffering from Obesity and health risk is high")
else:
  print("You are severely obese and health risk is high and extreme, visit our gym today")


#############								   	                  
#Question #4							
#############
'''Tasty Pizza has asked you to roll out their premium pizza customer program and has hired you to program the system. The first step is to see if a new user is already in the database. First, create a list of five classmates who are on the premium pizza customer list. Then, make a new list with five more classmates that want to join the exclusive club (make sure to also include some of the users on the first list in the second). 
Loop through the new list to see if someone is also in the member list. If they are, print a message letting them know that they are already a member. If they are not, let them know they are able to join and write a sentence about the benefits of joining the club. Make sure to make your comparison case insensitive.'''

#List of 5 class mates in premium customer list
old_list=["Sharon","Ramu","Ravi","Sneha","Goodnews"]

#List of 5 class mates that wants to join premium customer list
new_list=["Sharon","Anju","Ravi","Arjun","Goodnews"]
for new_list in old_list:
  if 'Anju' in old_list:
    print("You are already a member")
else:
  msg="If you join the club you can taste most tastiest pizza"
  print(msg)

#############						   	                  
#Question #6						
#############
'''Store the numbers 1-9 in a list. Loop through the list. Use an if-elif-else chain inside the loop to print the proper ordinal ending to the number (1st, 2nd, 3rd, 4th, etc), and print each result to a new line'''
#numbers 1-9 in a list
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers: #loop through the list.
 if number == 1:
   print("1st")
 elif number == 2:
	 print("\n2nd")
 elif number == 3:
	 print("\n3rd")
 else:
   print("\n" + str(number) + "th")

#############						   	                  
#Question #7						
#############
'''Write a program using the random package (remember to import random at the top of your file) and use random.randint(1,10) to get the computer to pick a number. Assign a number value to the player, and check using an if statement and equality if the number the computer has is the same number, or if the number is higher or lower. Print out the results in a message using an fstring.'''

#using a random package
import random
computer=random.randint(1,10)
print("computer :"+str(computer))
player=6
print("player :"+str(player))
if computer==player:
    print(f"both values are equal")
elif computer>player:
    print(f"computer is greater than player")
else:
    print(f"computer is less than the player")
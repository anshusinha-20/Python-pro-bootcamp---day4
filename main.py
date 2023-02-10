# import random

# randomInteger = random.randint(1, 10)
# print(randomInteger)

# randomFloat = random.random()
# print(randomFloat)

# statesOfIndia = ["Jharkhand", "Odisha", "Bihar"]
# print(statesOfIndia[0])
# print(statesOfIndia[-1])
# statesOfIndia[2] = "Delhi"
# print(statesOfIndia[-1])

# statesOfIndia.append("Madhya Pradesh")
# print(statesOfIndia)
# statesOfIndia.extend(["Uttar Pradesh", "Jammu and Kashmir", "Manipur"])
# print(statesOfIndia)

# fruits = ["strawberries", "nectarines", "apples", "grapes", "peaches", "cherries", "pears"]
# vegetables = ["spinach", "kale", "potatoes", "tomatoes", "celeries"]
# dirtyDozens = [fruits, vegetables]
# print(dirtyDozens)

#############################

# Day 4 Project: Rock Paper Scissors

import random

rock = """ 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

myChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computerChoice = random.randint(0, 2)

if (myChoice == 0):
    print(f"You chose:\n{rock}")
    if (computerChoice == 0):
        print(f"Computer chose:\n{rock}\nIt's a draw!")
    elif (computerChoice == 1):
        print(f"Computer chose:\n{paper}\nYou lose!")
    elif (computerChoice == 2):
        print(f"Computer chose:\n{scissors}\nYou won!")
elif (myChoice == 1):
    print(f"You chose:\n{paper}")
    if (computerChoice == 0):
        print(f"Computer chose:\n{rock}\nYou won!")
    elif (computerChoice == 1):
        print(f"Computer chose:\n{paper}\nIt's a draw!")
    elif (computerChoice == 2):
        print(f"Computer chose:\n{scissors}\nYou lose!")
elif (myChoice == 2):
    print(f"You chose:\n{scissors}")
    if (computerChoice == 0):
        print(f"Computer chose:\n{rock}\nYou lose!")
    elif (computerChoice == 1):
        print(f"Computer chose:\n{paper}\nYou won!")
    elif (computerChoice == 2):
        print(f"Computer chose:\n{scissors}\nIt's a draw!")
else:
    print("Invalid input!")






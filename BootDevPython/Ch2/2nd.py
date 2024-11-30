# variables -value can change

player_health = 1000
print(player_health)

# reduce by 100 here 
print(player_health - 100 )

player_health = 800
print(player_health)

player_health = 700
print(player_health)
player_health = 600
print(player_health)

# math 
player_health = 1000 
armour_multiplier = 2 

# create armoured_health here 
armoured_health = player_health * armour_multiplier 
print(armoured_health)

player_health = 100 
poison_damage = - 10 

player_poison_health = player_health + poison_damage 
print(player_poison_health)

# the best_sword var holds the value of the best sword in the game
best_sword = "scimitar"
print(best_sword)

# variable names 
my_name = "Trash Puppy"

#camelCase  - convention used in Python
variableName = 'TP'
#snake_case 

variable_name = 'TP'

# SCREAMING_SNAKE_CASE 
VARIABLE_NAME = 'TP'

player_has_magic = True  # 1 == true, 0 == false
print(f"player_has_health is a/an {type(player_health)}")
print(f"player_has_magic is a/an {type(player_has_magic)}")

# F-strings in Python (formatted strings)
name = "Trash Puppy"
height = "6ft"

# print("My name is " + name + "and I am " + height + "tall!") 

print(f"My name is {name} and I am {height} tall!")

name = "Yarl"
age = 37
race = "dwarf"

print(f"{name} is a {race} who is {age} years old.")

# Nonetype variables / used to set a default value that you expect to 
# / will change later 

# (None = absence of any value)  
enemy = None 

print(enemy is None)
print(enemy is not  None)

# Dynamic Typing - the type of value in stored in variables can change 

speed = 5 # integer type 

speed = "five" # string type 

# math with strings 
sentence_start = "You have "
sentence_end = " health"

player1_health = "1200"
player2_health = "1100"

print(sentence_start + player1_health + sentence_end)
# print(sentence_start * 6)
print(sentence_start + player2_health + sentence_end)

# Multi-Variable Declaration 
sword_name, sword_damage, sword_length = "Excalibur", 10 , 200

# the above is identical to: 
sword_name = "Excalibur"
sword_damage = 100
sword_length = 200

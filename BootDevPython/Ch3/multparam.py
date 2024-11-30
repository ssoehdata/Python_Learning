# multiple paramaters 

def subtract(a, b):  
    result = a - b
    return result 

result = subtract(5, 3)
print (result) 

# N.B. multiple parameters cab be given, but 
# the order of values passed into the parameters matters.
# the first parameter is the first value you pass in, 
# the second parameter is the second value you pass in. 

# e.g. a = 5, b = 3 


###############################
damage_one: int  = 2     # added type annotation
damage_two = 4 
damage_three: float = 3.5   # added  a float, note that annotation in triple_attack func below
damage_four  = -1
damage_five = 10 
damage_six = 5

def triple_attack(slash_one, slash_two, slash_three: list[int | float]) -> int | float: # added type annotation
    total_dmg = slash_one + slash_two + slash_three
    return total_dmg


result = triple_attack(2, damage_two, 89.9)   # values can be passed either as raw value, or as var
print(f"Result = {result}")



print("Getting damage for", damage_one, damage_two,"and", damage_three, '...')
print(triple_attack(damage_one, damage_two, damage_three), "points of damage dealt!")
print("==========================================")

print("Getting damage for", damage_four, damage_five,"and", damage_six, '...')
print(triple_attack(damage_four, damage_five, damage_six), "points of damage dealt!")
print("==========================================")

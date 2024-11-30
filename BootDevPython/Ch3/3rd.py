# Functions - allow for reusing and organizing code.
def area_of_circle(radius) -> int:      # radius is a parameter (or argument)   
    pi = 3.14
    area  = pi * radius * radius 
    return area  # n.b.: is also the end of the function body


sword_length = 1.0 
spear_length = 2.0 

sword_area = area_of_circle(sword_length)   # here area_of_circle is the function,
                                            #  sword_length is an argument (or parameter)
spear_area = area_of_circle(spear_length) 

print("Sword length:", sword_length, "meters.")
print("Sword attack area:", sword_area, "square meters") 

print("Spear length:",  spear_length, "meters.")
print("spear attack area:", spear_area, "square meters")

if __name__ == "__main__":
    print("This is the Functions module, aka Ch3")


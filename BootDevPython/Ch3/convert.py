def to_celsius(f) ->  int | float:
    celsius: int |  float = (5/9) * (f - 32)
    return celsius 


def test(f): 
    c: int | float = round(to_celsius(f), 2)
    print(f, "degrees fahrenheit is", c, "degrees celsius")


test(100)
test(88.5)
test(104)
test(112)

# Function calls
# damage1 = calculate_damage(10, 20, 30)
# damage2 = calculate_damage(5,10, 15)

test1 = to_celsius(32)
test2 = to_celsius(212)

print(f"test1 equals: {test1}")
print(f"test2 equals: {test2}")

# Terminology
# values passed into a function "parameters" or "arguments"

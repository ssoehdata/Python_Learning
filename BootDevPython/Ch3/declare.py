

def main():
    print("Fantasy Quest is booting up...")
    print("Game is running")
    health = 10 
    armour = 5 
    add_armour(health, armour)

def add_armour(h, a):
    new_health = h + a 
    print_health(new_health)

def print_health(new_health):
    print(f"The player now has {new_health} health")


    

# call entrypoint last 
main() 



# Multiple Return values 

def become_warrior(first_name: str, last_name: str, power: int):
    title: str = f"{first_name} {last_name} the warrior"

    new_power: str | int = power + 1 
    
    return title, new_power


def main():    
    test("Frodo","Baggins", 5 )
    test("Bilbo","Baggins", 10 )
    test("Gandalf","The Grey", 9000 )

def test(first_name, last_name, power):
    title, new_power = become_warrior(first_name, last_name, power)
    print(title, "has a power level of:", new_power)


main()

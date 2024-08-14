print("MonkeBeast Generator")
print()

monkedex = {}

def prettyPrint():
    print("Name\tType\tHP\tMP")
    if monkedex: 
        for key, value in monkedex.items():
            print(f"{key:^12}|{value['type']:^10}|{value['hp']:^6}|{value['mp']:^6}")

while True:
    print("Add your Beast!")
    name = input("Name: ").title()
    beast_type = input("Type: ").title()
    hp = int(input("HP: "))
    mp = int(input("MP: "))
    monkedex[name] = {"type": beast_type, "hp": hp, "mp": mp}
    print("------------")
    prettyPrint()
    print()
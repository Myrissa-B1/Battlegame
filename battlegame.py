# battlegame
wizard = 'wizards'
elf = 'elf'
human = 'human'
panther = 'panther'
wizard_hp = 70
wizard_damage = 150
elf_hp = 100
elf_damage = 100
human_hp = 150
human_damage = 20
panther_hp = 70
panther_damage = 50
dragon_hp = 300
dragon_damage = 50
dragon = 'dragon'

while True:
    print("1. Wizard")
    print("2. Elf")
    print("3. Human")
    print("4. Panther")
    print("5. Exit")
    option = input("Choose your character: ")
    option = option.lower()
    if option == '1' or option == 'wizard':
        my_hp = wizard_hp
        my_damage = wizard_damage
        character = 'wizard'
        break
    elif option == '2' or option == 'elf':
        my_hp = elf_hp
        my_damage = elf_damage
        character = 'elf'
        break
    elif option == '3' or option == 'human':
        my_hp = human_hp
        my_damage = human_damage
        character = 'human'
        break
    elif option == '4' or option == 'panther':
        my_hp = panther_hp
        my_damage = panther_hp
        character = 'panther'
        break
    elif option == '5' or option == 'exit':
        print("You Have Exited the game")
        exit()
    else:
        print("Unknown character")
print(f"You have chosen character : {character.capitalize()}")
print(f"Health: {my_hp}")
print(f"Damage {my_damage}")

print(f"Dragon HP is : {dragon_hp}")
print(f"{character.title()} damage is {my_damage}")

while True:
    dragon_hp = int(dragon_hp) - int(my_damage)
    print(f"The {character.title()} damaged the Dragon for {my_damage} points!")
    if dragon_hp <= 0:
        print("The Dragon's current hit points are 0")
        print("The Dragon has lost the battle")
        break
    my_hp = int(my_hp) - int(dragon_damage)
    print(f"The Dragon damaged {character.title()} for {dragon_hp} points!")
    if my_hp <= 0:
        print(f"The {character.title()} current hit points are 0")
        print(f"The {character.title()} has lost the battle")
        break

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and out run the natives.")
import random

#starting variables
done = False
miles_traveled = 0
thirst = 0
camel_tired = 0
natives_traveled = -20
drink = 5
natives_up = random.randrange(0, 10)
full_speed = random.randrange(10, 20)
moderate_speed = random.randrange(5, 12)

#while loop
while not done:
    print("A. Drink from your canteen .", "\nB. Ahead moderate speed.", "\nC. Ahead full speed.",
          "\nD. Stop for the night.", "\nE. Status check.", "\nQ. Quit.")
    choice = input("Type your choice ")
    if choice == "q":
        done = True
    # choice e
    elif choice == "e":
        print(
            "\nMiles traveled: %d\nDrinks in canteen: %d\nThe natives are %d behind you. \nCamel tiredness %d \nThirst level are %d" % (
            miles_traveled, drink, natives_traveled, camel_tired, thirst,))
    # choice d
    elif choice == "d":
        camel_tired = 0
        print("The camel is happy! The natives advance %d miles" % (natives_up,))
    # choice c
    elif choice == "c":
        print("you have traveled %d miles" % (full_speed,))
        miles_traveled = miles_traveled + full_speed
        natives_traveled = natives_traveled + natives_up
        thirst = thirst + 1
        camel_tired = random.randrange(1, 3)
        print("camel tiredness %d" % (camel_tired,))
        print("the natives advance %d miles" % (natives_up,))
    # choice b
    elif choice == "b":
        print("you have traveled %d miles" % (moderate_speed,))
        miles_traveled += full_speed
        natives_traveled += natives_up
        thirst += 1
        camel_tired = camel_tired + random.randrange(1, 3)
        print("camel tiredness %d" % (camel_tired,))
        print("the natives advance to %d miles" % (natives_up,))
    # choice a
    elif choice == "a":
        print("You drink from your canteen")
        drink = drink - 1
        thirst = 0

    # thirst warning
    if thirst >= 3:
        print("you are thirsty!")

    # death from thirst
    if thirst >= 5:
        print("you died of thirst")
        done = True

    # camel warning
    if camel_tired >= 5:
        print("your camel is getting tired")

    # camel death
    if camel_tired >= 8:
        print("Your camel is dead")
        done = True

    # caught by natives
    if natives_traveled >= 0:
        print("The natives caught you")
        done = True

    # natives warning
    elif natives_traveled >= -10:
        print("The natives getting close")

    #game won
    if miles_traveled == 300:
        print("You win!")
        done = True

    #out of water
    if drink <= 0:
        print("There are no more drinks")
        thirst = 0
        drink = done

    elif thirst >= 1:
        miles_traveled -= 1

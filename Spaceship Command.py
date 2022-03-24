import time
ShipName = "Ieniadas II"
Captain = "Adeline Fuller"
Location = "Ienia"
Password = "!£$%^IJHgfde456uHGFR%^&8iuy545678YTGHJ(*&^%thgfrtyu"
PasswordAttempt = input("Ship Password: ")
while PasswordAttempt != Password:
    print("Incorrect password")
    PasswordAttempt = input("Ship Password: ")
print ("Password correct. Welcome aboard the", ShipName + ".")
print("\nThe spaceship", ShipName, "is currently at", Location + ".") 
Choice = ""
while Choice != "d":
    print ("\nWhat would you like to do", Captain + "?\n")
    print ("a. Travel to another planet")
    print ("b. Fire cannons")
    print ("c. See details")
    print ("d. Exit\n")
    Choice = input ("Enter your choice:  ")
    if Choice == "a":
        Location = input ("Where would you like to go? ")
        print ("\nTravelling...")
        time.sleep(2)
        print (ShipName, "has arrived at", Location + ".")
        time.sleep(0.5)
    elif Choice == "b":
        print ("\nFiring cannons...")
        time.sleep(1)
        print ("\nBANG!")
        time.sleep(1.5)
     elif Choice == "c":
        print ("\nShip name:", ShipName)
        print ("Capain:", Captain)
        print ("Location:", Location)
        Details = input ("\nDo you want to change these detaials (y/n)? ")
        if Details == "y":
            print ("\nWhich details do you want to change?\n")
            print ("a. Ship name")
            print ("b. Captain")
            print ("c. Location")
            DetailsChoice = input ("\nEnter your choice: ")
            if DetailsChoice == "a":
                ShipName = input ("What do you want your ship's name to be? ")
            elif DetailsChoice == "b":
                Captain = input ("What do you want your captain's name to be? ")
            elif DetailsChoice == "c":
                Location == input ("What do you want your loction's name to be? ")
            else:
                print ("Invalid command. Please enter 'a','b' or 'c'.")
        elif Details == "n":
            print ("Okay")
        else:
            print ("Invalid command. Please enter 'y' or 'n'.")
    elif Choice == "d":
        print ("Goodbye")
        time.sleep(1)
    else:
        print ("Invalid command. Please enter 'a','b','c' or 'd'.")

print("Welcome to Rollercoaster")
height = int(input("How tall are you? "))
bill = 0
if height >= 120:
    print("You can ride the Rollercoaster")
    age = int(input("How old are you? "))
    if age <= 12:
        bill = 5
        print("Please Pay $5")
    elif age <= 18:
        bill = 7
        print("Please Pay $7")
    else:
        print("Please Pay $12")
        bill = 12
    wants_photo = input("Would you like to take a photo? Type y for yes and n for no: ")
    if wants_photo == "y":
        bill = bill + 3
    print(f"Your final bill is ${bill}")

else:
    print("You need to grow taller to ride the Rollercoaster")
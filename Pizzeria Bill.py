print("Welcome to Python Pizzeria")
size = input("What size pizza? S, M, L")
pepperoni = input("Do you want Pepperoni? Y for Yes, N for No")
cheese = input("Do you want Extra Cheese? Y for Yes, N for No")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid Input")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M":
        bill += 4
    elif size == "L":
        bill += 5
    else:
        print("No Pepperoni")

if cheese == "Y":
    if size == "S":
        bill += 3
    elif size == "M":
        bill += 5
    elif size == "L":
        bill += 7
    else:
        print("No Cheese")

print(f"Your Total bill is ${bill}")


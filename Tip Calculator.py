print("Welcome to Tip Calculator")
bill = float(input("What was the Total Bill $"))
tip=int(input("What percentage tip you want to give? 10 12 15"))
people = int(input("How many people do you have? "))
tip_as_present = tip/100
total_tip = bill*tip_as_present
total_bill = bill+total_tip
bill_per_person = total_bill/people
final_amount = round(bill_per_person,2)
print(f"Each Person Pay ${final_amount}")
print("Welcome to tip calculator.")
bill = input("What was the total bill? $")
tip = input("What percentage of tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
bill_tip = float(bill) * (int(tip)/100)
total_bill = bill_tip + float(bill)
per_person_bill = total_bill / int(people)
print(f"Each person should pay: ${round(per_person_bill,2)}")
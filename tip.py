print("Welcome to tip calculator")
bill = float(input("What is the total bill amount? $ "))
tip = int(input("What is the percentage you want to give as tip? 5 10 15 20 "))
people = int(input("How many people are sharing bill? "))
#lets do some maths now
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
#Tip Calculator

#get amount for bill and tip
Bill = input("How much was your bill for?")
Tip = input("how much tip would you like to leave? Ex. 10%, 15%, 20%, 25%, etc.")

#convert strings to float numbers
bill_int = float(Bill)
tip_int = float(Tip) * .100
#adds total together and returns float
Total_amount =  tip_int + bill_int
What_it_is = f"Your bill came to ${bill_int} with a tip amount of ${tip_int}. Making your grand total ${Total_amount}. Hope your food was good!"
print(What_it_is)
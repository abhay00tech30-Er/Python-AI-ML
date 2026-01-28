"""
2️⃣ Bill Split Calculator
Write a program that takes total bill amount and number of friends as input.
Calculate how much each person will pay.
Also print the data type of each variable used.
(Hint: use float() and division operator)
Total bill: 1000
Friends: 4
Each will pay: 250.0
"""

bill = float(input("Enter total bill amount: "))
friends = int(input("Enter number of friends: "))
each = bill / friends
print("Each will pay: ", each) 
print(type(bill))
print(type(friends))
print(type(each))   
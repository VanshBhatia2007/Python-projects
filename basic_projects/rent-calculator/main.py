rent = int(input("enter your flat rent :"))
food = int(input("enter your food expenses :"))
elec = int(input("enter your electricity bill :"))
charge_per_unit = int(input("enter your charge per unit :"))
pers = int(input("enter the no. of persons living in flat :"))

total_bill = elec*charge_per_unit

total = (food + rent + total_bill) // pers
print("each person rent is : ",total)
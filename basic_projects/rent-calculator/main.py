rent = int(input("enter your flat rent :"))
food = int(input("enter your food expenses :"))
elec = int(input("enter your electricity bill :"))
charge_per_unit = int(input("enter your charge per unit :"))
pers = int(input("enter the no. of persons living in flat :"))

total_bill = elec*charge_per_unit

total = (food + rent + total_bill) // pers
print("each person rent is : ",total)

# output :
# enter your flat rent :5000
# enter your food expenses :2500
# enter your electricity bill :1500
# enter your charge per unit :10
# enter the no. of persons living in flat :2
# each person rent is :  11250
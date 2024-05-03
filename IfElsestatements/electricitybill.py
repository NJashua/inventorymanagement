units_consumed = int(input("Enter the units consumed: "))
total_bill = 0

if units_consumed <= 100:
    total_bill = units_consumed * 0.8
elif units_consumed <= 200:
    total_bill = 80 + (units_consumed - 100) * 0.9
elif units_consumed <= 300:
    total_bill = 170 + (units_consumed - 200) * 1.1
else:
    total_bill = 250 + (units_consumed - 300) * 1.5

print("Total bill amount:", total_bill)

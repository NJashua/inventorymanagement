number = input("Enter input value: ")
number = int(number)

print("Prime numbers are:")
for num in range(2, number + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

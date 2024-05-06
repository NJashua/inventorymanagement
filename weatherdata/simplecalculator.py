def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a/b

def main():
    print("Welcome to simple calculator")

    try:
        while True:
            print("\n Select the operation")
            print("1. Addition")
            print("2. Subtration")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit")

            choice = int(input("Enter your choice: "))
            if choice == 1:
                num_1 = int(input("Enter first number: "))
                num_2 = int(input("Enter second number: "))
                result = add(num_1, num_2)
                print("Addition of two numbers is: ", result)
            elif choice == 2:
                num_1 = int(input("Enter first number: "))
                num_2 = int(input("Enter second number: "))
                result = sub(num_1, num_2)
                print("Subtraction of two numbers is: ", result)
            elif choice == 3:
                num_1 = int(input("Enter first number: "))
                num_2 = int(input("Enter second number: "))
                result = mul(num_1, num_2)
                print("Multiplcation of two numbers is: ", result)
            elif choice == 4:
                num_1 = int(input("Enter first number: "))
                num_2 = int(input("Enter second number: "))
                result = div(num_1, num_2)
                print("Division of two numbers is: ", result) 
            else:
                print("Exiting...")
                break
    except:
        print("Invalid choice..")

if __name__ == "__main__":
    main()
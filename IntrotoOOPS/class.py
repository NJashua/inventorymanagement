class Employee:
    def __init__(self, first_name, last_name, salary) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = first_name + '.' + last_name + '@' + 'jda.com'

emp_1 = Employee("John", "Son", 59000)
emp_2 = Employee("David", "Son", 60000)
print(emp_1.email)
print(emp_2.email) 
print("The salary of {},{} is {} and email {}".format(emp_2.first_name, emp_2.last_name, emp_2.salary, emp_2.email))
print("The salary of {},{} is {} and email {}".format(emp_1.first_name, emp_1.last_name, emp_1.salary, emp_1.email))

import pandas as pd
import uuid

class Employee:
    def __init__(self, name, position, department, email, salary):
        self.employee_id = str(uuid.uuid4())[:5]
        self.name = name
        self.position = position
        self.department = department
        self.email = email
        self.salary = salary

    def update_details(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

class EmployeeManagement:
    employees = []
    departments = {}

    @classmethod
    def add_employee(cls, employee):
        cls.employees.append(employee)
        if employee.department not in cls.departments:
            cls.departments[employee.department] = []
        cls.departments[employee.department].append(employee)
        print(f"Employee {employee.name} added successfully with ID: {employee.employee_id}")

    @classmethod
    def display_employee_details(cls):
        if not cls.employees:
            print("No employees found.")
        else:
            print("Employee Details: ")
            for employee in cls.employees:
                print(f'ID: {employee.employee_id}, Name: {employee.name}, Position: {employee.position}, Department: {employee.department}, Email: {employee.email}, Salary: {employee.salary}')

    @classmethod
    def display_department_details(cls, department):
        if department not in cls.departments:
            print(f"No employees found in department: {department}")
        else:
            print(f"Employees in {department} department: ")
            for employee in cls.departments[department]:
                print(f'ID: {employee.employee_id}, Name: {employee.name}, Position: {employee.position}, Email: {employee.email}, Salary: {employee.salary}')

    @classmethod
    def update_employee_details(cls, employee_id, **kwargs):
        for employee in cls.employees:
            if employee.employee_id == employee_id:
                employee.update_details(**kwargs)
                print(f"Details updated successfully for employee ID: {employee_id}")
                return
        print(f"No employee found with ID: {employee_id}")

    @classmethod
    def remove_employee(cls, employee_id):
        for employee in cls.employees:
            if employee.employee_id == employee_id:
                cls.employees.remove(employee)
                cls.departments[employee.department].remove(employee)
                print(f"Employee {employee.name} removed successfully")
                return
        print(f"No employee found with ID: {employee_id}")

    @classmethod
    def total_salary_expense(cls):
        total_salary = sum(employee.salary for employee in cls.employees)
        print(f"Total salary expense: ${total_salary}")

    @classmethod
    def search_employee_by_name(cls, name):
        found = False
        for employee in cls.employees:
            if name.lower() in employee.name.lower():
                print(f'ID: {employee.employee_id}, Name: {employee.name}, Position: {employee.position}, Department: {employee.department}, Email: {employee.email}, Salary: {employee.salary}')
                found = True
        if not found:
            print(f"No employee found with name containing '{name}'")

    @classmethod
    def give_raise(cls, employee_id, raise_amount):
        for employee in cls.employees:
            if employee.employee_id == employee_id:
                employee.salary += raise_amount
                print(f"Salary increased successfully for employee {employee.name}. New salary: ${employee.salary}")
                return
        print(f"No employee found with ID: {employee_id}")

    @classmethod
    def promote_employee(cls, employee_id, new_position):
        for employee in cls.employees:
            if employee.employee_id == employee_id:
                employee.position = new_position
                print(f"Employee {employee.name} promoted to {new_position}")
                return
        print(f"No employee found with ID: {employee_id}")

    @classmethod
    def save_employee_data(cls, filepath):
        # Ensure the file extension is '.xlsx'
        if not filepath.endswith('.xlsx'):
            filepath += '.xlsx'

        # Prepare the data for the DataFrame
        data = {
            "ID": [employee.employee_id for employee in cls.employees],
            "NAME": [employee.name for employee in cls.employees],
            "POSITION": [employee.position for employee in cls.employees],
            "DEPARTMENT": [employee.department for employee in cls.employees],
            "EMAIL": [employee.email for employee in cls.employees],
            "SALARY": [employee.salary for employee in cls.employees]
        }

        df = pd.DataFrame(data)

        df.to_excel(filepath, index=False)

        print(f"Employee data saved to {filepath}")

    @classmethod
    def employee_count_by_department(cls):
        print("Employee count by department:")
        for department, employees in cls.departments.items():
            print(f"{department}: {len(employees)}")


# Sample employee data
employees_data = [
    ["John Doe", "Manager", "Sales", "john.doe@example.com", 50000],
    ["Jane Smith", "Engineer", "Engineering", "jane.smith@example.com", 60000],
    ["David Brown", "Analyst", "Finance", "david.brown@example.com", 55000],
    ["Emily White", "HR Manager", "Human Resources", "emily.white@example.com", 65000],
]

# Initialize employees
for employee_info in employees_data:
    EmployeeManagement.add_employee(Employee(*employee_info))

# Switch case for user input
def main():
    while True:
        print("1. Add Employee")
        print("2. Display Employee Details")
        print("3. Display Department Details")
        print("4. Update Employee Details")
        print("5. Remove Employee")
        print("6. Calculate Total Salary Expense")
        print("7. Search Employee by Name")
        print("8. Give Raise to Employee")
        print("9. Promote Employee")
        print("10. Employee Count by Department")
        print("11. Save Employee Data to Excel")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Add Employee
            name = input("Enter employee name: ")
            position = input("Enter employee position: ")
            department = input("Enter employee department: ")
            email = input("Enter employee email: ")
            salary = float(input("Enter employee salary: "))
            EmployeeManagement.add_employee(Employee(name, position, department, email, salary))

        elif choice == "2":
            # Display Employee Details
            EmployeeManagement.display_employee_details()

        elif choice == "3":
            # Display Department Details
            department = input("Enter department name: ")
            EmployeeManagement.display_department_details(department)

        elif choice == "4":
            # Update Employee Details
            employee_id = input("Enter employee ID: ")
            field = input("Enter field to update (name/position/department/email/salary): ")
            new_value = input(f"Enter new value for {field}: ")
            EmployeeManagement.update_employee_details(employee_id, **{field: new_value})

        elif choice == "5":
            # Remove Employee
            employee_id = input("Enter employee ID to remove: ")
            EmployeeManagement.remove_employee(employee_id)

        elif choice == "6":
            # Calculate Total Salary Expense
            EmployeeManagement.total_salary_expense()

        elif choice == "7":
            # Search Employee by Name
            name = input("Enter employee name to search: ")
            EmployeeManagement.search_employee_by_name(name)

        elif choice == "8":
            # Give Raise to Employee
            employee_id = input("Enter employee ID: ")
            raise_amount = float(input("Enter raise amount: "))
            EmployeeManagement.give_raise(employee_id, raise_amount)

        elif choice == "9":
            # Promote Employee
            employee_id = input("Enter employee ID: ")
            new_position = input("Enter new position: ")
            EmployeeManagement.promote_employee(employee_id, new_position)

        elif choice == "10":
            # Employee Count by Department
            EmployeeManagement.employee_count_by_department()

        elif choice == "11":
            # Save Employee Data to Excel
            filename = input("Enter filename to save: ")
            EmployeeManagement.save_employee_data(filename)

        elif choice == "12":
            # Exit
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 12.")

main()

















    @classmethod
    def display_employee_details(cls):
        if not cls.employees:
            print("No employees are there..:)")
        else:
            print("Employee Details: ")
            data = []
            for employee in cls.employees:
                data.append({
                    "Employee ID": employee.employee_id,
                    "Name": employee.name,
                    "Position": employee.position,
                    "Department": employee.department,
                    "Email": employee.email,
                    "Salary": employee.salary
                })
            df = pd.DataFrame(data)
            print(df)
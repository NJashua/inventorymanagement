from flask import Flask, jsonify, request
import pandas as pd
import uuid
from sampledata import employees_data

app = Flask(__name__)

class Employee:
    def __init__(self, name, position, department, email, salary):
        self.employee_id = str(uuid.uuid4())[:6]
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
        return f'Employee {employee.name} added successfully with ID: {employee.employee_id}'
    
    @classmethod
    def display_employee_details(cls):
        if not cls.employees:
            return "No employees found."
        else:
            employee_datails = []
            for emp in cls.employees:
                employee_datails.append({
                    "Employee ID": emp.employee_id,
                    "Name": emp.name,
                    "Position": emp.position,
                    "Department": emp.department,
                    "Email": emp.email,
                    "Salary": emp.salary
                })
            return {'employee_details' : employee_datails}
    
    @classmethod
    def display_department_details(cls, department):
        if department not in cls.departments:
            return f"No employees found in department {department}"
        else:
            data = {
                "Employee ID": [],
                "Name": [],
                "Position": [],
                "Department": [],
                "Email": [],
                "Salary": []
            }
            for employee in cls.departments[department]:
                data["Employee ID"].append(employee.employee_id)
                data["Name"].append(employee.name)
                data["Position"].append(employee.position)
                data["Department"].append(employee.department)
                data["Email"].append(employee.email)
                data["Salary"].append(employee.salary)
                
            df = pd.DataFrame(data)
            # count = len(cls.departments[department])
            return df.to_dict(orient='records')

    @classmethod
    def update_employee_details(cls, employee_id, **kwargs):
        for employee in cls.employees:
            if employee.employee_id == employee_id:
                employee.update_details(**kwargs)
                return f"Details updated successfully for employee ID {employee_id}"
        return f"No employee found with ID {employee_id}"
    
    @classmethod
    def remove_employee(cls, employee_id):
        for employee in cls.employees:
            if employee_id == employee.employee_id:
                cls.employees.remove(employee)
                cls.departments[employee.department].remove(employee)
                return f'Employee {employee.name} removed successfully'
        return f"No employee found with ID: {employee_id}"
    
    @classmethod
    def total_salary_expense(cls):
        total_salary = sum(employee.salary for employee in cls.employees)
        return f'Total salary expense: INR {total_salary}'
    
    @classmethod
    def search_employee_by_name(cls, name):
        found_employees = []
        for employee in cls.employees:
            if name.lower() == employee.name.lower():
                found_employees.append({
                    'Employee ID': employee.employee_id,
                    'Name': employee.name,
                    'Position': employee.position,
                    'Department': employee.department,
                    'Email': employee.email,
                    'Salary': employee.salary
                })
        if not found_employees:
            return "Employee not found"
        else:
            return found_employees
    
    @classmethod
    def salary_hike(cls, employee_id, raise_amount):
        for employee in cls.employees:
            if employee.employee_id == employee_id:
                employee.salary += raise_amount
                return f"Salary increased successfully for employee {employee.name}. New salary: ${employee.salary}"
        return f"No employee found with ID: {employee_id}"

    @classmethod
    def promote_employee(cls, employee_id, new_position):
        for employee in cls.employees:
            if employee_id == employee.employee_id:
                employee.position = new_position
                return f"Employee {employee.name} promoted to {new_position}"
        return f"No employee found with ID: {employee_id}"

    @classmethod
    def save_employee_data(cls, filename):
        try:
            if not filename.endswith('.xlsx'):
                filename += '.xlsx'
        
            data = {
                "ID": [employee.employee_id for employee in cls.employees],
                "NAME": [employee.name for employee in cls.employees],
                "POSITION": [employee.position for employee in cls.employees],
                "DEPARTMENT": [employee.department for employee in cls.employees],
                "EMAIL": [employee.email for employee in cls.employees],
                "SALARY": [employee.salary for employee in cls.employees]
            }
            df = pd.DataFrame(data)
            df.to_excel(filename, index=False)  # Save data to Excel file
            return f"Employee data saved to {filename}"
        except AttributeError as e:
            return f"AttributeError occurred: {e}"

    @classmethod
    def employee_count_by_department(cls):
        count_by_department = {}
        for department, employees in cls.departments.items():
            count_by_department[department] = len(employees)
        return count_by_department
    
    @classmethod
    def total_revenue_of_company(cls, authorization):
        if authorization == "CEO":
            total_salary_of_employees = sum(employee.salary for employee in cls.employees)
            total_income_of_company = (total_salary_of_employees) * 12
            return f"Total salary paying to employees: INR {total_salary_of_employees}", f"The total Revenue of Company is: INR {total_income_of_company}"
        else:
            return "Unauthorized", ""

# Initialize employees
for employee_info in employees_data:
    EmployeeManagement.add_employee(Employee(*employee_info))

# Routes
@app.route('/add_employee', methods=['POST', 'GET'])
def add_employee():
    if request.method == 'POST':
        data = request.json
        return {'message': EmployeeManagement.add_employee(Employee(**data))}
    elif request.method == 'GET':
        return {'message': "Use POST method to add an employee."}


@app.route('/display_employee_details', methods=['GET'])
def display_employee_details():
    employee_details_df = EmployeeManagement.display_employee_details()
    if isinstance(employee_details_df, str):
        return {'message': 'No employee details found.'}
    else:
        return  employee_details_df

@app.route('/display_department_details/<department>', methods=['GET'])
def display_department_details(department):
    details = EmployeeManagement.display_department_details(department)
    if not details:  # Checking if details are empty
        return {'message': f'No employees found in department {department}'}
    return {'department_details': details}

@app.route('/update_employee_details/<employee_id>', methods=['PUT'])
def update_employee_details(employee_id):
    data = request.json
    return jsonify({'message': EmployeeManagement.update_employee_details(employee_id, **data)})

@app.route('/remove_employee/<employee_id>', methods=['DELETE'])
def remove_employee(employee_id):
    return jsonify({'message': EmployeeManagement.remove_employee(employee_id)})

@app.route('/total_salary_expense', methods=['GET'])
def total_salary_expense():
    return jsonify({'message': EmployeeManagement.total_salary_expense()})

@app.route('/search_employee_by_name/<name>', methods=['GET'])
def search_employee_by_name(name):
    return jsonify({'results': EmployeeManagement.search_employee_by_name(name)})

@app.route('/salary_hike/<employee_id>/<raise_amount>', methods=['PUT'])
def salary_hike(employee_id, raise_amount):
    return jsonify({'message': EmployeeManagement.salary_hike(employee_id, raise_amount)})

@app.route('/promote_employee/<employee_id>/<new_position>', methods=['PUT'])
def promote_employee(employee_id, new_position):
    return jsonify({'message': EmployeeManagement.promote_employee(employee_id, new_position)})

@app.route('/save_employee_data/<filename>', methods=['GET'])
def save_employee_data(filename):
    return jsonify({'message': EmployeeManagement.save_employee_data(filename)})

@app.route('/employee_count_by_department', methods=['GET'])
def employee_count_by_department():
    return jsonify({'count_by_department': EmployeeManagement.employee_count_by_department()})

@app.route('/total_revenue_of_company/<authorization>', methods=['GET'])
def total_revenue_of_company(authorization):
    return jsonify({'message': EmployeeManagement.total_revenue_of_company(authorization)})

# Routes
@app.route('/available_departments', methods=['GET'])
def available_departments():
    return jsonify({'departments': list(EmployeeManagement.departments.keys())})


if __name__ == "__main__":
    app.run(debug=True)

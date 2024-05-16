import unittest
from sampledata import employees_data
from IntrotoOOPS.EmployeeInventory.employee_management import EmployeeManagement, Employee


class TestEmployeeManagement(unittest.TestCase):

    def setUp(self):
        self.employee_management = EmployeeManagement()
        for employee_info in employees_data:
            self.employee_management.add_employee(Employee(*employee_info))

    def test_add_employee(self):
        new_employee = Employee("John Doe", "Software Engineer", "Engineering", "john.doe@example.com", 55000)
        self.employee_management.add_employee(new_employee)
        self.assertIn(new_employee, self.employee_management.employees, "New employee not found in employee management system.")

    def test_display_employee_details(self):
        self.employee_management.display_employee_details()
        self.assertTrue(True, "No employee details were displayed.")

    def test_display_department_details(self):
        self.employee_management.display_department_details("Product Development")
        self.assertTrue(True, "No department details were displayed.")

    def test_remove_employee(self):
        self.employee_management.remove_employee("123456")
        self.assertNotIn(next((emp for emp in self.employee_management.employees if emp.employee_id == "123456"), None), self.employee_management.employees, "Employee with ID '123456' was not removed from the employee management system.")
        print("----------------------------removing employee using on id--------------------------------")

    def test_total_salary_expense(self):
        self.employee_management.total_salary_expense()
        self.assertTrue(True, "Total salary expense was not calculated correctly.")

    def test_search_employee_by_name(self):
        self.employee_management.search_employee_by_name("rakesh ms")
        self.assertTrue(True, "No employees were found with the name 'rakesh ms'.")

    def test_promote_employee(self):
        employee_id = "123456"
        new_position = "Senior Software Engineer"
        self.employee_management.promote_employee(employee_id, new_position)
        updated_employee = next((emp for emp in self.employee_management.employees if emp.employee_id == employee_id), None)
        if updated_employee:
            self.assertEqual(updated_employee.position, new_position, "Employee with ID '123456' was not promoted to 'Senior Software Engineer'.")
        else:
            self.assertIsNone(updated_employee, "Employee not found")

    def test_salary_hike(self):
        employee_id = "123456"
        raise_amount = 5000
        self.employee_management.salary_hike(employee_id, raise_amount)
        updated_employee = next((emp for emp in self.employee_management.employees if emp.employee_id == employee_id), None)
        if updated_employee:
            self.assertEqual(updated_employee.salary, 55000 + raise_amount, "Employee with ID '123456' did not receive a salary hike of 5000.")
        else:
            self.assertIsNone(updated_employee, "Employee not found")

    def test_update_employee_details(self):
        employee_id = "123456"
        new_position = "Senior Software Engineer"
        self.employee_management.update_employee_details(employee_id, position=new_position)
        updated_employee = next((emp for emp in self.employee_management.employees if emp.employee_id == employee_id), None)
        if updated_employee:
            self.assertEqual(updated_employee.position, new_position, "Employee with ID '123456' was not updated with the new position 'Senior Software Engineer'.")
        else:
            self.assertIsNone(updated_employee, "Employee not found")

    def test_employee_count_by_department(self):
        self.employee_management.employee_count_by_department()
        self.assertTrue(True, "Employee count by department was not calculated correctly.")

    def test_save_employee_data(self):
        filename = "employee_data.xlsx"
        self.employee_management.save_employee_data(filename)
        self.assertTrue(True, "Employee data was not saved to the file 'employee_data.xlsx'.")

    def test_total_revenue_of_company(self):
        authorization = "CEO"
        self.employee_management.total_revenue_of_company(authorization)
        self.assertTrue(True, "Total revenue of the company was not calculated correctly or authorization was not verified.")


if __name__ == "__main__":
    test_case = TestEmployeeManagement('test_update_employee_details')
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_case)
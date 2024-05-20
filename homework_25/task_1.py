import json


class Employee():
    def __init__(self, name: str, position: str, salary: float) -> None:
        self.name = name
        self.position = position
        self.salary = salary


class Department():
    def __init__(self, name: str, description: str, employees: list) -> None:
        self.name = name
        self.description = description
        self.employees = employees
    
    def average(self):
        if not self.employees:
            return "No data found for average salary"
        total_salary = sum(emp.salary for emp in self.employees)
        return total_salary / len(self.employees)
    
    def max(self):
        if not self.employees:
            return "No data found for max salary"
        return max(emp.salary for emp in self.employees)

    def min(self):
        if not self.employees:
            return "No data found for min salary"
        return min(emp.salary for emp in self.employees)
    
    def positions(self):
        all_positions = {}
        for emp in self.employees:
            if emp.position not in all_positions:
                all_positions[emp.position] = 1
            else:
                all_positions[emp.position] += 1
        
        if not all_positions:
            print("     - No data found for positions")
            return 
        
        for position, amount in all_positions.items():
            print(f"     - {position}:\n          - number of employees: {amount}")
            
    
def read_json_file(file_path):
    try:
        with open(file_path, "r") as data_file:
            departments_details = json.load(data_file)
        return departments_details
    except FileNotFoundError as fnfe:
        print("Couldn't find the file", fnfe)


def main():
    print()
    file_path = "homework_25/resources/employees.json"
    
    departments = read_json_file(file_path)
    if not departments:
        print("File is empty.")
        return 
    
    all_departments = []
    for _, department_details in departments.items():
        department_name = department_details['name']
        description = department_details['description']
        employees = department_details['employees']
        
        all_employees = []
        for employee in employees:
            empl = Employee(
                name=employee['name'],
                position=employee['position'],
                salary=float(employee['salary'])
            )
            all_employees.append(empl)
        
        department = Department(
            name=department_name,
            description=description,
            employees=all_employees
        )
        all_departments.append(department)
    print()

    for dept in all_departments:
        print(f"                   {dept.name}")
        print(f"> Description: \n     - {dept.description}")
        print(f"> Average Salary: \n     - {dept.average()}")
        print(f"> Max Salary: \n     - {dept.max()}")
        print(f"> Min Salary: \n     - {dept.min()}")
        print(f"> Positions: ")
        dept.positions()
        print("\n")

if __name__ == "__main__":
    main()

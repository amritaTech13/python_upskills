# Assignment -2 :
 
# Write a Python script that:
# Stores employee data in a dictionary
# Can add, update, and delete employees
# Uses a list of dicts to store multiple employee records
# Use OOPS concept (mandatory)
# utilize for loop

class Employees:
    def __init__(self):
        self.employees = []

    def add(self, name, id, position,dept,salary):
            self.employees.append({'name':name, 
                                 'id':id,
                                 'Position':position,
                                 'Department':dept,
                                 'Salary':salary
                                 })
    def update(self, id, salary):
        for emp in self.employees:
            if emp['id'] == id:
                emp['salary'] = salary
                print(f"Salary updated for {emp['name']}")
                return
        print("OOPs...,You cannot update empty records")

    def delete(self, id):
        for emp in self.employees:
            if emp['id'] == id:
                 self.employees.remove(emp)  
                 print(f"Employee {emp['name']} has been removed from records")  
                 return
        print(f"There is no reacodrs forn for this employee {emp['name']}")   

    def print_emp(self):
         for emp in  self.employees:
              print(emp)  

emp1 = Employees()
emp1.add("Amrita", 2260,'developer','Microsoft', 10000)
emp1.add("Anu", 2261,'Tester','Microsoft', 50000)
emp1.add("Ankita", 2262,'DevOp','Microsoft', 40000)
emp1.add("Sandeep", 2263,'Java','Microsoft', 40000)
emp1.print_emp()
emp1.update(2263, 13000)
emp1.print_emp()
emp1.delete(2263)
emp1.print_emp()
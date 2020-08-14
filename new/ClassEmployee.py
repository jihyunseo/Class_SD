class Employee:
    empCount=0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount+=1
    def displayEmployee(self):
        print("Total Employee",Employee.empCount)
    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    # from ClassEmployee import Employee as emp
    # emp1=emp("Zara",2000)
    # emp2=emp("Manni",5000)
    # emp1.displayEmployee()
    # emp2.displayEmployee()
    
    # import ClassEmployee as emp
    # emp1=emp.Employee("Zara,2000")
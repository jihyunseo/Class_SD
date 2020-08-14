print('hello! 1')
print('hello! 2')
print('hello! 3')
print('hello! 4')
print('hello! 5')
print('hello! 6')

class Athlete:
    def __init__(self, value='Jane'):
        self.thing= value;
    def getAthlete(self):
        return self.thing

a=Athlete()
a.getAthlete()
b=Athlete('Holy')
Athlete.__init__(a,'Holy')
b.getAthlete()

print(a.getAthlete())
print(b.getAthlete())

class Point:
    def __init__(self, x=0,y=0):
        self.x=x
        self.y=y
    def innerPrint(self, infor):
        print(infor, self.x, self.y)

pt1=Point()
print('point01 class', pt1.x,',',pt1.y)
pt2=Point(3,5)
print('point02 class',pt2.x,',',pt2.y)
pt2.innerPrint('point02 innerprint:')

# emp1 = employee("Zara", 2000)
# Print(emp1.name,emp1.salary)

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

emp1 = Employee("Zara", 2000); 
emp2 = Employee("Manni",5000)
emp1.displayEmployee();
emp2.displayEmployee()
print("Total Employee",Employee.empCount)

from ClassEmployee import Employee as emp
emp1=emp("Zara",2000)
emp2=emp("Manni",5000)
emp1.displayEmployee()
emp2.displayEmployee()
    
import ClassEmployee as emp
emp1=emp.Employee("Zara",2000)

class NamedList(list):
    def __init__(self,a_name):
        list.__init__([])
        self.name=a_name
        self.dob=None
johnny=NamedList('John Paul Jones')
normelvar=3
johnny.dob='2017.10.10'
johnny.extend(['Composer','Arranger','Musician'])
for attr in johnny:
    print(johnny.name+'is a '+attr+'.-'+johnny.dob)


import pickle
favorite_color={"lion":"yellow","kitty":"red"}
pickle.dump( favorite_color, open( "save.pkl", "wb" ) )
favorite_color_load = pickle.load( open( "save.pkl", "rb" ) )
favorite_color_load

from ClassEmployee import Employee as emp
emp1=emp("Zara",2000)
emp1.displayEmployee()

import pickle
pickle.dump(emp1,open("./emp1.pkl","wb"))
print('dump pickle')
emp1_pkl=pickle.load(open("./emp1.pkl","rb"))
print('load pickle')
emp1_pkl.displayEmployee()
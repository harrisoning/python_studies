class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def __dir__(self):
        return ['name', 'salary']

    def displayCount(self):
        print (f"Total Employee {Employee.empCount}" )

    def displayEmployee(self):
        print (f"Name: {self.name}, Salary: {self.salary}")
        
    def __secretAccess(self, access):
        print (f"{self.name} have secret {access}!")

    def tellSecretAccess(self, access):
        self.__secretAccess(access)

class Manager(Employee):
    '管理人员'

    def __init__(self, name, salary, title):
        super().__init__(name, salary)
        self.title = title

    def myDuty(self, duty):
        print(f'My job duty is to {duty}')

    
if __name__ == '__main__':
    # 创建 Employee 类的对象
    emp1 = Employee("Zara", 2000)
    emp2 = Employee("Manni", 5000)
    emp3 = Employee("Harrison", 10000)

    emp1.displayEmployee()
    emp2.displayEmployee()
    emp3.displayEmployee()

    emp3.displayCount()

    emp3.tellSecretAccess("Admin Power")



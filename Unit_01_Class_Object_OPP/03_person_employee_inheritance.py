#CreatedBy: LE VAN DIEP

#supper class Person, supclass Employee
class Person:
    def __init__(self, fullName, gender, birthday):
        self.fullName = fullName
        self.gender = gender
        self.birthday = birthday
    
    def display_info(self):
        print("Fullname: ", self.fullName)
        print("Gender: ", self.gender)
        print("Birthday: ", self.birthday)

#subclass is can inheritance the multi supper class    
class Employee(Person):
    #this is pulic param, want to get or set: 'Employee.base_salary'
    base_salary = 2000000
    def __init__(self, fullName, gender, birthday, code, number_of_salary):
        #call init of Person class
        Person.__init__(self, fullName, gender, birthday)
        self.code = code
        self.number_of_salary = number_of_salary

    def display_info(self):
        print("* "*30)
        print("Employee Code: ", self.code)
        Person.display_info(self)
        print("Number of salary: ", self.number_of_salary)       
        print("Current salary: ", self.get_salary())         
        #format currency
        print("Current salary has format: ", "{:,.2f}".format(self.get_salary()))
    
    def get_salary(self):
        return Employee.base_salary * self.number_of_salary

if __name__ == "__main__":
    #Female is False, Male is True
    person = Person("Mary Ana", False, "2000-03-24")
    person.display_info()

    employee = Employee("John Mith", True, "1990-09-14", "EMP_0001", 3)
    employee.display_info()

    #change base salary
    Employee.base_salary = Employee.base_salary + 500
    employee2 = Employee("Linda Nice", False, "1985-02-15", "EMP_0002", 5)
    employee2.display_info()

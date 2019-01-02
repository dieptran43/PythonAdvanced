import datetime

class Employee:
    def __init__(self, firstName, lastName, checkIn, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.checkIn = checkIn
        self.salary = salary
    
    def showInfo(self):
        print("Full Name: ", self.firstName +" "+ self.lastName)
        # print("Check in: ", self.checkIn)        
        # print("Salary: ", self.salary)
        print("Check in: ", self.checkIn.strftime("%d/%m/%Y"))
        print("Salary: ", "$ {:,.2f}".format(self.salary))
        print("#" * 50)


#####################################
#create method new instance Employee
def create_employee(data):
    infors = data.split(",")
    firstName = infors[0].strip()
    lastName = infors[1].strip()
    #checkIn = infors[3].strip()
    checkIn = datetime.datetime.strptime(infors[3].strip(), "%d/%m/%Y")
    salary =  float(infors[2].strip())
    return Employee(firstName, lastName, checkIn, salary)

#return list employee
def create_list_employees(file_name):
    lstEmployees = []
    f = open(file_name,"r", encoding="utf-8")
    for line in f:
        data = line.strip()
        emp = create_employee(data)
        lstEmployees.append(emp)
    f.close()
    return lstEmployees

#view infor of employee
def print_list_employee(list_emp):
    total = 0
    for emp in list_emp:
        emp.showInfo()
        total += emp.salary
    return total

if __name__ == "__main__":
    # obj1 = Employee("Smith", "Honda", "20/12/2018", 5000)
    # obj1.showInfo()

    lstEmployees = create_list_employees("./data/employee.txt")
    total = print_list_employee(lstEmployees)
    print("Sum total of salary: ", "$ {:,.2f}".format(total))
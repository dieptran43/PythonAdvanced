from a_05_excercise import *

if __name__ == "__main__":
    lstEmployee = create_list_employees("./data/employee.txt")
    print_list_employee(lstEmployee)    

# f = open("./data/employee.txt","r", encoding="utf-8")
# for line in f:
#     data = line.strip()
#     print(data)
#     infors = data.split(",")
#     print("Fist name: ",infors[0].strip())
#     print("Last name: ",infors[1].strip())
#     print("Salary: ",infors[2].strip())
#     print("Check in: ",infors[3].strip())
#     print("*" * 50)
# f.close()
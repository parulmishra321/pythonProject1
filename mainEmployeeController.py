from Employee import *

def main():

    employee = Employee(employeeList)

    while True:
        print("*************************************WELCOME***********************************")
        print()
        print("1. Print all details of employees in descending order of salary")
        print("2. Store all the Employee List using EmpId as a key")
        print("3. Remove element if EmpId is duplicate")
        print("4. Update employee salary for EmpId 101")
        print("5. Search employee whose EmpId is 101 using lambda function")
        print("6. Update the details of employees by splitting empName into firstName and lastName")
        print("7. Exit.")
        print("*******************************************************************************")
        print()
        try:
            choice = int(input("Enter Your Choice: "))
            if (choice == 1):
                print("Details of employee:")
                employee.displayEmployeeDetails()
            elif (choice == 2):
                print("Details of employee store id as key:")
                employee.storeEmpIdAsKey()
            elif (choice == 3):
                print("Details of employee after removing duplicate id:")
                employee.removeEmpById()
                employee.displayEmployeeDetails()
            elif (choice == 4):
                print("Details of employee after updating salary for Emp ID 101:")
                employee.updateSalary(101,50000)
                employee.displayEmployeeDetails()
            elif (choice == 5):
                print("Details of employee with Emp ID 101 after seaching using lambda function :")
                employee.searchEmployee(101)
            elif (choice == 6):
                print("Details of employee after splitting name into firstname and lastname:")
                employee.splittingEmployeeName()
            elif (choice == 7):
                break;
            else:
                print("INVALID INPUT!! TRY AGAIN")
        except Exception as e:
            print(e)
            print("INVALID DETAILS!! TRY AGAIN")

if __name__ == "__main__":
    main()





class Employee:

    def __init__(self, employeeList):
        self.employeeList = employeeList

    def displayEmployeeDetails(self):
        for emp in employeeList:
            print(emp)

    keyList = {}

    def storeEmpIdAsKey(self):
        for emp in employeeList:
            self.keyList[emp[0]] = dict(zip(["EmpID", "EmpName", "Salary"], emp))
        print(self.keyList)

    def removeEmpById(self):
        tempList = []
        for emp in employeeList:
            if emp not in tempList:
                tempList.append(emp)
            else:
                employeeList.remove(emp);

    def updateSalary(self,empId, newSalary):
        for emp in employeeList:
            if emp[0] == empId:
                emp[2] = newSalary

    def searchEmployee(self, empId):
        searchList = list(filter(lambda emp: emp[0] == empId, employeeList))
        print(searchList)


    def splittingEmployeeName(self):
        tempList = {}
        for emp in employeeList:
            tempList["EmpId"] = emp[0]
            firstName, lastName = emp[1].split(" ")
            tempList["FirstName"] = firstName
            tempList["LastName"] = lastName
            tempList["Salary"] = emp[2]
        print(tempList)

employeeList =[
    [101, "ABC abc", 10000],
    [102, "XYZ xyz", 20000],
    [102, "XYZ xyz", 20000],
    [103, "XCB ncb", 5000]
]










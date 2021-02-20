import operator

class Employee:

    maxEmployees = 5
    minEmployees = 2
    SaleCommission = 500.0

    def __init__(self):
        self.id = self.getEmployeeId()
        self.name = self.getEmployeeName()
        self.properties = self.getProperties()
        self.salesCommission = self.getSalesCommission(self.properties)

    def printEmployeeDetails(self):
        #Still to format the printing here
        return self.id, self.name, self.properties, self.salesCommission
    
    def getEmployeeId(self):
        #validate input and return method
        return input("Employee ID >")
        
    def getEmployeeName(self):
        #validate input and return method
        return input("Employee Name >")

    def getProperties(self):
        #validate input and return method
        return int(input("How may properties sold? > "))
    
    def getSalesCommission(self, noProperties):
        return noProperties*Employee.SaleCommission

#main program
#validation required to improve
#basic principles implemented
employee=[]
bonus =0.15

#getNumber of employees
while True:

    #get number of employees
    noOfEmployees = int(input("How many employees > "))
    #check between Min and Max no of employees
    if Employee.minEmployees<=noOfEmployees<=Employee.maxEmployees:
        break
    else:
        print("Must be between 2 and 5 employees.")
        print("Try again please!!")

#Create employee instances
for loop in range(noOfEmployees):
    employee.append(Employee())


#ranking/sorting the employees by highest sales person, ie employee[0]
employee.sort(key=operator.attrgetter('properties'), reverse=True)

print("Rank order Highest to Lowest Property Sales")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
for loop in range(noOfEmployees):
    print(employee[loop].printEmployeeDetails())
print("-=-=--=-=-=-=-=-=-==--=-=-=---==-=-=-=--=---=")

#calculate a bonus to employee with highest sales
print("Therefore, {0} is entitled to a {1} bonus" \
.format(employee[0].name, employee[0].salesCommission*bonus))





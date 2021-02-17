import operator

class Student:

    #constructor
    def __init__(self):
        self.name = self.inputName()
        self.web = self.validateMarks("Web")
        self.programming = self.validateMarks("Programming")
        self.graphics = self.validateMarks("Graphics")
        self.networks = self.validateMarks("Networks")
        self.mean = self.getMean()
        self.grade = self.getGrade()

    #methods

    def getTotal(self):
        return (self.web+self.programming+ \
                self.graphics+self.networks)
    
    def getMean(self):
        return round(self.getTotal()/4,0)

    def getGrade(self):
        if 0<=self.mean<=39:
            return "F"
        elif 40<=self.mean<=49:
            return "D"
        elif 50<=self.mean<=59:
            return "C"
        elif 60<=self.mean<=69:
            return "B"
        elif 70<=self.mean<=100:
            return "A"                     
        else:
            return "X"

    def printStudentDetails(self):
        return(self.name,self.web,self.programming,\
          self.graphics,self.networks, \
          self.mean,self.grade)

    def inputName(self):
        name=input("Enter Name of Student > ")
        return name
    
    def validateMarks(self,id):
        while True:
            mark=input(id+":Give a mark > ")
            try:
                 mark=int(mark)
                 if 0<=mark<=100:
                     break
                 else:
                     print("Mark out of range(0-100)")
            except:
                print("Invalid input, try again!")
        return mark        
        


#MAIN PROGRAM###########################################################
    
#INITIALISE a list to store instances(objects) of the class Student
#It has to be empty at first as you dont know how many students
student=[]

#INPUT - "Requires a change here" to ask and validate user for "how many student between
#1 and 5.  Here I have set it at 3 students
noOfStudents=3
for loop in range(noOfStudents):
    student.append(Student())

#sort the students by Mean score, uses operator library as neat solution
#to sorting objects stored in a list, using a key attribute.
student.sort(key=operator.attrgetter('mean'), reverse=True)

#OUTPUT - all sorted student attributes by calling a method
for i in range(noOfStudents):
    print(student[i].printStudentDetails())
    






    



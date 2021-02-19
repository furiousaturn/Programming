class Customer:
    
    #constructor
    def __init__(self,id):
        self.id = id
        self.name=self.getCustomerDetails("name")
        self.address=self.getCustomerDetails("address")
        self.phone=self.getCustomerDetails("phone")

    #methods
    def printCustomerDetails(self):
        return self.id, self.name,self.address,self.phone

    def getCustomerDetails(self,attr):
        #validation can be added for these (i.e. str length >0)
        aString=input("Enter {} of Customer > ".format(attr))
        return aString

class Pizza:
    pizzaMin,pizzaMax = 1,6

    small,medium,large = 3.25,5.50,7.15
    topping1,topping2,topping3,toppingMore = 0.75,1.35,2.00,2.50

    def __init__(self, custId):
        self.custId = custId
        self.size = self.getSize()
        self.topping = self.getTopping()
        self.cost = self.size+self.topping

    def printPizzaDetails(self,custId):
        return self.custId, self.size, self.topping,self.cost

    def getSize(self):
        #validation required

        print("Pizza size:")
        print("=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=")
        print("1=small, 2=Medium, 3=Large >")

        size=int(input("Enter size no. >" ))
        if (size == 1): return Pizza.small
        elif (size == 2): return Pizza.medium
        elif (size ==3): return Pizza.large

    
    def getTopping(self): 
        #validation required
        
        print("Toppings:")
        print("=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=")
        print("1, 2, 3 or 4 (or more) > ")

        toppings=int(input("Enter no. of toppings >" ))
        if (toppings  == 1): return Pizza.topping1
        elif (toppings == 2): return Pizza.topping2
        elif (toppings == 3): return Pizza.topping3
        elif (toppings == 4): return Pizza.toppingMore
    
#main program
#Initialise list, number of pizzas for custId = 0
customer=[]
custId=0

pizza=[]
noOfPizzas=2

#create a customer id=0
customer.append(Customer(custId))

#repeat for noOfPizzas
for loop in range(noOfPizzas):
    pizza.append(Pizza(custId))

print("Customer id=0")
print("-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-==---=")
print(customer[custId].printCustomerDetails())

print("-=-=--=-Pizzas ordered, Custid = 0-=-=---=-")

for loop in range(noOfPizzas):
    print(pizza[loop].printPizzaDetails(custId))

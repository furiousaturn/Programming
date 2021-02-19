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
        self.topping= self.getTopping()
        self.cost = self.getCost()

    def printPizzaDetails(self,custId):
        return self.custId, self.size, self.topping,self.cost

    def getSize(self):
        print("Pizza size:")
        print("=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=")
        print("1=small, 2=Medium, 3=Large >")

        size=int(input("Enter size no. >" ))
        if (size == 1): return Pizza.small
        elif (size == 2): return Pizza.medium
        elif (size ==3): return Pizza.large

    
    def getTopping(self): 
        return Pizza.topping1
    
    def getCost(self):
        return 3.40



#main program
customer=[]
customer.append(Customer(0))
print(customer[0].printCustomerDetails())

pizza=[]
pizza.append(Pizza(0))
print(pizza[0].printPizzaDetails(0))
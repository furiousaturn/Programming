class Customer:
    
    def __init__(self):
        self.amountGBP = self.getAmountGBP()
        self.amountCurrency = self.getCurrencyRate()
        self.transactionFee = self.getTransactionFee(self.amountCurrency)
        self.totalCost = self.amountGBP + self.transactionFee
        self.staffMember = self.isStaff()

    def getAmountGBP(self):
        return float(input("Input GBP to convert >>> "))

    def getTransactionFee(self,gbp):

        if 0.0<=gbp<=300.0: return 0.035
        elif 300.0<gbp<=750.0: return 0.030
        elif 750.0<gbp<=1000.0: return 0.025
        elif 1000.0<gbp<=2000.0: return 0.020
        elif gbp > 2000.0: return 0.020

    def getCurrencyRate(self):
        #validation required
        ctype =[["USD",1.40],["EUR",1.14],["BRL",4.77],["JPY",151.05],["TRY", 5.68]]
        
        for id in range(5):
            print(id+1, ctype[id][0])
        
        selection = int(input("Make Selection >>> "))
        
        return ctype[selection-1][1]
    
    def isStaff(self):
        sm=input("Staff member (Y/N)? >> ")
        if (sm=="Y") or (sm == "y"):
            return True
        else:
            return False

#MAIN PROGRAM
customer = Customer()

print(customer.amountGBP)
print(customer.amountCurrency)
print(customer.transactionFee)

if customer.staffMember:
    print("Staff discount amount = {:.2f}".format(float(customer.totalCost)*0.05))
    print("Total cost = {:.2f} ".format(float(customer.totalCost)*0.95))
else:
    print("Total cost = {:.2f}".format(float(customer.totalCost)))









def GetAmount():
 while True:
   GBP = input("Enter GBP Amount to Convert: ")

   try:
     GBP=float(GBP)
     if GBP > 0 and GBP <= 2500:
       break
     else:
       print("Error: Amount cannot be more than £2500")
   except:
     print("Error: Amount Invalid")

 return GBP


def ExchangeRate():
             
        while True:
            print("1 = USD")
            print("2 = EUR")
            print("3 = BRL")
            print("4 = JPY")
            CurrencyType = input("Enter Option: ")
            try:
                CurrencyType=int(CurrencyType)
                
                if CurrencyType > 0 and CurrencyType <5:
                    break
                else:
                    print("Out of range, try again!")
            except:
                print("Error: Please make a valid selection")
            
        if CurrencyType == 1:
            ExchangeRate = 1.40
        elif CurrencyType == 2:
            ExchangeRate = 1.14
        elif CurrencyType == 3:
            ExchangeRate = 4.77
        elif CurrencyType == 4:
            ExchangeRate = 151.05
        
        return ExchangeRate

def TransactionFee(GBP):
    if GBP > 2000:
        TransactionFee = GBP * (1.5/100)
    elif 2000 > GBP >= 1000:
        TransactionFee = GBP * (2/100)
    elif 1000 > GBP >= 750:
        TransactionFee = GBP * (2.5/100)
    elif 750 > GBP >= 300:
        TransactionFee = GBP * (3/100)
    else:
        TransactionFee = GBP * (3.5/100)
    return TransactionFee

def ConvertCurrency(GBP, ExchangeRate):
    conversion = GBP * ExchangeRate
    return conversion


def getDiscount():
    while True:
        staffMember = input("Are you a Staff Member? (Y/N)")
    
        if staffMember in ["y","Y","n","N"]:
            break
        else:
            print("A Y or N required, try again")

    if staffMember in ["y","Y"]:
        discounted = 0.95
    else:
        discounted = 1
        
    return discounted

#main program#########################

#Enter amount in pounds - validated        
GBP = GetAmount()

#Choose currency and return the exchange rate for that currency
er=ExchangeRate()

#Converts amount into chosen currency
convertedAmount = ConvertCurrency(GBP,er)

#calculates a transaction fee based on Amount entered
tf=TransactionFee(GBP)

#determines discount amount
discount=getDiscount()

#calculates and prints total cost, given the scenario
totalCost = (convertedAmount+tf)*discount
print("Total Cost is £{:.2f}".format(totalCost))
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("-->Where Transaction fee was £{:.2f}".format(tf))
if discount !=1:
    print("-->Where Staff discount was applied at 5%")
print("-->Where exchange rate used was {:.2f}".format(er))

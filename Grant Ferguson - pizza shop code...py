def CustomerDetails():
  global Name
  global Address

  while True:
    Name = str(input("What Is Your Name?"))
    Address = input("Please Enter Your Address")
    PhoneNumber = int(input("What Is Your Phone Number"))
    try:
      if PhoneNumber.length == 11:
          print ("Accpeted")
      elif:
          print ("Error, Incorrect Number")
    except:
      print ("Error, Invalid")

  return Name
  return Address
     


def getQuantityPizza():
  Error = True:
  while Error == True:
    try:
      Quantity = int(input("Enter the number of pizzas you want"))
      if Quantity < 1:
        print("The number of pizzas cannot be less than 1, try again.")
      elif Quantity > 6:
        print("The number of pizzas cannot be less than 6.")
      else:
        Error = False
    except:
      print("Input was not a number, try again.")
  return Quantity

Quantity = getQuantityPizza()
print(Quantity)
    
def GetPizzaSize(quantity):
  sizes = []
  while len(sizes) < quantity: 
    size = (input("What Size Pizza Do You Want? (Options: S, M, L) ")).upper()
    if size == "S":
      sizes.append(3.25)
    elif size == "M":
      sizes.append(5.50)  
    elif size == "L":
      sizes.append(7.15)
    else:
      print ("Error try Again")
  return sizes

def ExtraToppings(Quantity):
  toppings= []
  while len (toppings) < Quantity:
    topping = int(input("How Many Extras Toppings Would You Like?")).title()
    if topping == 0:
      toppings.append(0)
    elif topping == 1:
      toppings.append(0.75)
    elif topping == 2:
      toppings.append(1.35)
    elif topping == 3:
      toppings.append(2.00)
    elif toppings == 4:
      toppings.append(2.50) 
    else:
      print("Error, Please Try Again") 
    
    return toppings

def DeliveryCharge():
  
def printBill(CustomerDetails, PizzaQuantity, PizzaSize, ExtraToppings, DeliveryCharge, DiscountApplied):

  print(CustomerDetails)
  print(PizzaQuantity)
  print(PizzaSize)
  print(ExtraToppings)
  print(DeliveryCharge)
  print(DiscountApplied)
  print((PizzaQuantity + PizzaSize + ExtraToppings + DeliveryCharge) - DiscountApplied)

for i in GetPizzaSize(3):
  sizeTotal = 0
  sizeTotal += i
  print(i)
print(sizeTotal)

def getDiscount(TotalCost):
  if TotalCost > 20:
    TotalCost = (TotalCost - (TotalCost * 0.1))
  else:
    TotalCost = TotalCost

  return TotalCost

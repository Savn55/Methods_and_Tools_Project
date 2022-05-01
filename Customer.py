# Customer class file

import pandas as pd
from Cart import Cart

# The idea is Customer is the main subject of all so everything revolves around 
# it. when logging in to store, customer should have username,password,fname,lname
# account info (card name, number, etc including shipping and billing addrs), and 
# customer directly controls the Cart class too (as soon as customer is signed in,
# customer is kind of assigned with cart to hold items), and definately should be
# handling file (using pandas here)
class Customer:
  def __init__(self,userName):
    self.userName = userName
    self.password = None 
    self.firstName = None
    self.lastName = None
    self.cardName = None
    self.cardNumber = None
    self.billingAddress = None
    self.billingCity = None
    self.billingState = None
    self.billingZip = None
    self.shippingAddress = None
    self.shippingCity = None
    self.shippingState = None
    self.shippingZip = None
    self.cart = Cart(userName)  ## Cart object as customer attribute in constructor
    self.readFile = 'customer.csv'
    self.customersInfo = pd.read_csv(self.readFile) ## read customer.csv file


# setting name and storing it in customer file
  def setName(self,firstName,lastName):
    self.firstName = firstName
    self.lastName = lastName
    self.customersInfo.loc[self.customersInfo['username'] == self.userName,'fname'] = firstName
    self.customersInfo.loc[self.customersInfo['username'] == self.userName,'lname'] = lastName 
    self.customersInfo.to_csv(self.readFile, index = False)

  def setPaymentInfo(self, cardName, cardNumber, billingAddr, billingCity, billingState, billingZip):
    self.cardName = cardName
    self.cardNumber = cardNumber
    self.billingAddress = billingAddr
    self.billingCity = billingCity
    self.billingState = billingState
    self.billingZIP = billingZip
    self.customersInfo.loc[self.customersInfo['username'] == self.userName, 'cardName'] = cardName
    self.customersInfo.loc[self.customersInfo['username'] == self.userName, 'cardNum'] = cardNumber
    self.customersInfo.loc[self.customersInfo['username'] == self.userName, 'billingAddr'] = billingAddr
    self.customersInfo.loc[self.customersInfo['username'] == self.userName, 'billCity'] = billingCity
    self.customersInfo.loc[self.customersInfo['username'] == self.userName, 'billState'] = billingState
    self.customersInfo.loc[self.customersInfo['username'] == self.userName, 'billZip'] = billingZip
    self.customersInfo.to_csv(self.readFile, index = False)
    print(self.customersInfo.loc[self.customersInfo['userName'] == self.userName]) 
    # prints the row (user account informations) with userName == userName


  def setShippingAddress(self, shippingAddr,shippingCity,shippingState,shippingZip):
    self.shippingAddress = shippingAddr
    self.shippingCity = shippingCity
    self.shippingState = shippingState
    self.shippingZip = shippingZip
    self.customersInfo.loc[self.customersInfo['userName'] == self.userName, 'shipAddr'] = shippingAddr
    self.customersInfo.loc[self.customersInfo['userName'] == self.userName, 'shipCity'] = shippingCity
    self.customersInfo.loc[self.customersInfo['userName'] == self.userName, 'shipState'] = shippingState
    self.customersInfo.loc[self.customersInfo['userName'] == self.userName, 'shipZip'] = shippingZip
    self.customersInfo.to_csv(self.readFile, index = False)
    print(self.customersInfo.loc[self.customersInfo['userName'] == self.userName])
    # prints the row (user account informations) with userName == userName

 
  ## returns items (books) in the cart
  def getCart(self):
    return self.cart
  
  def addUser(self, username,password):
    new_row = pd.Series({'userName':username,'password':password})
    self.customersInfo = self.customersInfo.append(new_row,ignore_index = True)
    self.customersInfo.to_csv(self.readFile, index = False)

  def isUser(self):
    if self.userName in self.customersInfo['userName'].unique():
      return True
    return False

  def checkPassword(self,username,password):
    uname = self.customersInfo.loc[self.customersInfo['userName'] == self.Username,'user'].iloc[0]
    pwd = self.customersInfo.loc[self.customersInfo['userName'] == self.Username,'password'].iloc[0]
    if uname == username and pwd == password:
      return True
    else:
      return False

  def deleteAccount(self,cart):
    self.customersInfo = self.customersInfo.drop(self.customersInfo[self.customersInfo['userName']==self.username].index)
    self.customersInfo.to_csv(self.readFile, index = False)
    print('Account is Deleted\n')
    exit()

  def printAccountDetails(self):
    df = (self.customersInfo.loc[self.customersInfo.index[self.customersInfo['user'] == self.Username]])
    print(df[['user', 'password', 'First', 'Last', 'StreetName', 'StreetNumber', 'City', 'State', 'Zip', 'CardName', 'CardNum',
     'BillingAddress', 'BillingCity', 'BillingState', 'BillingZip']])

  
  def logout(self):
    exit()


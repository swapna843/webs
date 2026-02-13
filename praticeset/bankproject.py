from abc import ABC ,abstractmethod
class Account(ABC):
  @abstractmethod
  def deposite(self,account):
    pass

  @abstractmethod
  def withdraw(self,amount):
    pass

  @abstractmethod
  def get_balanace(self):
    pass

class Bankacount(Account) :
  def __init__(self,name,acc_no,balance=0):
    self.name=name
    self.acc_no=acc_no
    self.__balance=balance

  def deposite(self,amount) :
    if(amount<=0) :
      raise ValueError("amount must be grater than 0")
    self.__balance+=amount
    print(f'deposited {amount} into account {self.acc_no}')
  def withdraw(self, amount):
    if(amount>self.__balance):
      raise ValueError("withdrawal amount exceeds balance ")
    self.__balance -=amount
    print(f"withdrawal {amount} from  account {self.acc_no}")
  def  get_balanace(self):
    return self.__balance
  def show_deatils(self):
    print(f'Name:{self.name}') 
    print(f'Account number:{self.acc_no}')
    print(f'Balance:{self.__balance}')

class SavingAccount(Bankacount):
  def withdraw(self, amount):
    if(amount>self.get_balanace()) :
      raise ValueError("withdrawal amount exceeds balance")
    print("saving account withdrawal ")
    super().withdraw(amount)


try:
  acc1=SavingAccount('swapna',1014556,10000) 
  acc1.deposite(5000)   
  acc1.withdraw(10000)
  acc1.show_deatils()
except ValueError as e:
  print("error",e)  

    

   
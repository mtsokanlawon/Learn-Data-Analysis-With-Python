class account:
   '''a type of class that holds a person's bank account details'''
   
   instance_count = 0
   @classmethod
   def increment_instance_count(cls):
      cls.instance_count += 1
      print("Number of account instances created:", cls.instance_count)

      
   message_count = 0
   @classmethod
   def increment_message_count(cls):
      cls.message_count += 1
      print('An instance has been created')
      
   def __init__(self, account_name, account_number, opening_balance, account_type, deposited, withdrew, balance):
      
      account.increment_message_count()
      self.account_name = account_name
      self.account_number = account_number
      self.opening_balance = opening_balance
      self.account_type = account_type
      self.deposited = deposited
      self.withdrew = withdrew
      self.balance = opening_balance
      
   def withdraw(self, amount):
      self.balance -= amount
      return self.balance   

   def deposit(self, amount):
      self.balance += amount
      return self.balance
   
   def get_balance(self):
      self.balance = self.opening_balance + self.deposited - self.withdrew
      return 'account balance:', self.balance

      
      

   def __str__(self):
      return "account[" + self.account_number + "] -" + self.account_name + ", " + self.account_type + " account = " + str(self.opening_balance)
   

acc1 = account('Oba', '123', 40.00, 'savings', 20, 13, 40)
print(acc1)
print('withdrew:', acc1.withdrew, 'balance:', acc1.withdraw(13))
print('deposited:', acc1.deposited, 'balance:', acc1.deposit(20))
print(acc1.get_balance())
print(account.increment_instance_count())

acc2 = account('Mercy', '456', 50.00, 'investment', 2, 0, 50)
print(acc2)
print('withdrew:', acc2.withdrew, 'balance:', acc2.withdraw(0))
print('deposited:', acc2.deposited, 'balance:', acc2.deposit(2))
print(acc2.get_balance())
print(account.increment_instance_count())

acc3 = account('Goodness', '789', 70.00, 'current', 90, 37, 70)
print(acc3)
print('withdrew:', acc3.withdrew, 'balance:', acc3.withdraw(37))
print('deposited:', acc3.deposited, 'balance:', acc3.deposit(90))
print(acc3.get_balance())
print(account.increment_instance_count())
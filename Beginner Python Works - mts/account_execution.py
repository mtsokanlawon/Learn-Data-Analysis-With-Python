from account import account

acc1 = account("123", "Mercy", 50.00, "Current")
print(acc1)
acc1.deposit(40.45)
acc1.withdraw(0)
acc1.get_balance()
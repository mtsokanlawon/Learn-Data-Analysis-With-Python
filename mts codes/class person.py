class person:
   """an example of class that holds a person's name and age"""
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def __str__(self):
      return self.name + ' is ' + str(self.age)

   def birthday(self):
      print("happy birthday you were ", self.age)
      self.age += 1
      print("You are now ", self.age)
   
   #defining instance methods
   def calculate_pay(self, hours_worked):
      hourly_pay = 40
      if self.age >= 20:
         hourly_pay += 5
      return hourly_pay * hours_worked

   def is_teenager(self):
      return self.age < 20

p1 = person('mercy', 17)
p2 = person('oba', 15)
p3 = person('goodness', 25)


print("id(p1):", id(p1))
print("info:", p1)
print(p2)
p2.birthday()
print(p2)
pay = p1.calculate_pay(50)
print(p1.name, "'s", "pay is $", pay, "per week")
pay2 = p2.calculate_pay(80)
print(p2.name, "'s", "pay is $", pay2, "per week" )
pay3 = p3.calculate_pay(40)
print(p3.name, "'s", "pay is $", pay3, "per week")

#check_age_qualification = is_teenager()
print(p3.name, 'is teenager:', p3.is_teenager())

print("class attributes")
print(person.__doc__)
print(person.__name__)
print(person.__module__)
print(person.__dict__)
print("object Attribute")
print(p1.__class__)
print(p1.__dict__)
#class person:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age

#Default string representation
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name + ' is ' + str(self.age)
        

p1 = person('john', 36)
p2 = person('Ben', 12)

print("p1:",  p1)
print("Id(p1):", id(p1))
print("p2:", p2)
print("Id(p2):", id(p2))

#update attribute
p2.name = 'Stone'
p2.age = 32

print(p1.name, 'is', p1.age)
print(p2.name, 'is', p2.age)


print(p1)


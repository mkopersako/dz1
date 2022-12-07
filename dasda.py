class Pets:
    voice = "squeaky"
    size = "little"
    legs = "4"
    def __init__(self, subtype, age, colors):
        self.subtype = subtype
        self.age = age
        self.colors = colors

print("1-ginger, 2-black, 3-white")

x1 = Pets("Guinea Pig", 1.2, 1)
x2 = Pets("Hamster", 0.7, 2)
x3 = Pets("Rat", 0.11, 3)

print(x1.subtype)
print(x1.age)
print(x1.colors)

print(x2.subtype)
print(x2.age)
print(x2.colors)

print(x3.subtype)
print(x3.age)
print(x3.colors)
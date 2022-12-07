class Cars:
    engine = "common"
    wheels = "4"
    places = "5"
    def __init__(self, brand, year, colors):
        self.brand = brand
        self.year = year
        self.colors = colors

print("1-yellow, 2-blue, 3-black")

x1 = Cars("Land Rover", 2018, 3)
x2 = Cars("Toyota", 2014, 2)
x3 = Cars("Mercedes", 2016, 1)

print(x1.brand)
print(x1.year)
print(x1.colors)

print(x2.brand)
print(x2.year)
print(x2.colors)

print(x3.brand)
print(x3.year)
print(x3.colors)
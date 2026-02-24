class Ferrari():
    def price(self):
        print("\nFerrari is an average of $250 000 - $500 000.")
    def place(self):
        print("\nFerrari is one of the most widely driven cars in Italy.")
    def popularity(self):
        print("\nFerrari is still a popular car...")

class BMW():
    def price(self):
        print("\nBMW is an average of $50 000 - $200 000.")
    def place(self):
        print("\nBMW is one of the most driven cars in China.")
    def popularity(self):
        print("\nBMW is still a popular car...")

obj_ferrari = Ferrari()
obj_bmw = BMW()

for car in (obj_ferrari, obj_bmw):
    car.price()
    car.place()
    car.popularity()
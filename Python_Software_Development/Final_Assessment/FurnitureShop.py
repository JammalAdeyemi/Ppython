class Furniture:
    def __init__(self, Price, StockLevel, isDeliveryFree):
        self.price = Price
        self.stockLevel = StockLevel
        self.isDeliveryFree = isDeliveryFree
    def getPrice(self):
        return self.price
    def getStockLevel(self):
        return self.stockLevel
    def getDeliveryFree(self):
        return self.isDeliveryFree
    def addStock(self, amount):
        self.stockLevel += amount
    def sale(self, amount):
        if self.stockLevel > amount:
            self.stockLevel -= amount
            return True
        else:
            return False

class Bookcase(Furniture):
    def __init__(self, Price, StockLevel, isDeliveryFree, NumberOfShelves):
        super(Bookcase, self).__init__(Price, StockLevel, isDeliveryFree)
        self.numberOfShelves = NumberOfShelves
    def getNumberofShelves(self):
        return self.numberOfShelves

class Desk(Furniture):
    def __init__(self, Price, StockLevel, isDeliveryFree, Color):
        super(Desk, self).__init__(Price, StockLevel, isDeliveryFree)
        self.color = Color
    def getColor(self):
        return self.color

F1 = Furniture(25.0, 5, True)
print(f"Furniture Price = {F1.getPrice()}")
print(f"Furniture Stock Level = {F1.getStockLevel()}")
print(f"Is Delivery Free? = {F1.getDeliveryFree()}")
F1.addStock(4)
print(f"Furniture Stock Level after Stock = {F1.getStockLevel()}")
F1.sale(3)
print(f"Furnitur Stock Level after Sales = {F1.getStockLevel()}")

B1 = Bookcase(35.0,4,True,3)
print(f"Bookcase no of shelves = {B1.getNumberofShelves()}")

D1 = Desk(58.0, 7, True, 'black')
print(f"Desk color = {D1.getColor()}")

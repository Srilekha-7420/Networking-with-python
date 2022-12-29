class Product:
    def __init__(self,name,price,deal_price,ratings):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.ratings=ratings
    def display_product_details(self):
        print("product:{}".format(self.name))
        print("price:{}".format(self.price))
        print("deal price:{}".format(self.deal_price))
        print("ratings:{}".format(self.ratings))
    def get_deal_price(self):
        return self.deal_price
class ElectronicItem(Product):
    def set_warrenty(self,warranty_in_months):
        self.warrenty_in_months=warranty_in_months
    def get_warrenty(self):
        return self.warrenty_in_months
class GroceryItem(Product):
    def __init__(self,name,price,deal_price,ratings,expiry_date,package_date):
        super().__init__(name,price,deal_price,ratings)
        self.expiry_date=expiry_date
        self.package_date=package_date
    def display_product_details(self):
        super().display_product_details()
        print("expiry date:{}".format(self.expiry_date))
productObj=Product("milk",10,9,5)
productObj.display_product_details()
print("=========================")
electronicObj=ElectronicItem("IPhone",10,9,5)
electronicObj.display_product_details()
print("=========================")
g=GroceryItem("Dal",20,10,5,2022,2022)
g.display_product_details()
#groceryItem=GroceryItem("milk",10,9,5,2022,2022)
#groceryItem.display_product_details
#method resolution order

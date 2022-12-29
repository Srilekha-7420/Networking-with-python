#composition:object passed as argument
#debug:set debug point where we want to know the execution.and select the 2nd the debug filename.py
#and click on step into option for line by line
#step over:for executing the debug point
class Product:
    def __init__(self,name,price,deal_price,ratings):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.ratings=ratings
        self.you_save=price-deal_price
    def display_product_details(self):
        print("product:{}".format(self.name))
        print("price:{}".format(self.price))
        print("deal price:{}".format(self.deal_price))
        print("you save:{}".format(self.you_save))
        print("ratings:{}".format(self.ratings))
    def get_deal_price(self):
        return self.deal_price
class ElectronicItem(Product):
    def set_warrenty(self,warranty_in_months):
        self.warrenty_in_months=warranty_in_months
    def get_warrenty(self):
        return self.warrenty_in_months
class GroceryItem(Product):
    pass
class Order:
    def __init__(self,delivary_speed,delivary_address):
        self.items_in_cart=[]
        self.delivery_speed=delivary_speed
        self.delivary_address=delivary_address
    def add_item(self,product,quantity):
        self.items_in_cart.append((product,quantity))
    def display_order_details(self):
        for product,quantity in self.items_in_cart:
            product.display_product_details()
            print("quantity:{}".format(quantity))
    def display_total_bill(self):
        total_bill=0
        for product,quantity in self.items_in_cart:
            price=product.get_deal_price()*quantity
            total_bill+=price
            print("total bill:{}".format(total_bill))
milk=GroceryItem("milk",40,25,5)
tv=ElectronicItem("TV",45000,40000,4)
order=Order("prime delivary","hyd")
order.add_item(milk,2)
order.add_item(tv,1)
print("+++++++")
order.display_order_details()
print("+++++++")
order.display_total_bill()

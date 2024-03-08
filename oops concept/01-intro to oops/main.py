# how to create a class  
class Item:   
    def calculate_total_price(self,x,y):
        return x * y
# how to create an instance of a class    
item1=Item()
#assign attributes
item1.name="phone"
item1.price=100
item1.quantity=5
   # calling methods from instance of a class 
print(item1.calculate_total_price(item1.price,item1.quantity))

item2=Item()
item2.name="laptop"
item2.price=100777
item2.quantity=5
    
print(item1.calculate_total_price(item2.price,item1.quantity))
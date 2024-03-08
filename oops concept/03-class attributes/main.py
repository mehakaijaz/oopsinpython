class Item :
    pay_rate=0.8
    all=[]
    def __init__(self,name:str,price:float,quantity=0):
        #run validators to the recieved arguments
        assert price>=0,f"price {price} is not greater than or equal to zero"
        assert quantity>=0 ,f"quantity {quantity} is not greater than or equal to zero"
        
        #assign self objects
        self.name=name
        self.price=price
        self.quantity=quantity
        
        Item.all.append(self)
        
    def calculate_total_price(self):
            return self.price*self.quantity
    
    def apply_discount(self):
        self.price=self.price*self.pay_rate  
        
    def __repr__(self):
         return f"item('{self.name}',{self.price},{self.quantity})"
item1=Item("phone",100,7)
item2=Item("copy",456,98)

#print(item1.calculate_total_price())
#print(item2.calculate_total_price())
print(Item.all)    
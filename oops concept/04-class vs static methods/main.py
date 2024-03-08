import csv 

class Item:
    pay_rate=0.8
    all=[]
    
    def __init__(self,price=float,quantity=0,name=str):
        assert price >= 0,f"price {price} is not greater than or equal to zero"
        assert quantity >= 0 ,f"quantity {quantity} is not greater than or equal to zero"
        
        #assign self objects
        self.name=name
        self.price=price
        self.quantity=quantity
        
        Item.all.append(self)
        
    def calculate_total_price(self):
            return self.price*self.quantity
    
    def apply_discount(self):
        self.price=self.price*self.pay_rate  
     
    @classmethod
    def instantiate_from_csv(cls):
        with open('E:/learning/python/oops concept/04-class vs static methods/items.csv','r') as f:
            reader=csv.DictReader(f)
            items=list(reader)
            
            for item in items:
                Item(
                    name=item.get('name'),
                    price=float(item.get('price')),
                    quantity=int(item.get('quantity')),
                )
      
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
            if isinstance(num, float):
                # Count out the floats that are point zero
                return num.is_integer()
            elif isinstance(num, int):
                return True
            else:
                return False
        
    def __repr__(self):
         return f"item('{self.name}',{self.price},{self.quantity})"

#print(item1.calculate_total_price())
#print(item2.calculate_total_price())
print(Item.all)    
print(Item.is_integer(5))#ye bool h
print(Item.instantiate_from_csv())#ye none type hai

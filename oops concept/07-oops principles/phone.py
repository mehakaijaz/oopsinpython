from item import Item

class Phone(Item):
    def __init__(self, price=float, quantity=0, name=str,brokenphones=0):
        #call to super() to have accessto all attributes/methods
         super().__init__(price, quantity, name)

         assert brokenphones >= 0
         
         self.brokenphones=brokenphones
         
phone1=Phone('jsdxsw',500,5,1)
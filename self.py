class shopping:
    def __init__(self,place):
        self.p=zudio
       print ("welcome to shopping at",place)
    def dress(self,typ):
        self.t=typ
    def price(self,price):
        self.p=price
    def size(self,size):
        self.s=size
    def display(self):
        print(self.t,self.p,self.s)
banglore=shopping()
banglore.dress("traditional")
banglore.price(700)
banglore.size("small")
banglore.display()

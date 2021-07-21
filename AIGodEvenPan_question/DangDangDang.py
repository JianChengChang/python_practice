# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 19:05:57 2020

@author: user
"""



class Dong():

    meallst = []
    pricelst = []
    sold = []
    total = 0
    
    def __init__(self,meal="",price=0,c=""):
        self.meal = meal
        self.price = price
        self.c = c
        
    def a(self):
        if self.meal not in self.meallst:
            self.meallst += self.meal
            self.pricelst.append(self.price)
            self.sold.append(0)
        print("Launched! Meal: %s." % self.meal)
        print(f'Price: {self.price:.0f}')
    
    def u(self,np):
        if self.meal in self.meallst:
            self.pricelst[self.meallst.index(self.meal)] = np
            print("Updated! Meal: %s." % self.meal)
            print(f'New Price: {np:.0f}')
        else:
            pass
    
    def s(self,sel):
        if self.meal in self.meallst:
            self.sold[self.meallst.index(self.meal)] += sel
            self.total += self.pricelst[self.meallst.index(self.meal)] * sel
            print("Sold. Meal: %s." % self.meal)
            print(f'Total number of sold: {sel:.0f}')
        else:
            pass
    
    def d(self):
        print('Meal:%s' % self.meallst)
        print('Total number of sold: %s' %self.sold)
        
    def q(self):
        print("==========Dangdangdang==========")
        print("Staff: %s" % self.c)
        print("Total Dong sold: %d" %sum(self.sold))
        print("Profit: %d" %self.total)

    
def main():
    
    c = input('Name: ')
    print ("Dangdangdang! %s" % c)               
    d = Dong(c=c)
    
    while True:
    
        m = input('code dishes: ')
        m = m.split(" ")
        
        if m[0] == "-1":
            price = int(input("Selling Price: "))
            d = Dong(m[1],price,c)
            d.a()
            
        elif m[0] == "-2":
            np = int(input("Update Price: "))
            d = Dong(m[1],np,c)
            d.u(np)

            
        elif m[0] == "-3":
            sel = int(input('Sold: '))
            d = Dong(m[1],d.pricelst[d.meallst.index(m[1])],c)
            d.s(sel)
            
        elif m[0] == "d":
            d.d()
        
        elif m[0] == "q":
            d.q()
            d.meallst = []
            d.pricelst = []
            d.sold = []
            d.total = 0
            break
    
    
    
if __name__ == "__main__":
    main()
      
        


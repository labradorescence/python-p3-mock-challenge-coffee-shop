#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    f1 = Coffee("Cappuccino")
    f2 = Coffee("Latte")
    f3 = Coffee("Espresso")

    c1 = Customer("Hammurabi")
    c2 = Customer("Jappy")
    c3 = Customer("Tyler")

    o1 = Order(c1, f1, 8)
    o2 = Order(c2, f1, 5)
    o3 = Order(c3, f1, 6)
    o4 = Order(c1, f2, 6)
    o5 = Order(c2, f2, 6)
    o6 = Order(c3, f2, 7)
    o7 = Order(c1, f3, 3)
    o8 = Order(c2, f3, 3)
    o9 = Order(c3, f3, 3)    



    ipdb.set_trace()

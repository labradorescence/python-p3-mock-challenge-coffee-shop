class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 3 <= len(value) and not hasattr(self, 'name'):
            self._name = value

    def orders(self):
        return [ order for order in Order.all if order.coffee == self ]
    
    def customers(self):
        pass
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        pass

class Customer:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value

    
    def orders(self):
        return [ order for order in Order.all if order.customer == self ]
    # [ order.coffee.name for order in Order.all if order.customer == c1 ]
    
    def coffees(self):
        non_unique = [ order.coffee for order in Order.all if order.customer == self ]
        unique = set(non_unique)
        unique_list = list(unique)
        return unique_list
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        if (isinstance(price, float) 
            and 1 <= price <= 10 
            and not hasattr(self, 'price')):
            self._price = price

    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self, value):
        if isinstance(value, Customer):
            self._customer = value

    @property
    def coffee(self):
        return self._coffee
    @coffee.setter
    def coffee(self, value):
        if isinstance(value, Coffee):
            self._coffee = value
    

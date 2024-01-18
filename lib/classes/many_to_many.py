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
        all_customers = [ order.customer for order in Order.all if order.coffee == self]
        unique_customers = set(all_customers)
        unique_list = list(unique_customers)
        return unique_list
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        return sum([ order.price for order in self.orders()])/len(self.orders())


class Customer:
    all = []
    def __init__(self, name):
        self.name = name

        Customer.all.append(self)
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value

    def orders(self):
        return [ order for order in Order.all if order.customer == self ]

    def coffees(self):
        non_unique = [ order.coffee for order in Order.all if order.customer == self ]

        unique = set(non_unique)
        unique_list = list(unique)
        return unique_list
    
    def create_order(self, n_coffee, n_price):
        return Order(self, n_coffee, n_price)
    
    # @classmethod 
    # def total_spent(cls, customer, coffee):
    #     #calculate the total amount spent by the customer 
    #     return sum(order.price for order in customer.orders() if order.coffee == coffee)
    
    # @classmethod
    # def most_aficionado(cls, coffee):
    #     # create a list of customer names who order that coffee 
    #     customer_for_coffee = [ order.customer for order in Order.all if order.coffee == coffee]

    #     if not customer_for_coffee:
    #         return None 
        
    #     print(customer_for_coffee, cls.total_spent(coffee))

    #     # find the customer with the highest total spent on the coffee 

    #     return max(customer_for_coffee, key=cls.total_spent(coffee))
    #     # the key param specifies a function to determines the sorting key
 
    @classmethod
    def total_spent(cls, customer, coffee):
        """
        Calculate the total amount spent by the customer on a specific coffee.

        Parameters:
        - customer: The customer object.
        - coffee: The coffee object.

        Returns:
        - Total amount spent by the customer on the specified coffee.
        """
        return sum(order.price for order in customer.orders() if order.coffee == coffee)

    @classmethod
    def total_spent_for_coffee(cls, customer, coffee):
        """
        Helper function for sorting customers based on total spent.

        Parameters:
        - customer: The customer object.

        Returns:
        - Total amount spent by the customer on the specified coffee.
        """
        return cls.total_spent(customer, coffee)

    @classmethod
    def most_aficionado(cls, coffee):
        """
        Find the customer who is the most aficionado of a specific coffee.

        Parameters:
        - coffee: The coffee object.

        Returns:
        - The customer object who spent the most on the specified coffee.
        """
        # Define a separate function to act as the key function
        def key_function(customer):
            return cls.total_spent(customer, coffee)

        # customer who ordered the coffee.
        customers_for_coffee = [order.customer for order in Order.all if order.coffee == coffee]

        # Check if there are no customers for the specified coffee.
        if not customers_for_coffee:
            return None

        # Display the list of customers and their total spent on the coffee.
        print(":::", customers_for_coffee, [c.name for c in customers_for_coffee], ":::")

        # Find the customer with the highest total spent on the coffee.
        return max(customers_for_coffee, key=key_function)
        # Use the separate key_function to pass the coffee parameter to cls.total_spent.


    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self._price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        if (
            isinstance(price, float) 
            and 1 <= price <= 10 
            and not hasattr(self, 'price')
            ):
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
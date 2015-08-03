class Animal(object):
    def __init__(self,name):
        self.name = name     
        
zebra = Animal("Jeffrey")
print zebra.name 

# Class definition
class Animal(object):
    """Makes cute animals."""
    # For initializing our instance objects
    def __init__(self, name, age,is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry
# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.




zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print zebra.name, zebra.age, zebra.is_hungry
print giraffe.name, giraffe.age, giraffe.is_hungry
print panda.name, panda.age, panda.is_hungry

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print self.name 
        print self.age 
        

hippo = Animal("Jdwqe",11,)
hippo.description()


class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."


my_cart = ShoppingCart('Colin')
my_cart.add_item('apple',14)




class Triangle(object):
    def __init__(self, side1, side2, side3):
       self.side1 = side1
       self.side2 = side2
       self.side3 = side3

class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self,hours):
        self.hours = hours
        return hours * 12

# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self,hours):
        self.hours = hours
        return hours * 20
    
    def full_time_wage(self,hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)
        

milton = PartTimeEmployee("milton")
print milton.full_time_wage(10)


class Triangle(object):
    number_of_sides = 3
    def __init__(self,angle1,angle2,angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    
    def check_angles(self):
        if self.angle1 +self.angle2 +self.angle3 == 180:
            return True
        else:
            return False
    
my_triangle = Triangle(90,30,60)
print my_triangle.number_of_sides
print my_triangle.check_angles()


class Equilateral(Triangle):
    angle = 60
    def __init__(self):
        self.angle1 = self.angle2 = self.angle3 = self.angle
        





















       
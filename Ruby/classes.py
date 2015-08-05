class Car(object):
    condition = "new"
    def __init__(self,model,color,mpg):
        self.model = model
        self.color = color 
        self.mpg = mpg

my_car = Car("DeLorean","sliver","88")
print my_car.condition
print my_car.model
print my_car.color
print my_car.mpg





class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    
    def display_car(self):
        print "This is a %s %s with %s MPG."%(self.color,self.model,str(self.mpg))
    
    def drive_car(self):
        self.condition = "used"
        print self.condition     

class ElectricCar(Car):
    def __init__(self,battery_type,model,color,mpg):
        self.battery_type = battery_type
        self.model=model
        self.color=color
        self.mpg=mpg
        
    def drive_car(self):
        self.condition = "like new"
        print self.condition
        
my_car = ElectricCar("molten salt","alero","purple",100)
print my_car.drive_car()


class Point3D(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return "(%d, %d, %d)" %(self.x, self.y, self.z)

my_point = Point3D(1,2,3)
print my_point.__repr__()
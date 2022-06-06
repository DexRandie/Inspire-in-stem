
class employee:
    def __init__ (that,_name,_salary):
        that.name = _name
        that.salary = _salary

    def sayHi (that):
        print('Hi, my name is ' + str(that.name) + ' and my salary is ' + str(that.salary))  

employee1 = employee('Dex ' ,str(1000000000000) )
employee1.sayHi()

class vehicle:
    def __init__ (self,max_speed,mileage_distance):
        self.max_speed = max_speed 
        self.mileage_distance = mileage_distance
    def maxspeed(self):
        print('vehicle max speed is ' , str(self.max_speed) + ' kmh and it covers ' , str(self.mileage_distance) , ' kms')
vehicle1 = vehicle(100 , 1000)
vehicle1.maxspeed()
# paswords
print('what is your gender')

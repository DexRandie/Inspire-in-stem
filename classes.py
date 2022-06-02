class dog:
    def att(name,age):
        def bend(type,gender):
            dog.att('bosco',17)
            dog.bend('rattoreailer','male')
class person:
    def __init__(self, _name,_age):
        self.name = _name
        self.age = _age
    def sayHi(self):
        
          print('Hello, my name is ' + str(self.name) +' and iam ' + str(self.age) +' yrs old' )     

person1 = person('Bob ' , 16 )      
person1.sayHi()   

person2 = person(' Dex ' , 19)
person2.sayHi()



class employee:
    def __init__(that,_name,_salary):
        that.name = _name
        that.salary = _salary

    def sayHi (that):
        print('Hi, my name is ' + str(that.name) + ' and my salary is' + str(that.salary))  

employee1 = ('Dex ' , str(1,000,000,000,000) )
employee1.sayHi()

class employee:
    def __init__ (that,_name,_salary):
        that.name = _name
        that.salary = _salary

    def sayHi (that):
        print('Hi, my name is ' + str(that.name) + ' and my salary is ' + str(that.salary))  

employee1 = employee('Dex ' ,str(1000000000000) )
employee1.sayHi()

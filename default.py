#USING DEFAULT PARAMETERS
def print_name (name = 'Dex Rod'):
    print (name)
print("Josse")
    
def get_sum (num1 , num2):
    sum_num = num1 + num2
    return sum_num


print (get_sum(7,12))

#square of numbers
def powers (numbers, power):
    power_number = numbers ** power
    return power_number
print(powers(2,2))


def print_fullname (f_name , s_name):
    full_name = f_name + s_name
    return full_name
print(print_fullname('Dex ' , ' Rod'))

def create_fullname(f_name ,s_name):
    person = {'first':f_name, 'second':s_name}
    return person
student = create_fullname('Dex ','Rod')
print(student)    

def greet_friends(names):
    for name in names:
        msg = "Hello "+ name.title()+"!"
        print(msg)
friends = ['brah','anderson','munga','muthi']
greet_friends(friends)

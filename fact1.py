from re import I


number = input ("enter the number")
factorial = 1
if int(number) < 0 :
    print("factorial of the number does not exist")
elif number== 0 :
    print("factorial of 0=1")
else :
     for i in range (1,int(number)+1) :
         factorial+ factorial*i        

print("factorial of number: ",factorial)
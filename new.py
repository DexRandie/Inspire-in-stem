import random


first  = str(input('would you like to use  numbers or  letters in your password ? '))
x = str(input('please enter your password '))
for number in x:
    print (str(input("please add some letters to make password strong")))
for lettter in x :
    print (input("press enter to validate your password"))

print(x)    
print ('what is your prefferd password ?')
num_pass = int(input("write your prefferd numbers"))
sym_pass = "Mongrel@123"
len_pass = int(input("How many characters would you like"))
for parsword in range (num_pass):
    parsword = ""
for c in range (len_pass):
    parsword+= random.choice(sym_pass)
print(parsword)
resoonsestatus
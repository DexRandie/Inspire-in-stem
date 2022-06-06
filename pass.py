#passwords 
import random
print ('what is your prefferd password ?')
num_pass = int(input("write your prefferd numbers"))
sym_pass = "Mongrel@123"
len_pass = int(input("How many characters would you like"))
for parsword in range (num_pass):
    parsword = ""
for c in range (len_pass):
    parsword+= random.choice(sym_pass)
print(parsword)

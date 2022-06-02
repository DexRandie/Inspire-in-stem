
acc_bal = input("ener your account balance")

if (int(acc_bal) >100000) and (int(acc_bal) < 200000):
    acc_bal = acc_bal - 25000
    print("we have deducted ksh 25000")
elif(acc_bal < 150000) :
    print('no blance')  
if(int(acc_bal) > 500000) and (int(acc_bal) < 1000000):
    acc_bal = acc_bal - (0.3*acc_bal)
    print("we have deducted 30percent from your account ")
else:
    if (int(acc_bal)) > 1000000:
         acc_bal = acc_bal - 15000
         print("we have deducted ksh15000")
    
   

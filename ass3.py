age = input ('what is your age ? ')
gender = input('what gender are you ? : male/female ? ')
account_bal = 0
if (int(age) > 25) and ( age < 30 ):
    account_bal = account_bal + 100000
    print('confirmed you have recieved 100000')
else:
    print('sorry no money for you')


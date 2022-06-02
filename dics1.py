Dex_fev_food = ['beef','chicken','vegs']
shelly_fev_food = ['rice','ugali','mahindi chom']
food = {
    'dex':[' beef ,  chicken , vegs '],
    'shelly': ['rice , ugali , mahindi chom ']
}
#print(food.get('dex'))
#print(food.get('shelly'))


for dex,shelly in food.items() :
    print(f"{dex}:{shelly}")  

        
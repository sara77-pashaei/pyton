data=[]
for f in range(5):
    food=input('please enter the food and calories you eat:')
    food,calorie=food.split(' ')
    data.append([food,float(calorie)])
    
print(data)











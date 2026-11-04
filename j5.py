# scores= [12,14,8,30,54]
# print(scores)



# mazrabs=[]
# for num in range(1,1000):
#     if num%3==0:
#         mazrabs.append(num)
# print(sum(mazrabs)/len(mazrabs))   



# total=0
# cities=['shiraz', 'esfahan','tehran']
# populations=[2,2.5,15]
# areas=[2,3,8]
# for i in range(len(cities)):
#     print(cities[i],populations[i],areas[i])   
#     if populations[i]>2:
#         total+=populations[i]
        
# print(total)





# data=[['shiraz',2,2],
#       ['esfahan',2.5,3],
#       ['tehran',15,8]
#       ]
# for row in data:
#    city=row[0]
#    population=row[1]
#    area=row[2]
#    print(city,population,area)




# txt='esfahan 2 1.5'
# info=txt.split(' ')
# city,population,area=info
# print(city,population,area)



data=[]
for i in range (3):
    text=input('please enter your city,population,area (separated by espace)/n')
    city,pop,area=text.split(' ')
    data.append([city, float(pop),float(area)])
    
print(data)   
    
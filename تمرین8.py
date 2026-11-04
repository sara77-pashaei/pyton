def take_ma(number):
    ma=[]
    
    for i in range(1,number+1):
        if number%i==0:
            ma.append(i)
    return ma
number=int(input('please enter a number:'))        
MA=take_ma()
print(MA)        
                
        
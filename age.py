name= input(' please enter your name: ')
age= int( input(' please enter your age: ')) 
gender= input(' please enter your gender: ')
if age<=20 :
    print (' teenager')
    if gender== 'male' :
        print (' mello mr' , name)
    elif gender== 'female' :
        print (' hello mrs' , name)
    
elif 20<age<40 :
    print (' adult')
    
elif age>70 :
    print (' old')
    

LDL= float ( input (' please enter your blood lipid level : (mg/dl) '))
Corona= input (' Do you have a history of coronavirus infection? : (positive or negative)')
if LDL> 100 and Corona== 'positive' :
    print (' drug1')
    
elif 80<LDL<100 and Corona== 'negative' :
     print (' drug2')
     
else :
    print (' drug3')
    

    


work= input (' what do you want to do ? : (1 or 2)')
book=  int (input (' please enter the number of books you have read :'))
age= int ( input (' please enter your age :'))   
m= book/age
m= round ( m , 2)
birth=  int (input (' please enter your years of birth :'))
year= int (input (' please enter the current year : '))
sen= year - birth
if work== '1' :
    print ('number of books read ' , book , ' and average number of books ' ,m ,' and your age is' , age )
    
elif work== '2' :
    print ('  your years of birith' , birth , ' and current year is ' , year , ' and your age in the current year is' , sen ,)
     
else :
    print (' is wrong')
    
    

    
# اوتیسم و سقط جنین

age= int ( input (' please enter the mothers age :'))
autism= input (' is there a history of autism in the younger generatins ?: ( yes or no)')
if age>45 and autism == 'yes':
    print ('Abortion is performed')
    
elif age<45 and autism == 'no':
    print (' Abortion is not performed')
    
    
    
    
    


DNA=input('please enter yor DNA sequence:')
DNA=DNA.upper()
count=0
for N in DNA:
    if N in ['G','C']:
      count=count+1
per=(count/len(DNA))*100
print(per)






age=int(input('please enter your age:'))
gender=input('please enter your gender:')
gender=gender.upper()
if age>=30:
    print('Dr')
    if gender=='male':
        print(' Hello mr')
    elif gender=='female':
        print('Hello mrs')
        
if age<30:
    print('Student')
    
    
    
    
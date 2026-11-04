data={}
n=int(input('how many patiants?:'))
for i in range(n):
    name=input(f'please enter the name of patiants= {i+1}:')
    bp=float(input(f'please enter the blood plessure of patiant {i+1}:'))
    bs=float(input(f'please enter the blood sugar of patiant {i+1}:'))
    data[name]={'bp':bp,'bs':bs}
print(data)

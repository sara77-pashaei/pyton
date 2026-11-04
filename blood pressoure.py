bp=float( input(' please enter your blood pressure: '))
suger=float( input(' please enter your blood suger: '))
if suger>140 and bp>160:
    print(' drug1')
    
elif 140>suger>120 and bp<140:
    print(' drug2')
    
elif suger<120 and 110<bp<180:
    print(' no drug')
    
else:
    print(' drug3')


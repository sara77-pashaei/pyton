path=r"C:\برنامه\aiolearn\my codes\weights.txt"
data={}
with open(path,'r')as file:
    lines=file.readlines()
    for line in lines[2:]:
      aa=line.strip().split('\t')[0]
      mw=line.strip().split('\t')[-1]
      data[aa]=float(mw)
      print(aa,mw)
      
      
      
      
      
      
path=r"C:\برنامه\aiolearn\my codes\new.txt"
with open(path,'w') as file:
    for aa,mw in data.items():
        # file.write(aa)
        # file.write('\t')
        # file.write(str(mw))
        # file.write('\n')
        
        file.write(f'{aa}\t{mw}\n')
        
        
        
      
    
      
    
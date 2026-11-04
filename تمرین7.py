# path=r"C:\برنامه\aiolearn\my codes\kegg.txt"
# data={}
# with open(path,'r')as file:
#     lines=file.readlines()
#     for line in lines [2:]:
#      date=line.strip('\n').split('\t')[0]
#      date=int(date.split('/')[0])
#      drug=line.strip('\n').split('\t')[4]
#      company=line.strip('\n').split('\t')[5]
#      if  'Novartis'in company:
#          data[drug]=(company,date)
#          print(drug,company,date)
          
            
# path=r"C:\برنامه\aiolearn\my codes\kegg-result.txt"
# with open(path,'w')as file:
#     for drug,values in data.items():
#         values=company,date
#         file.write(f'{drug}\t{company}\t{date}\n')
         
        
        
        
        
        
        
path = r"C:\برنامه\aiolearn\my codes\kegg.txt"
data = {}

with open(path, 'r') as file:
    for line in file:
        try:
            parts = line.strip().split('\t')
            date = int(parts[0].split('/')[0])
            drug = parts[4]
            company = parts[5]
        except (ValueError, IndexError):
            continue

        if 'Novartis' in company:
            data[drug] = (company, date)
            print(drug, company, date)

path = r"C:\برنامه\aiolearn\my codes\kegg-result.txt"
with open(path, 'w', encoding='utf-8') as file:
    for drug, (company, date) in data.items():
        file.write(f'{drug}\t{company}\t{date}\n')
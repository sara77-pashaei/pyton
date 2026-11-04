def gnes_obesity():
    with open ('disgenet.xlsx','r')as f:
        lines=f.readlines()
        for line in lines[1:]:
            print(line)
            

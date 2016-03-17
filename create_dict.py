f=open('dssp.3line','r')
flist=f.read().splitlines()
dict={}
for i in range (0,1197,3):
     dict[flist[i]] = (flist[i+1],flist[i+2])
print dict
f.close
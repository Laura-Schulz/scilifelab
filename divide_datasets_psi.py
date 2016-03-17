f=open('dssp.txt','r')
flist=f.read().splitlines()
dict={}
count=0
for i in range (0,1197,3):
     count=count+1
     dict[flist[i]] = 'sequence'+str(count)+'.svm.psi'
f.close()
g=open('output_id1.txt','r')
glist=g.read().splitlines()
i=open('trainingsset1_psi.txt','w')
for line in glist:
   h=open(dict.get(line),'r')
   i.write(h)
h.close()
i.close()
f=open('dssp.txt','r')
flist=f.read().splitlines()
dict={}
count=0
for i in range (0,1197,3):
     count=count+1
     dict[flist[i]] = 'sequence'+str(count)+'.svm.psi'
f.close()
g=open('test2','r')
glist=g.read().splitlines()
i=open('trainingsset5_2psi.txt','w')
for line in glist:
   if line in dict:
       h=open(dict.get(line),'r')
       hlist=h.read().splitlines()
       i.writelines(["%s\n" % item for item in hlist])
   else:
       pass
h.close()
i.close()
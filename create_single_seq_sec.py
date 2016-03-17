f=open("dssp.txt","r")
flist=f.read().splitlines()
seq_count=0
for i in range(0,int(len(flist)),3):
     seq_count=seq_count+1
     g=open("sequence"+str(seq_count)+".txt","w")
     g.write(flist[i]+'\n'+flist[i+1]+'\n'+flist[i+2]+'\n')
f.close()
g.close()
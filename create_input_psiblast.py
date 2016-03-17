f=open("sequences.fasta","r")
flist=f.read().splitlines()
seq_count=0
for i in range(0,int(len(flist)),2):
     seq_count=seq_count+1
     g=open("sequence"+str(seq_count)+".fasta","w")
     g.write(flist[i]+'\n'+flist[i+1]+'\n')
f.close()
g.close()
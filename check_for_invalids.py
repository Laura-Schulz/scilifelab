header=[]
seqs=[]
sec_struc=[]
pos=[]
target_value=[]
f=open('dssp.txt','r')
flist=f.read().splitlines()
invalid={}
for i in range(0,1197,3):
      header.append(flist[i])
      seqs.append(flist[i+1])
      sec_struc.append(flist[i+2])
count=0
for line in seqs:
    count=count+1
    for i,letter in enumerate(line):
         if letter not in 'ARNDCQEGHILKMFPSTWYVarndcqeghilkmfpstwyv':
              print 'position in line, pos:', count, i
              print 'invalid amino acid:', letter
print seqs
f.close()
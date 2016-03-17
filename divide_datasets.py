f=open('dssp.txt','r')
flist=f.read().splitlines()
dict={}
for i in range (0,1197,3):
     dict[flist[i]] = (flist[i+1],flist[i+2])
g=open('cdhit.txt','r')
y=open('header.txt','w')
glist=g.read().splitlines()
for line in glist:
   if 'Cluster' not in line:
            split_line=line.split()
            head=split_line[2]
            head=head[:-3]
            if line[0] == '0':
                y.write('True'+' '+str(head)+'\n') 
            else:
                y.write('False'+' '+str(head)+'\n')
y.close()
y=open('header.txt','r')
ylist=y.read().splitlines()
count=0
file_count=1
h=open("output1.txt","w")
for line in ylist: 
     count=count+1
     splitline=line.split()
     if splitline[0] == 'True' and count >= 55:
             file_count=file_count+1
             h=open("output"+str(file_count)+".txt","w")
             output=dict.get(splitline[1])
             h.write("%s\n%s\n" % output)
             count=0
     else: 
             output2=dict.get(splitline[1])
             h.write("%s\n%s\n" % output2)
f.close()
g.close()
h.close()
y.close()

#for t in list_of_tuples:
 #   line = ' '.join(str(x) for x in t)
  #  f.write(line + '\n')

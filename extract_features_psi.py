import pandas as pd
import numpy as np
import math
import sys
script_name=sys.argv[0]
input_file_matrix=sys.argv[1]
input_file_seq_sec=sys.argv[2]
output=sys.argv[3]


with open(input_file_matrix,'r') as file:
   array2d = [[float(digit) for digit in line.split()] for line in file]
data=np.array(array2d)
data1 = pd.DataFrame(data, dtype=float)
data1.columns = ["1", "2", "3", "4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
f= lambda x: (1 / (1 + math.exp(-x)))
data2=data1.applymap(f)

dflist=[]
for i in data2.index:
   dflist.append(" 1:"+str(data2.iloc[i]['1'])+" 2:"+str(data2.iloc[i]['2'])+" 3:"+str(data2.iloc[i]['3'])+" 4:"+str(data2.iloc[i]['4'])+" 5:"+str(data2.iloc[i]['5'])+" 6:"+str(data2.iloc[i]['6'])+" 7:"+str(data2.iloc[i]['7'])+" 8:"+str(data2.iloc[i]['8'])+" 9:"+str(data2.iloc[i]['9'])+" 10:"+str(data2.iloc[i]['10'])+" 11:"+str(data2.iloc[i]['11'])+" 12:"+str(data2.iloc[i]['12'])+" 13:"+str(data2.iloc[i]['13'])+" 14:"+str(data2.iloc[i]['14'])+" 15:"+str(data2.iloc[i]['15'])+" 16:"+str(data2.iloc[i]['16'])+" 17:"+str(data2.iloc[i]['17'])+" 18:"+str(data2.iloc[i]['18'])+" 19:" +str(data2.iloc[i]['19'])+" 20:"+str(data2.iloc[i]['20']))

f=open(input_file_seq_sec,'r')
flist=f.read().splitlines()
header=[]
seqs=[]
sec_struc=[]
target_value=[]
for i in range(0,int(len(flist)),3):
      header.append(flist[i])
      seqs.append(flist[i+1])
      sec_struc.append(flist[i+2])

for line in sec_struc:
     for n,letter in enumerate(line):
                      if letter is 'C':
                           target_value.append(+1)
                      else:
                           target_value.append(-1)
import json
zipped=zip(target_value,dflist)
list(zipped)
g=open(output,'w')
for a,b in zipped:
   g.write(str(a)+str(b)+'\n')




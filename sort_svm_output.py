f1 = open('svm_input5.txt', 'r')
f1list=f1.read().splitlines()
f2 = open('out1234.txt', 'r')
f2list=f2.read().splitlines()
TP_FP_list=[]
for line1, line2 in zip(f1list,f2list):
        if line1[0] == '-' and line2[0] == '-':
            TP_FP_list.append(1)
        if line1[0] == '-' and line2[0] != '-':
            TP_FP_list.append(0)
        if line1[0] != '-' and line2[0] == '-':
             TP_FP_list.append(0)
        if line1[0] != '-' and line2[0] != '-': 
             TP_FP_list.append(1)
g=open('out1234.txt','r')
sortlist=[]
for line in g.readlines():
    fs = [float(f) for f in line.split(",")]
    sortlist.append(fs)

TP_FP_list, sortlist = zip(*sorted(zip(sortlist, TP_FP_list)))
print sortlist
print 'haha'
print TP_FP_list


f1.close()
f2.close()

f1 = open('svm_input5.txt', 'r')
f1list=f1.read().splitlines()
f2 = open('out1234.txt', 'r')
f2list=f2.read().splitlines()
g = open('eval1234.txt', 'w')
countFP=0
countTN=0
countTP=0
countFN=0

for line1, line2 in zip(f1list,f2list):
        if line1[0] == '-' and line2[0] == '-':
            countTN = countTN+1
            g.write("True Negative"+'\n')
        if line1[0] == '-' and line2[0] != '-':
            countFN = countFN+1
            g.write("False Negative"+'\n')
        if line1[0] != '-' and line2[0] == '-':
            countFP = countFP+1
            g.write("False Positive"+'\n')
        if line1[0] != '-' and line2[0] != '-': 
            countTP = countTP+1
            g.write("True Positive"+'\n')
import math
MCC=(countTP*countTN-countFP*countFN)/(math.sqrt((countTP+countFP)*(countTP+countFN)*(countTN+countFP)*(countTN+countFN)))
ACC=(countTP+countTN)/float(countTP+countFP+countFN+countTN)
g.write('number of True Positives:'+ str(countTP)+'\n')
g.write('number of True Negatives:'+ str(countTN)+'\n')
g.write('number of False Positives:'+ str(countFP)+'\n')
g.write('number of False Negatives:'+ str(countFN)+'\n')
g.write('accuracy:'+str(ACC)+'\n')
g.write('MCC:'+str(MCC))

f1.close()
f2.close()
g.close()
import operator
import numpy as np
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
pre0=open('out_all.txt','r')
pred0=pre0.read().splitlines()
pre=open('out_psi_all.txt','r')
pred=pre.read().splitlines()
pre1=open('out_psi_t1_all.txt','r')
pred1=pre1.read().splitlines()
pre2=open('out_psi_t2_all.txt','r')
pred2=pre2.read().splitlines()
ac=open('trainingsset_all.txt','r')
ac2=ac.read().splitlines()
act=[]
for line in ac2:
   act.append(line.split(None, 1)[0])
actual0=[]
predictions0=[]
tpl0=zip(act,pred0)
tpl0.sort(key=operator.itemgetter(1),reverse = True)
for item0 in tpl0:
    actual0.append(int(item0[0]))
    predictions0.append(float(item0[1]))

actual=[]
predictions=[]
tpl=zip(act,pred)
tpl.sort(key=operator.itemgetter(1),reverse = True)
for item in tpl:
    actual.append(int(item[0]))
    predictions.append(float(item[1]))

actual1=[]
predictions1=[]
tpl1=zip(act,pred1)
tpl1.sort(key=operator.itemgetter(1),reverse = True)
for item1 in tpl1:
    actual1.append(int(item1[0]))
    predictions1.append(float(item1[1]))

actual2=[]
predictions2=[]
tpl2=zip(act,pred2)
tpl2.sort(key=operator.itemgetter(1),reverse = True)
for item2 in tpl2:
   actual2.append(int(item2[0]))
   predictions2.append(float(item2[1]))

false_positive_rate0, true_positive_rate0, thresholds = roc_curve(actual0, predictions0) 
roc_auc0 = auc(false_positive_rate0, true_positive_rate0)

false_positive_rate, true_positive_rate, thresholds = roc_curve(actual, predictions) 
roc_auc = auc(false_positive_rate, true_positive_rate)

false_positive_rate1, true_positive_rate1, thresholds = roc_curve(actual1, predictions1) 
roc_auc1 = auc(false_positive_rate1, true_positive_rate1)

false_positive_rate2, true_positive_rate2, thresholds = roc_curve(actual2, predictions2) 
roc_auc2 = auc(false_positive_rate2, true_positive_rate2)
plt.title('Receiver Operating Characteristic')
plt.plot(false_positive_rate0, true_positive_rate0, 'k', label='single seq, linear kernel, AUC = %0.2f'% roc_auc0)
plt.plot(false_positive_rate, true_positive_rate, 'b', label='multiple seq, linear kernel, AUC = %0.2f'% roc_auc)
plt.plot(false_positive_rate1, true_positive_rate1, 'g', label='multiple seq, polynomial kernel, AUC = %0.2f'% roc_auc1)
plt.plot(false_positive_rate2, true_positive_rate2, 'r', label='multiple seq, radial kernel, AUC = %0.2f'% roc_auc2)
plt.legend(loc='lower right')
plt.plot([0,1],[0,1],'k--')
plt.xlim([-0.1,1.2])
plt.ylim([-0.1,1.2])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

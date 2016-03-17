import operator
import numpy as np
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
pre=open('out1234.txt','r')
pred=pre.read().splitlines()
ac=open('svm_input5.txt','r')
ac2=ac.read().splitlines()
act=[]
for line in ac2:
   act.append(line.split(None, 1)[0])
actual=[]
predictions=[]
tpl=zip(act,pred)
tpl.sort(key=operator.itemgetter(1),reverse = True)
for item in tpl:
    actual.append(int(item[0]))
    predictions.append(float(item[1]))
false_positive_rate, true_positive_rate, thresholds = roc_curve(actual, predictions) 
roc_auc = auc(false_positive_rate, true_positive_rate)
plt.title('Receiver Operating Characteristic')
plt.plot(false_positive_rate, true_positive_rate, 'b',
label='AUC = %0.2f'% roc_auc)
plt.legend(loc='lower right')
plt.plot([0,1],[0,1],'r--')
plt.xlim([-0.1,1.2])
plt.ylim([-0.1,1.2])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

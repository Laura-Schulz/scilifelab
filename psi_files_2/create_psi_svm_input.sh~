for i in sequence*.txt.matrix ; do
    for j in sequence*.txt ; do
	if [ $j == $i.matrix ]; then
              python extract_features_psi.py ${i} ${j} "${j/.txt}".svm.psi
        fi
    done
done

for i in *.psi; do
    tail -n +4 ${i} | head -n -6  > "${i/.fasta.psi}".txt
done
for i in *.txt; do
    sed 's/.......//' ${i} > "${i/.txt}".test
done
for i in *.test; do
    echo $i
    sed -r 's/.{92}$//' ${i} > "${i/.test}".txt.matrix
done

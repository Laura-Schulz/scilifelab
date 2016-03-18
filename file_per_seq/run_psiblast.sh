for i in *.fasta; do 
if [ ! -s ${i}.psi ] ; then
echo $i
#rm -f ${i}.psi
#blastpgp -j 3 -d ~/Downloads/uniref90.fasta -i ${i} -o "${i}".blastpgp -Q "${i}".psi; 
fi
done

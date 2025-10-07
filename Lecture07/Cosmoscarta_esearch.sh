echo -e "Performing esearch..."
esearch -db nucleotide -query "Cosmoscarta[organism]" | efetch -format uid > Cosmoscarta.nuc.gis
esearch -db nucleotide -query "Cosmoscarta[organism]" | efetch -format acc > Cosmoscarta.nuc.acc
esearch -db nucleotide -query "Cosmoscarta[organism]" | efetch -format fasta > Cosmoscarta.nuc.fa
echo -e "Done esearch"

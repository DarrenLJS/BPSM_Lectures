#!/usr/bin/bash

rm -f nem*
cp ~/Exercises/Lecture06/nem* .

local_seq="plain_seq"
remote_seq="AJ223353"
rm -rf ${local_seq} ${remote_seq}
mkdir -p ${local_seq} ${remote_seq}
mv plain_seq_* ./${local_seq}/
mv AJ223353_* ./${remote_seq}/

for file in ./${local_seq}/*.fasta; do
  base=$(basename "${file}" ".fasta")
  echo -e "Blasting ${file}..."
  blastx -db nem -query ${file} -outfmt 7 > ./${local_seq}/${base}.out
done
for file in ./${remote_seq}/*.fasta; do
  base=$(basename "${file}" ".fasta")
  echo -e "Blasting ${file}..."
  blastx -db nem -query ${file} -outfmt 7 > ./${remote_seq}/${base}.out
done

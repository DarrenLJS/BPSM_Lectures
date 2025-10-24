#!/usr/bin/bash

rm -f *.fasta *.txt
local_file=/localdisk/data/BPSM/Lecture12/plain_genomic_seq.txt
cp ${local_file} .

accession="AJ223353"
wget -O ${accession}.fasta "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=${accession}&strand=1&rettype=fasta&retmode=text"

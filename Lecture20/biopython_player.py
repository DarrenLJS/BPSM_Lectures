#!/usr/bin/python3

import re
import numpy as np
from Bio import Entrez, SeqIO
from Bio.Seq import Seq
from input_handler import validate_gene, validate_taxon

def main():

    while True:
        email = input("Your email (needed for NCBI URL request): ").strip()
        if re.search(
            r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", 
            email, re.IGNORECASE
        ):
            break
        else:
            print("\nPlease input a valid email.")
    
    while True:
        try:
            gene_input = input("Gene name: ").strip()
            validate_gene(gene_input, email)
            break
        except Exception as e:
            print(f"\nPlease input a valid gene name. {e}")

    while True:
        try:
            taxon_input = input("Taxon group: ").strip()
            validate_taxon(taxon_input, email)
            break
        except Exception as e:
            print(f"\nPlease input a valid taxon group. {e}")
    
    print(f"\nSuccess! Your gene: {gene_input}")
    print(f"Success! Your taxon group: {taxon_input}\n")

    records = get_info(gene_input, taxon_input, email)
    lengths = list(map(lambda x: len(x.seq), records))
    print(f"The average length of the protein sequences is {np.mean(lengths)}")

def get_info(gene_name, taxon_name, email):
    Entrez.email = email
    searcher = Entrez.esearch(db = "protein", term = f"{gene_name}[gene] AND {taxon_name}[organism] NOT partial", retmax = 500)
    search_results = Entrez.read(searcher)["IdList"]
    print(f"{len(search_results)} protein sequences found!")
    
    records = []
    if search_results:
        fetcher = Entrez.efetch(db = "protein", id = search_results, rettype = "gp")
        records = list(SeqIO.parse(fetcher, "genbank"))
    return records

if __name__ == "__main__":
    main()

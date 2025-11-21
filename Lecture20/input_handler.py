#!/usr/bin/python3

from Bio import Entrez, SeqIO
from Bio.Seq import Seq

def validate_gene(gene_name, email):
    Entrez.email = email
    searcher = Entrez.esearch(db = "nucleotide", term = gene_name, retmax = 20)
    search_result = Entrez.read(searcher)
    if not search_result["IdList"] or search_result["Count"] == 0:
        raise ValueError(f"No result for {gene_name} on NCBI gene!")
    print(f"{search_result['Count']} results found for {gene_name} on NCBI gene!")

def validate_taxon(taxon_group, email):
    Entrez.email = email
    searcher = Entrez.esearch(db = "taxonomy", term = taxon_group, retmax = 20)
    search_result = Entrez.read(searcher)
    if not search_result["IdList"]:
        raise ValueError(f"No result for {taxon_group} on NCBI Taxonomy!")
    print(f"{search_result['Count']} results found for {taxon_group} on NCBI Taxonomy!")


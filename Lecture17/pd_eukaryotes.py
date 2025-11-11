#!/localdisk/home/s2906787/Exercises/.venv/bin/python3

import pandas as pd
import subprocess

def main():
    subprocess.call("wget -qO eukaryotes.txt 'ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/eukaryotes.txt'", shell = True)
    subprocess.call("head eukaryotes.txt", shell = True)

    eukaryotes_df = pd.read_csv("eukaryotes.txt", sep = "\t", na_values = ["-"])
    print(eukaryotes_df.head())
    subprocess.call("rm -f eukaryotes.txt", shell = True)

    fungi = eukaryotes_df[eukaryotes_df.apply(lambda x: x["Group"] in ["Fungi"] and x["Size (Mb)"] > 100, axis = 1)]
    print(len(fungi))

    print(eukaryotes_df["Group"].value_counts())
    groups_dict = filter_unique(eukaryotes_df, "Group")

    Heliconius = eukaryotes_df[eukaryotes_df["#Organism/Name"].str.contains("Heliconius")]["#Organism/Name"]
    print(Heliconius.unique().tolist())
    print(len(Heliconius.unique().tolist()))
    print(list(set(Heliconius)))
    print(len(list(set(Heliconius))))

    subgroups_dict = filter_unique(eukaryotes_df, "SubGroup")

    plants = groups_dict.get("Plants")["Center"].agg("value_counts")
    print(plants)
    print(f"{plants.index.tolist()[0]} has the most plant genomes of {plants.iloc[0]}!")
    insects = subgroups_dict.get("Insects")["Center"].agg("value_counts")
    print(insects)
    print(f"{insects.index.tolist()[0]} has the most insect genomse of {insects.iloc[0]}!")

    proteins_genes = eukaryotes_df.loc[:, ["#Organism/Name", "TaxID", "Genes", "Proteins"]]
    proteins_genes["proteins_per_gene"] = eukaryotes_df.apply(lambda x: proteins_per_gene(x["Genes"], x["Proteins"]), axis = 1)
    print(proteins_genes.head())
    min_10_perc = proteins_genes[proteins_genes["proteins_per_gene"] >= 1.1]
    print(f"{min_10_perc['#Organism/Name'].unique().tolist()}\nare the genomes with at least 10% more proteins than genes.")

def filter_unique(data, column):
    unique_list = list(set(data[column]))
    unique_dict = {}
    for uniq in unique_list:
        filtered = data[data[column] == uniq]
        print(f"There are {len(filtered)} rows for {uniq}!")
        unique_dict[uniq] = filtered
    return unique_dict

def proteins_per_gene(genes, proteins):
    if genes <= 0 or not genes:
        return None
    elif not proteins:
        return 0
    else:
        return proteins/genes

if __name__ == "__main__":
    main()

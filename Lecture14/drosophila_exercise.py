#!/usr/bin/python3

def main():
    list_drosophila = []
    with open("data.csv", "r") as file:
        for line in file:
            reader = line.strip().split(",")
            dict_line = {
                "species" : reader[0], 
                "sequence" : reader[1].upper(), 
                "gene_name" : reader[2], 
                "expression_level" : int(reader[3])
            }
            list_drosophila.append(dict_line)

    species_filter = ["Drosophila melanogaster", "Drosophila simulans"]
    filter1 = []
    filter2 = []
    filter3 = []
    filter4 = []
    for i in list_drosophila:
        if i["species"] in species_filter:
            filter1.append(i["gene_name"])
        if len(i["sequence"]) >= 90 and len(i["sequence"]) <= 110:
            filter2.append(i["gene_name"])
        if at_content(i["sequence"]) < 0.5 and i["expression_level"] > 200:
            filter3.append(i["gene_name"])
        if i["species"] != "Drosophila melanogaster":
            if i["gene_name"].startswith("k") or i["gene_name"].startswith("h"):
                filter4.append(i["gene_name"])
    print(f"{", ".join(filter1)} are from {", ".join(species_filter)}.")
    print(f"{", ".join(filter2)} are between 90 and 110 bases long.")
    print(f"{", ".join(filter3)} have AT content less than 0.5, and expression level greater than 200.")
    print(f"{", ".join(filter4)} start with k or h, but not from Drosophila melanogaster.")
    for i in list_drosophila:
        if at_content(i["sequence"]) > 0.65:
            print(f"{i["gene_name"]} has a high AT content > 0.65.")
        elif at_content(i["sequence"]) <= 0.65 and at_content(i["sequence"]) >= 0.45:
            print(f"{i["gene_name"]} has a medium AT content between 0.45 and 0.65.")
        elif at_content(i["sequence"]) < 0.45:
            print(f"{i["gene_name"]} has a low AT content < 0.45.")

def at_content(seq):
    at_count = seq.count("A") + seq.count("T")
    at_proportion = at_count/len(seq)
    return at_proportion

if __name__ == "__main__":
    main()

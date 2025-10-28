#!/usr/bin/python3

def main():
    print("Splicing genomic_dna2.txt...")
    with open("exons.txt", "r") as file:
        list_pos = list(map(lambda x: x.strip().split(",", maxsplit=1), file.readlines()))
    with open("genomic_dna2.txt", "r") as file:
        genomic = file.read().strip()
    spliced = []
    for i in range(len(list_pos)):
        start_pos = int(list_pos[i][0])
        end_pos = int(list_pos[i][1])
        print(f"Exon {i+1} starts at position {start_pos} and ends at position {end_pos}.")
        spliced += [genomic[start_pos:end_pos+1]]
    remainder = [genomic]
    for i in range(len(spliced)):
        print(f"Cutting out Exon {i+1}")
        cut = remainder[-1].split(spliced[i], maxsplit=1)
        remainder.pop(-1)
        remainder += cut
    with open("genomic_spliced.txt", "w") as file:
        file.write(f"{''.join(spliced)}\n")
    print("Generated genomic_spliced.txt!")


if __name__ == "__main__":
    main()

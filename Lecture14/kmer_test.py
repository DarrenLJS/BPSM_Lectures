#!/usr/bin/python3

def main():
    seq_file = input("File: ").strip()
    k = int(input("Size of k-mers: ").strip())
    n = int(input("Number of occurrences: ").strip())
    seq_list = []
    with open(seq_file, "r") as file:
        for line in file:
            seq_list.append(line.strip())
    seq_list = list(filter(lambda x: len(x) > 0 and not x.startswith(">"), seq_list))
    for i in range(len(seq_list)):
        kmer_list = kmer_id(seq_list[i], k, n)
        print(f"Sequence {i+1} has the following k-mers: {", ".join(kmer_list)}")

def kmer_id(seq, k, n):
    kmer_dict = {}
    for i in range(len(seq) - k + 1):
        if seq[i:i+k] not in list(kmer_dict.keys()):
            kmer_dict[seq[i:i+k]] = 1
        elif seq[i:i+k] in list(kmer_dict.keys()):
            kmer_dict[seq[i:i+k]] += 1
    common_kmer = [k for k, v in kmer_dict.items() if v > n]
    return common_kmer


if __name__ == "__main__":
    main()

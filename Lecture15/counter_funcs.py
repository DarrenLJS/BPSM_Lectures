#!/usr/bin/python3

def main():
    reference = input("DNA sequence: ")
    kmer_length = int(input("k-mer length: "))
    threshold = int(input("Frequency threshold of k-mers: "))
    print(kmer_id(reference, kmer_length, threshold))

def aa_perc_1(seq_aa, res):
    ref_seq = seq_aa.upper()
    count_res = ref_seq.count(res.upper())
    return round((count_res/len(ref_seq))*100, 2)

def aa_perc_2(seq_aa, res_list = ["A", "I", "L", "M", "F", "W", "Y", "V"]):
    ref_seq = seq_aa.upper()
    count_list = list(map(lambda x: ref_seq.count(x.upper()), res_list))
    total_count = 0
    for count in count_list:
        total_count += count
    return round((total_count/len(ref_seq))*100, 2)

def unknown_perc(seq_dna, thres):
    ref_seq = seq_dna.upper()
    threshold = round(thres, 2)
    base_list = ["A", "T", "C", "G"]
    count_list = list(map(lambda x: ref_seq.count(x), base_list))
    total_count = 0
    for count in count_list:
        total_count += count
    unk_perc = 100.00 - round((total_count/len(ref_seq))*100, 2)
    if unk_perc > threshold:
        return True
    else:
        return False

def kmer_id(seq_dna, k, n):
    ref_seq = seq_dna.upper()
    kmer_count_dict = {}
    for i in range(len(ref_seq) - k + 1):
        if ref_seq[i:i+k] not in list(kmer_count_dict.keys()):
            kmer_count_dict[ref_seq[i:i+k]] = 1
        elif ref_seq[i:i+k] in list(kmer_count_dict.keys()):
            kmer_count_dict[ref_seq[i:i+k]] += 1
    common_kmer = [k for k, v in kmer_count_dict.items() if v > n]
    return common_kmer

if __name__ == "__main__":
    main()

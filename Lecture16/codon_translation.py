#!/usr/bin/python3

gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

def main():
    seq = str(input("Sequence: ").strip()).upper()
    top_seq, bot_seq = {}, {}

    for i in range(3):
        top_seq[f"seq_top_{i}"] = seq[i:]
        bot_seq[f"seq_bot_{i}"] = seq_reverse(seq[i:])

    top_prot, bot_prot = {}, {}
    for key, seq in top_seq.items():
        top_prot[key] = seq_translate(seq)
    for key, seq in bot_seq.items():
        bot_prot[key] = seq_translate(seq)

    for key in top_seq.keys():
        print(f"\n{top_seq[key]}\ntranslates to\n{top_prot[key]}\n")
    for key in bot_seq.keys():
        print(f"\n{bot_seq[key]}\ntranslates to\n{bot_prot[key]}\n")

def seq_reverse(seq):
    reference = {"A" : "T", "T" : "A", "C" : "G", "G" : "C"}
    reverse = list(map(lambda x: reference[x], seq))[::-1]
    return "".join(reverse)

def seq_translate(seq):
    protein = []
    for i in range(0, len(seq), 3):
        if len(seq[i:i+3]) == 3:
            protein.append(gencode.get(seq[i:i+3], "X"))
    return "".join(protein)

if __name__ == "__main__":
    main()

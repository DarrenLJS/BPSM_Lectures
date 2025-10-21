#!/usr/bin/python3

def main():
    seq = input('What is your sequence? ')
    pex1 = int(input('Position of exon 1: '))
    pex2 = int(input('Position of exon 2: '))
    length1 = int(input('Length of exon 1: '))
    length2 = int(input('Length of exon 2: '))
    seq_new, cod_seq = coding_seq(seq, pex1, pex2, length1, length2)
    print(f'The sequence is\n{seq_new}')
    print(f'The coding sequence is\n{cod_seq}')
    print(f'The length of coding sequence is {len(cod_seq)}.')
    print(f'The percentage of sequence which is coding is {(len(cod_seq)/len(seq_new))*100}.')

def coding_seq(seq, pex1, pex2, length1, length2):
    seq_low = seq.lower()
    ex1 = seq[pex1:pex1+length1]
    ex2 = seq[pex2:pex2+length2]
    seq_low = seq_low.replace(ex1.lower(), ex1, 1)
    seq_new = seq_low.replace(ex2.lower(), ex2, 1)
    return seq_new, ex1 + ex2

main()

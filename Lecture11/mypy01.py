#!/usr/bin/python3

def main():
    seq = input('What is your sequence? ')
    count_a, count_t, avg_at = at_count(seq)
    print(f'The number of Adenine nucleotides is {count_a}.')
    print(f'The number of Thymine nucleotides is {count_t}.')
    print(f'The average number of Adenine & Thymine nucleotides is {avg_at}.')
    print('The complement of', seq, complement(seq), sep = '\n')
    pos, frags = ecori_cut(seq)
    len_frags = [len(i) for i in frags]
    print(f'EcoRI cuts at positions {pos} to give fragments of lengths {len_frags}')

def at_count(seq):
    count_a, count_t = 0, 0
    for i in seq:
        if i == 'A':
            count_a += 1
        elif i == 'T':
            count_t += 1
        else:
            continue
    return count_a, count_t, (count_a + count_t)/len(seq)

def complement(seq):
    dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    complement = ''
    for i in seq:
        if i in dict.keys():
            complement = complement + dict[i]
    return complement

def ecori_cut(seq):
    find = 'GAATTC'
    results = []
    pos = []

    for i in range(len(seq) - len(find) + 1):
        if seq[i:i+len(find)] == find:
            pos += [i+1]

    if len(pos) < 1:
        return [-1], [0]
    else:
        left = seq
        for i in pos:
            results += [left[:i]]
            left = left[i:]
        results.append(left)
        return pos, results

main()

#!/usr/bin/python3

import re

def main():
    with open("long_dna.txt", "r") as file:
        sequences = file.readlines()
    sequences = list(map(lambda x: x.strip().upper(), sequences))
    
    bpsm1_dict = {}
    for seq in sequences:
        bpsm1_dict[seq] = bpsm1_digest(seq)

    bpsm1_bpsm2_dict = {}
    for seq in sequences:
        bpsm1_bpsm2_dict[seq] = bpsm1_bpsm2_digest(seq)
    
    for seq, frags in bpsm1_dict.items():
        if len(frags) < 1:
            print(f"BpsmI did not digest\n{seq}\nLength: {len(seq)}\n")
        else:
            print(f"BpsmI digested\n{seq}\nLength: {len(seq)}\n")
            counter = 0
            for frag in frags:
                counter += 1
                print(f"Fragment {counter}: {frag}\nLength: {len(frag)}\n")

    for seq, frags in bpsm1_bpsm2_dict.items():
        if len(frags) < 1:
            print(f"Double digestion by BpsmI and BpsmII did not work on\n{seq}\nLength: {len(seq)}\n")
        else:
            print(f"Double digestion by BpsmI and BpsmII worked on\n{seq}\nLength: {len(seq)}\n")
            counter = 0
            for frag in frags:
                counter += 1
                print(f"Fragment {counter}: {frag}\nLength: {len(frag)}\n")

def bpsm1_digest(sequence):
    if not re.search(r"A[ATCG]TAAT", sequence):
        return frags
    else:
        bpsm1_iter = re.finditer(r"A[ATCG]TAAT", sequence)
        positions = []
        for match in bpsm1_iter:
            start = match.start()
            positions.append(start+3)
        positions = list(sorted(positions))
        frags = []
        prev_pos = 0
        for pos in positions:
            frags.append(sequence[prev_pos:pos])
            prev_pos = pos
        frags.append(sequence[prev_pos:])
        return frags

def bpsm1_bpsm2_digest(sequence):
    if not re.search(r"(A[ATCG]TAAT|GC[AG][AT]TG)", sequence):
        return []
    else:
        bpsm1_iter = re.finditer(r"A[ATCG]TAAT", sequence)
        bpsm2_iter = re.finditer(r"GC[AG][AT]TG", sequence)
        positions = []
        for match in bpsm1_iter:
            start = match.start()
            positions.append(start+3)
        for match in bpsm2_iter:
            start = match.start()
            positions.append(start+4)
        positions = list(sorted(positions))
        frags = []
        prev_pos = 0
        for pos in positions:
            frags.append(sequence[prev_pos:pos])
            prev_pos = pos
        frags.append(sequence[prev_pos:])
        return frags

if __name__ == "__main__":
    main()

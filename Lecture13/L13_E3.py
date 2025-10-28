#!/usr/bin/python3

import subprocess

def main():
    subprocess.call("rm -rf sequence_*", shell=True)
    with open("AJ223353_coding.fasta", "r") as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
    sequences = list(filter(lambda x: x[0] != ">", lines))
    for i in range(len(sequences)):
        print(f"Reading sequence {i+1}...")
        sliding_windows = slider(sequences[i])
        print(sliding_windows)
        print(f"Calculating GC proportion in sequence {i+1} and its windows...")
        for j in sliding_windows:
            gc_perc = gc_content(j)
            print(f"{j}\nhas percentage GC content of {gc_perc}")
        print(f"Sequence {i+1} has percentage GC content of {gc_content(sequences[i])}")
        print(f"Generating FASTA files for sequence {i+1}...")
        with open(f"sequence_{i+1}.fasta", "w") as file:
            file.write("This FASTA file is a compilation of all window segments of length 30, offset 3 of the following sequence:\n")
            file.write(f"{sequences[i]}\n")
        print(f"Generated sequence_{i+1}.fasta!")
        for j in range(len(sliding_windows)):
            with open(f"sequence_{i+1}_segment_{j+1}.fasta", "w") as file:
                file.write(f">sequence_{i+1}_segment_{j+1}, GC content: {gc_content(sliding_windows[j])}%\n")
                file.write(f"{sliding_windows[j]}\n")
            print(f"Generated sequence_{i+1}_segment_{j+1}.fasta!")
            print(f"Appending to sequence_{i+1}.txt...")
            with open(f"sequence_{i+1}.fasta", "a") as file:
                file.write("\n")
                file.write(f">segment_{j+1}, GC content: {gc_content(sliding_windows[j])}%\n")
                file.write(f"{sliding_windows[j]}\n")
        print(f"Finished reading sequence {i+1}!")
        subprocess.call(f"mkdir sequence_{i+1}", shell=True)
        subprocess.call(f"mv sequence_{i+1}*.fasta ./sequence_{i+1}", shell=True)


def slider(seq):
    windows = []
    for i in range(0, len(seq), 3):
        if len(seq[i:]) < 30:
            break
        windows += [seq[i:i+30]]
    for i in windows:
        print(i)
    return windows

def gc_content(seq):
    count_gc = seq.count("G") + seq.count("C")
    total = len(seq)
    return round((count_gc/total)*100, 1)

if __name__ == "__main__":
    main()

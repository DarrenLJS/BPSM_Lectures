#!/usr/bin/python3

import subprocess

def main():
    subprocess.call("rm -rf *_bases", shell=True)
    for i in range(100, 999, 100):
        subprocess.call(f"mkdir {i}_{i+99}_bases", shell=True)
        print(f"Making {i}_{i+99}_bases directory...")
    subprocess.call("ls *.dna > dna_files.txt", shell=True)
    with open("dna_files.txt", "r") as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
    list_files = list(filter(lambda x: x.endswith(".dna"), lines))
    for i in list_files:
        with open(i, "r") as file:
            sequences = list(map(lambda x: x.strip(), file.readlines()))
        print(f"Sorting {i}...")
        base = sorter(sequences, i)
        for j in range(100, 999, 100):
            subprocess.call(f"mv {base}_{j}_{j+99}.txt ./{j}_{j+99}_bases", shell=True)
        subprocess.call(f"for file in ./*_bases/*.txt; do [ -f $file ] && [ ! -s $file ] && rm $file; done", shell=True)
        print(f"Finished sorting {i}!")

def sorter(list_seq, file):
    rename = "_".join(file.split(".", maxsplit=1))
    for i in range(100, 999, 100):
        with open(f"{rename}_{i}_{i+99}.txt", "w") as file:
            file.write("")
    for i in list_seq:
        a, b = 200, 200
        for j in range(200, 1010, 100):
            if len(i) < j:
                a = j - 100
                b = j - 1
                break
        print(f"Writing seq to {rename}_{a}_{b}.txt...")
        with open(f"{rename}_{a}_{b}.txt", "a") as file:
            file.write(f"{i}\n")
    return rename


if __name__ == "__main__":
    main()

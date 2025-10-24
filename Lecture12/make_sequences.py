#!/usr/bin/python3

import subprocess

def main():
    print("Getting sequences...")
    subprocess.call("./get_sequences.sh", shell=True)
    with open("plain_genomic_seq.txt", "r") as file:
        local_seq = file.read().strip().strip("\n").upper()
    with open("AJ223353.fasta", "r") as file:
        remote_lines = file.readlines()
    remote_lines = list(filter(lambda x: x[0] != ">" and len(x) > 0, remote_lines))
    remote_seq = "".join([i.strip().strip("\n") for i in remote_lines]).upper()
    print("Sequences obtained!")

    print("Making sequences blastable...")
    local_seq = "".join(map(lambda x: checker(x), local_seq))
    print(local_seq)
    remote_seq = "".join(map(lambda x: checker(x), remote_seq))
    print(remote_seq)
    print("Sequences are now blastable!")

    print("Separating into coding and non-coding sequences...")
    local_coding = local_seq[:64] + local_seq[91:]
    local_noncoding = local_seq[64:91]
    remote_coding = remote_seq[28:409]
    remote_noncoding1, remote_noncoding2 = remote_seq[:28], remote_seq[409:]
    
    with open("plain_seq_coding.fasta", "w") as file:
        file.write(f">{len(local_coding)}\n")
        file.write(f"{local_coding}\n")
    with open("plain_seq_noncoding.fasta", "w") as file:
        file.write(f">{len(local_noncoding)}\n")
        file.write(f"{local_noncoding}\n")
    with open("AJ223353_coding.fasta", "w") as file:
        file.write(f">{len(remote_coding)}\n")
        file.write(f"{remote_coding}\n")
    with open("AJ223353_noncoding_1.fasta", "w") as file:
        file.write(f">{len(remote_noncoding1)}\n")
        file.write(f"{remote_noncoding1}\n")
    with open("AJ223353_noncoding_2.fasta", "w") as file:
        file.write(f">{len(remote_noncoding2)}\n")
        file.write(f"{remote_noncoding2}\n")
    print("Coding and non-coding sequences obtained!")

    print("Running BLAST...")
    subprocess.call("./blast_sequences.sh", shell=True)
    print("BLAST Done!")

def checker(base):
    if base not in ["A", "T", "C", "G"]:
        return "N"
    else:
        return base
            

main()

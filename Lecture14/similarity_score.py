#!/usr/bin/python3

def main():
    file_name = input("File: ").strip()
    seq_list = []
    with open(file_name, "r") as file:
        for line in file:
            seq_list.append(line.strip())
    seq_list = list(filter(lambda x: len(x) > 0 and not x.startswith(">"), seq_list))
    for i in range(len(seq_list)):
        matching = seq_list.copy()
        matching.pop(i)
        similarity_score(seq_list[i], matching)

def similarity_score(seq, match_list):
    for match in match_list:
        if len(match) < len(seq):
            ref = len(match)
        elif len(match) >= len(seq):
            ref = len(seq)
        count_same = 0
        for i in range(ref):
            if seq[i] == match[i]:
                count_same += 1
        score = round((count_same/len(seq))*100, 2)
        print(f"{seq}\nis {score}% similar to\n{match}\n")
        

if __name__ == "__main__":
    main()

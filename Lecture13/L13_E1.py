#!/usr/bin/python3

def main():
    print("Trimming input.txt...")
    with open("input.txt", "r") as file:
        list_seq = list(map(lambda x: x.strip(), file.readlines()))
    trimmed_seq = [i[15:] for i in list_seq]
    for i in range(len(list_seq)):
        print(f"The length of old sequence {i+1} is {len(list_seq[i])}.")
        print(f"The length of new sequence {i+1} is {len(trimmed_seq[i])}.")
    with open("input_trimmed.txt", "w") as file:
        file.write(f"{'\n'.join(trimmed_seq)}\n")
    print("Generated input_trimmed.txt!")

if __name__ == "__main__":
    main()

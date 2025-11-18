#!/usr/bin/python3

import matplotlib.pyplot as plt

def main():
    while True:
        try:
            window = int(input("Window size: "))
            content = input("Content (AT/GC): ").lower()
            if content not in ["at", "gc"]:
                raise ValueError("Only AT or GC content")
            base_range = int(input("Base range (0 means all): "))
            break
        except Exception as e:
            print("Invalid input. Try again!")

    plotter(window, content, base_range)

def plotter(window, content, base_range):
    with open("ecoli.txt", "r") as file:
        if base_range == 0:
            seq = file.read().replace("\n", "").upper()
        else:
            seq = file.read().replace("\n", "")[0:base_range].upper()
    
    def analyser(window, content, seq):
        if content == "at":
            at_content = []
            for start in range(len(seq) - window):
                frame = seq[start:start + window]
                at = (frame.count("A") + frame.count("T"))/window
                at_content.append(at)
            return at_content
        elif content == "gc":
            gc_content = []
            for start in range(len(seq) - window):
                frame = seq[start:start + window]
                gc = (frame.count("G") + frame.count("C"))/window
                gc_content.append(gc)
            return gc_content

    data = analyser(window, content, seq)

    plt.figure(figsize = (20, 10))
    
    plt.plot(data, linewidth = 2)
    
    if content == "at":
        plt.suptitle("AT content of E coli genome", fontsize = 20)
    elif content == "gc":
        plt.suptitle("GC content of E coli genome", fontsize = 20)
    plt.title(f"Window size of {str(window)}", fontsize = 15)
    plt.xlabel("Position base-pair")
    plt.ylabel("Fraction of bases")
    
    plt.savefig("Chart_L19.png", transparent = False)


if __name__ == "__main__":
    main()

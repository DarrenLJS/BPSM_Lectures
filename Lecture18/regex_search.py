#!/usr/bin/python3

accession_list = [
    "xkn59438", 
    "yhdck2", 
    "eihd39d9", 
    "chdsye847", 
    "hedle3455", 
    "xjhd53e", 
    "45da", 
    "de37dp"
]

import re

def main(acc):
    for i in acc:
        match_5 = re.search(r"5", i)
        if match_5:
            print(f"{i} has a '5'")

    for i in acc:
        match_d_or_e = re.search(r"[de]", i)
        if match_d_or_e:
            print(f"{i} has a 'd' or a 'e'")

    for i in acc:
        match_de = re.search(r"(de|d\w+e)", i)
        if match_de:
            print(f"{i} has 'd' and 'e' in that order")

    for i in acc:
        match_d_e = re.search(r"d\we", i)
        if match_d_e:
            print(f"{i} has 'd' and 'e' with a single letter between")

    for i in acc:
        match_de_ed = re.search(r"(de|ed|d\w+e|e\w+d)", i)
        if match_de_ed:
            print(f"{i} has 'd' and 'e' in any order")

    for i in acc:
        match_xy_start = re.search(r"^[xy]", i)
        if match_xy_start:
            print(f"{i} starts with 'x' or 'y'")

    for i in acc:
        match_xy_e = re.search(r"^[xy]\w+e$", i)
        if match_xy_e:
            print(f"{i} starts with 'x' or 'y', and ends with 'e'")

    for i in acc:
        match_3num = re.findall(r"[0-9]", i)
        if len(match_3num) >= 3:
            print(f"{i} has any 3 numbers in any order")

    for i in acc:
        match_3diffnum = re.findall(r"[0-9]", i)
        if len(list(set(match_3diffnum))) >= 3:
            print(f"{i} has 3 different numbers")

    for i in acc:
        match_3ormore = re.search(r"[0-9]{3,}", i)
        if match_3ormore:
            print(f"{i} has 3 or more numbers in a row")

    for i in acc:
        match_d_arp = re.search(r"d[arp]$", i)
        if match_d_arp:
            print(f"{i} ends with 'd', and 'a' or 'r' or 'p'")

if __name__ == "__main__":
    main(accession_list)

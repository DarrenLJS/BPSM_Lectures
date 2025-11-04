#!/usr/bin/python3

from counter_funcs import aa_perc_1
from counter_funcs import aa_perc_2
from counter_funcs import unknown_perc
from counter_funcs import kmer_id

def main():
    test_aa_perc_1()
    test_aa_perc_2()
    test_unknown_perc()
    test_kmer_id()

def test_aa_perc_1():
    try:
        assert round(aa_perc_1("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
        assert round(aa_perc_1("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
        assert round(aa_perc_1("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
        assert round(aa_perc_1("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)
    except AssertionError:
        print("aa_perc_1 fails the test.")
    else:
        print("aa_perc_1 works!")

def test_aa_perc_2():
    try:
        assert round(aa_perc_2("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
        assert round(aa_perc_2("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
        assert round(aa_perc_2("MSRSLLLRFLLFLLLLPPLP")) == 65
    except AssertionError:
        print("aa_perc_2 fails the test.")
    else:
        print("aa_perc_2 works!")

def test_unknown_perc():
    try:
        assert unknown_perc("ATGCATCAAT", 10) == False
        assert unknown_perc("ATXCATCBAT", 20) == False
        assert unknown_perc("ATXCATCBAT", 10) == True
    except AssertionError:
        print("unknown_perc fails the test.")
    else:
        print("unknown_perc works!")

def test_kmer_id():
    try:
        assert kmer_id("ATGCATCATG", 2, 2) == ["AT"]
        assert kmer_id("ATGCATCATG", 2, 1) == ["AT", "TG", "CA"]
        assert kmer_id("ATGCATCATG", 3, 1) == ["ATG", "CAT"]
    except AssertionError:
        print("kmer_id fails the test.")
    else:
        print("kmer_id works!")

if __name__ == "__main__":
    main()

#!/usr/bin/python3

import pytest
from counter_funcs import aa_perc_1
from counter_funcs import aa_perc_2
from counter_funcs import unknown_perc
from counter_funcs import kmer_id

def test_aa_perc_1():
    assert round(aa_perc_1("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
    assert round(aa_perc_1("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
    assert round(aa_perc_1("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
    assert round(aa_perc_1("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)

def test_aa_perc_2():
    assert round(aa_perc_2("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
    assert round(aa_perc_2("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
    assert round(aa_perc_2("MSRSLLLRFLLFLLLLPPLP")) == 65

def test_unknown_perc():
    assert unknown_perc("ATGCATCAAT", 10) == False
    assert unknown_perc("ATXCATCBAT", 20) == False
    assert unknown_perc("ATXCATCBAT", 10) == True

def test_kmer_id():
    assert kmer_id("ATGCATCATG", 2, 2) == ["AT"]
    assert kmer_id("ATGCATCATG", 2, 1) == ["AT", "TG", "CA"]
    assert kmer_id("ATGCATCATG", 3, 1) == ["ATG", "CAT"]


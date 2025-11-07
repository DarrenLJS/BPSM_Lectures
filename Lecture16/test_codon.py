#!/usr/bin/python3

import pytest
from codon_translation import seq_reverse
from codon_translation import seq_translate

def test_seq_reverse():
    assert seq_reverse("ATCG") == "CGAT"
    assert seq_reverse("ATGTTCGG") == "CCGAACAT"

def test_seq_translate():
    assert seq_translate("ATGTTCGGTTGA") == "MFG_"
    assert seq_translate("ACCGAACAT") == "TEH"
    assert seq_translate("ACCGAAC") == "TE"

def test_all():
    assert seq_translate(seq_reverse("TCAACCGAACAT")) == "MFG_"


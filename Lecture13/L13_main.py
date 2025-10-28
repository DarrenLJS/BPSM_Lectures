#!/usr/bin/python3

import subprocess

lecture13 = "/localdisk/data/BPSM/Lecture13"
subprocess.call(f"cp {lecture13}/* .", shell=True)
aj223353_coding = "/localdisk/home/s2906787/Exercises/Lecture12/AJ223353/AJ223353_coding.fasta"
subprocess.call(f"cp {aj223353_coding} .", shell=True)

subprocess.call("./L13_E1.py", shell=True)
subprocess.call("./L13_E2.py", shell=True)
subprocess.call("./L13_E3.py", shell=True)
subprocess.call("./L13_E4.py", shell=True)

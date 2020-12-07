#!/usr/bin/env python3


import re
from statistics import mean

perf_lines = '^\[SUM\]\W+[0-9]+.[0-9]+-([0-9]+.[0-9]+)\W+sec\W+[0-9]+.[0-9]+\W+MBytes\W+([0-9]+\.*[0-9]*)?\W+Mbits\/sec'

file_handler = open('android_tdd1_uplink.txt')

numlist = list()

for line in file_handler:
    line = line.rstrip()

    y = re.findall(perf_lines, line)
    if (y):
        print(float(y[0][0]), ",", float(y[0][1]), sep='')


#if __name__ == "__main__":
#    main()


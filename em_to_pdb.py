#for a file that was energy minimised using Gromacs
#Have to change the numbers according to the file
#Change the file names as well


import numpy as np

infile = open('/home/snehab/Work/EMin/em.pdb', 'r')
outfile = open('/home/snehab/Work/EMin/em1.pdb', 'w')

for line in infile:
    if not(line.startswith('ATOM')):
        outfile.write(line)
    else:
        lis = line.split()
        if int(lis[1]) <= 3476:
            outfile.write(line[:21] + 'A' + line[22:])
        elif 3476 < int(lis[1]) <= 7117:
            outfile.write(line[:21] + 'B' + line[22:])
        elif 7117 < int(lis[1]) <= 24331:
            outfile.write(line[:21] + 'C' + line[22:])
        elif 24331 < int(lis[1]) <= 44530:
            outfile.write(line[:21] + 'D' + line[22:])
        elif 44530 < int(lis[1]) <= 45828:
            outfile.write(line[:21] + 'E' + line[22:])
        elif 45828 < int(lis[1]) <= 50962:
            outfile.write(line[:21] + 'F' + line[22:])
        elif 50962 < int(lis[1]) <= 52738:
            outfile.write(line[:21] + 'J' + line[22:])
        elif 52738 < int(lis[1]) <= 54804:
            outfile.write(line[:21] + 'O' + line[22:])
        elif 54804 < int(lis[1]) <= 55524:
            outfile.write(line[:21] + 'P' + line[22:])
        elif 55524 < int(lis[1]) <= 56795:
            outfile.write(line[:21] + 'Q' + line[22:])
        elif 56795 < int(lis[1]) <= 59299:
            outfile.write(line[:21] + 'M' + line[22:])

infile.close()
outfile.close()

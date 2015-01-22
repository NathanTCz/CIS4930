from __future__ import print_function

line_c = 0
data = []
with open(raw_input('File to be analyzed (.csv only): '), 'r') as file:
    for line in file:
        line_c += 1
        if line_c == 1:
            keys = [x for x in line.split(',')]
            continue
        else:
            data.append( {k.strip('\n'): v.strip('\n') for k, v in zip(keys, line.split(','))} )

for d in data:
    print(d['TMAX'])

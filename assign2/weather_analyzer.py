from __future__ import print_function

def parse_date(date):
    date = date[4] + date[5] + '/' + date[6] + date[7] + '/' + date[0] + date[1] + date[2] + date[3]
    return date

def ctof(temp):
    return ((temp * 9 / 5) + 32)

def find_max_temp(data):
    max_temp = 0
    for d in data:
        if ( float(d['TMAX']) > max_temp):
            max_temp = float(d['TMAX'])
            day = d['DATE']
    return ctof(max_temp / 10), parse_date(day)

def find_min_dif(data):
    min_dif = float('inf')
    for d in data:
        tmin = ctof( float(d['TMIN']) / 10)
        tmax = ctof( float(d['TMAX']) / 10)
        if ( (tmax - tmin) < min_dif ):
            min_dif = (tmax - tmin)
            day = d['DATE']
    return min_dif, parse_date(day)

def find_ave_wnd(data):
    ave_wnd = 0
    for d in data:
        ave_wnd += float(d['AWND'])
    return ( ave_wnd / len(data) )

def tot_prcp(data):
    tot_prcp = 0
    for d in data:
        tot_prcp += float(d['PRCP'])
    return tot_prcp

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

print('Maximum temperature (F): ',find_max_temp(data)[0], ' on ', find_max_temp(data)[1] )
print('Minimum temperature difference (F): ',find_min_dif(data)[0], ' on ', find_min_dif(data)[1] )
print('Average wind speed (m/s): ',find_ave_wnd(data) / 10)
print('Total precipitation (mm): ',tot_prcp(data) / 10)

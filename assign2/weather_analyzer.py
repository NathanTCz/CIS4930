from __future__ import print_function

def parse_date(date):
    date = '{0[4]}{0[5]}/{0[6]}{0[7]}/{0[0]}{0[1]}{0[2]}{0[3]}'.format(date)
    return date

def ctof(temp):
    return ((temp * 9 / 5) + 32)

def find_max_temp(data):
    return max([( ctof(float(d['TMAX']) / 10), parse_date(d['DATE']) ) for d in data], key=lambda x: x[0])

def find_min_dif(data, min_dif=float('inf')):
    for d in data:
        tmin, tmax = ctof( float(d['TMIN']) / 10), ctof( float(d['TMAX']) / 10)
        if ( (tmax - tmin) < min_dif ):
            min_dif, day = (tmax - tmin), d['DATE']
    return min_dif, parse_date(day)

def find_ave_wnd(data):
    return ( sum( [float(d['AWND']) for d in data] ) / len(data) )

def tot_prcp(data):
    return ( sum( [float(d['PRCP']) for d in data] ) )

with open(raw_input('File to be analyzed (.csv only): '), 'r') as file:
    keys = [x for x in file.readline().split(',')]
    data = [{k : v for k, v in zip(keys, line.strip('\n').split(','))} for line in file]

print('Maximum temperature (F): ',find_max_temp(data)[0], ' on ', find_max_temp(data)[1] )
print('Minimum temperature difference (F): ',find_min_dif(data)[0], ' on ', find_min_dif(data)[1] )
print('Average wind speed (m/s): ','{:.2f}'.format( find_ave_wnd(data) / 10) )
print('Total precipitation (mm): ',tot_prcp(data) / 10)

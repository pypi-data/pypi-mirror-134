import os
import pycountry

def get_supported_countries():
    for cn in os.listdir('./countries'):
        if cn.startswith('_'): continue 
        country = pycountry.countries.lookup(cn.split('.')[0])
        print('{}\t[{}]'.format(country.name, country.alpha_2))

from countries.pk import pk

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 21:08:45 2015

@author: zhihuixie
"""

import vcf

def load_data(file_name):
    vcf_reader = vcf.VCFReader(open(file_name, 'rb'))
    types = []
    records = [list(record) for record in vcf_reader]
    for item in records:
         types.append(item[7]['TYPE'])
    return types
def counter(type1, types):
    counts = 0
    for site_type in types:
        counts += site_type.count(type1)
    return counts

if __name__ == '__main__':

    file_name = 'Genomic Data Science with Galaxy Project - identify polymorphic sites.vcf'
    types = load_data(file_name)
    target_types = ['snp', 'mnp', 'del', 'ins', 'complex']
    for target_type in target_types:
        counts = counter(target_type, types)
        if target_type != 'del' or target_type != 'ins':
            print 'The number of ' + target_type + ' type is: %d' %counts
        if target_type == 'del':
            counts1 = counts
        if target_type == 'ins':
            counts2 = counts
    print 'The number of del/ins type is: %d' %(counts1 + counts2)
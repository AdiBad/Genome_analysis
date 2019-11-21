# -*- coding: utf-8 -*-
"""
"C:\Users\Aditya\Desktop\new_dataset"

Created on Thu Nov 21 01:34:39 2019

@author: Aditya
"""
#For single GSE SOFT file parsing in GEOParse
import GEOparse

gse = GEOparse.get_GEO(filepath = r'C:\Users\Aditya\Desktop\GSE15824_family.soft.gz', destdir = r'E:\CodingProjects')
for name, extra in gse.gsms.items():
    name = name.strip('\n')
    print('\t\t'+name+' transferred\n')
    gse.gsms[name].table.to_csv(name+'.txt', index = None, sep = '\t', mode = 'w')

#For multiple files, store list of GSE files you have downloaded
#in a text file and read it sequentially to access all the GSMs

#Storing list of files in variable putingeo
    
f = open(r'fetchtheseGSEfromGEO.txt','r')
putingeo = f.readlines() 
f.close()

import GEOparse
import os
num = len(putingeo)
for i in putingeo:
    print (str(num)+' files remaining')
    num = num - 1
    i=i.strip('\n')
    os.chdir(i)
    gse = GEOparse.get_GEO(filepath='./'+i+'_family.soft.gz')
    for name, extrathing in gse.gsms.items():
            name=name.strip('\n')
            print ('\t\t'+name+' transferred')
            gse.gsms[name].table.to_csv(name+'.txt', index=None, sep='\t', mode='w')
        os.chdir('..')
        print (i+' completed')
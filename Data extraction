#Code to download .SOFT format from online of all GSE I need
#For one GSE:

import GEOparse
gse = GEOparse.get_GEO(geo='GSE1563', destdir='./')

#For multiple GSE:

# fetchtheseGSEfromGEO.txt contains list of GSE I want from GEO

f = open( r'C:\Users\ambily.sivadas\Desktop\AdityaB\humans\GPL8888_26SAMPLES\fetchtheseGSEfromGEO.txt','r')
putingeo = f.readlines() 
f.close()

import GEOparse
for i in putingeo
    gse = GEOparse.get_GEO(i.strip('\n'), destdir='./')

#..............................................................................................................
#Code to fetch all GSM of all GSE and store in a new folder

f = open( r'C:\Users\ambily.sivadas\Desktop\AdityaB\humans\GPL8888_26SAMPLES\fetchtheseGSEfromGEO.txt','r')
putingeo = f.readlines() 
f.close()


import GEOparse
import os
for i in putingeo:
    i=i.strip('\n')
    print (i+' being downloaded')
    os.makedirs(i)
    os.chdir(i)
    gse = GEOparse.get_GEO(i.strip('\n'), destdir='./')
    os.chdir('..')


#..............................................................................................................
#Code to fetch tables (processed data in form of LRR, BAF, Gtype) from downloaded .soft 
#or .soft.rar file  and create a text file for each sample

f = open(r'C:\Users\ambily.sivadas\Desktop\AdityaB\humans\GPL8888_26SAMPLES\fetchtheseGSEfromGEO.txt','r')
putingeo = f.readlines() 
f.close()

import  GEOparse
import os
num = 26
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

#..............................................................................................................  
#Extract characteristics of an individual from .SOFT file and store in an excel sheet
#Get particular GSE file (this one is online access)

import GEOparse
gse = GEOparse.get_GEO('GSE76645')

#Insert data in Excel file like <GSM><Characteristics>
wb=Workbook('human_character.xlsx')
ws=wb.create_sheet('GSE76645')
for name, extrathing in gse.gsms.items():
    print (str(name),str(gse.gsms[name].metadata['characteristics_ch1']))
    ws.append([str(name),str(gse.gsms[name].metadata['characteristics_ch1'])])
    
wb.save('human_character.xlsx')



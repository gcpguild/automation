"""
Creating the roles as per the client, 'thyrve' requirements
May 21 2022.
Author : ramamurthy.valavandan@kyndryl.com
Google-Cloud-Platform-Guild-Members : Google-Cloud-Platform-Guild-Members@kyndryl.com 
"""
from pickle import NONE
import pandas as pd

import re

import xlwt
from xlwt.Workbook import *

import xlsxwriter
from pathlib import Path

customerscopexlsxfile="customer_requirements.xlsx"

clientname="thyrve"
basepath = "C:"
ifc="GCP Roles"
N="\\"
creaddel = ["(create buckets & add files)", "(Create & delete)", "(Postgres)"]

addprecolv = ["Above services", "Same as above", "Above services +", "All Services (no restrictions)"]

USCL="A:B"

runcol=['Role','Services']

"""
NO CHANGE SHOULD BE DONE FROM HERE ONWARDS ...
"""
sl=27
ls=len(ifc)
if(ls <= sl ):
    ifl=ifc
else:
    ifl=(ifc[0:sl])

def prt(p):

    width = len(p) + 4
    print('┏' + "━"*width + "┓")
    print('┃' + p.center(width) + '┃')
    print('┗' + "━"*width + "┛")


inputxlsxfile = ("{}{}{}{}{}".format(basepath,N, clientname, N, customerscopexlsxfile))

checkinputxlsxfile = Path(inputxlsxfile)


if checkinputxlsxfile.is_file():
    pi="\'Customer mapping in Excel file format is available  \' :"
    p = ("{} {}".format(pi,inputxlsxfile))
    prt(p)
else:
    pi="\'Customer mapping in Excel file is missing !\' :"
    p = ("{} {}".format(pi,inputxlsxfile))
    prt(p)
    exit(1)

xl = pd.ExcelFile(inputxlsxfile)

sheetlst=xl.sheet_names  
for sn in (sheetlst):
    sheetname=sn
with open(inputxlsxfile, "rb") as f:
    
        #dfe = pd.read_excel(f, sheet_name=sheetname, header=0, index_col=0, usecols=USCL)
        dfe = pd.read_excel(f, sheet_name=sheetname, usecols=USCL)
        colname=dfe.columns
        row_count=dfe.count()[0]


def cleaning(mi):
    mi = mi.strip()
    mi = mi.rstrip()
    mi = mi.lstrip()
    return mi

def usc(mi,syr):
    if (syr == '_'):
        mi = re.sub("\s", syr, mi)
    mi = re.sub('[^A-Za-z0-9]+', syr , mi)
    return mi

def readcoldata(mi):
    mio = cleaning(di)
    return mio


custrole = []
req = []

for fld in colname:
    mi = fld
    mi = cleaning(mi)
    #print ('Ffld -->', mi)
    if (mi == runcol[0]):
        
        for i in dfe.index:
            di = (dfe[mi][i])
            mir = readcoldata(mi)
            syr = "_"
            mir = usc(mir, syr)
            #print ('mir -', mir)
            if mir not in custrole:
                custrole.append(mir) 
          
    if (mi == runcol[1]):
       
         for i in dfe.index:
            di = (dfe[mi][i])
            miw = readcoldata(mi)
            miw = re.sub('[(*+)]+', ' ', miw)
            miw = re.sub('Create & delete', ' ', miw)
            miw = re.sub('Postgres', ' ', miw)
            miw = re.sub('Postgres', ' ', miw)
            miw = re.sub('Compute Engines', 'Compute Engine', miw)
            miw = re.sub('GCS', 'Storage', miw)
            miw = re.sub('create buckets & add files',' ',  miw)
            #miw = re.sub('Same as above',' ',  miw)
            miw = re.sub('Above services +',' ',  miw)
         
            #miw = re.sub('Above services',' ',  miw)
            miw = re.sub('All Services (no restrictions)', ' ', miw)

            miw = cleaning(miw)
            if miw not in req:
                req.append(miw)
           
sno=("{}_{}".format(clientname,ifl))

mi=sno

mi = cleaning(mi)

ext_table_name=mi

outxls = ("{}{}{}{}{}{}{}".format(basepath,N,clientname, N,ext_table_name,".","xlsx"))

pi="\'Ouput Excel file Created  \' :"
p = ("{} {}".format(pi,outxls))
prt(p)

dfe.to_excel(outxls, sheet_name=sno, index=False)

lc = len(req)


sheetnamesout = []

for cr in (custrole):
    #print(cr)
    sheetnamesout.append(cr)



scnt = len(sheetnamesout)

"""
    for x in zip(custrole, req):   
        fx=("==".join(map(str, x)))
        print(fx)
"""  
#writer = pd.ExcelWriter(outxls, engine='xlsxwriter')

with pd.ExcelWriter('outxls.xlsx', engine='xlsxwriter', mode='w') as writer:
    for m in range(0,scnt):
        js = ("{}{}".format("df", m))
       
        sa = sheetnamesout[m]
  
        ch = req[m] 
        if (m == 0):
            ds0 = []
            if ch not in ds0:
                ds0.append(ch)
              
                js0 = pd.DataFrame({sa: ds0})
                js0.to_excel(writer, sheet_name=sa, index=False)
        if (m == 1):
            ds1 = []
            if ch not in ds1:
                ds1.append(ds0)
                ds1.append(ch)
                
                js1 = pd.DataFrame({sa: ds1})
                js1.to_excel(writer, sheet_name=sa, index=False)
        if (m == 2):
            ds2 = []
            if ch not in ds2:
                ds2.append(ds1)
                ds2.append(ch)
                
                js2 = pd.DataFrame({sa: ds2})
                js2.to_excel(writer, sheet_name=sa, index=False)
        if (m == 3):
            ds3 = []
            if ch not in ds3:
                ds3.append(ds2)
                #print('ds3', ds3)
                js3 = pd.DataFrame({sa: ds3})
                js3.to_excel(writer, sheet_name=sa, index=False)
        if (m == 4):
            ds4 = []
            if ch not in ds4:
                ds4.append(ch)
                #print('ds4', ds4)
                js4 = pd.DataFrame({sa: ds4})
                js4.to_excel(writer, sheet_name=sa, index=False)
        if (m == 5):
            ds5 = []
            if ch not in ds5:
                ds5.append(ds4)
                #print('ds5', ds5)
                js5 = pd.DataFrame({sa: ds5})
                js5.to_excel(writer, sheet_name=sa, index=False)
        if (m == 6):
            ds6 = []
            if ch not in ds6:
                ds6.append(ch)
                #print('ds6', ds6)
                js6 = pd.DataFrame({sa: ds6})
                js6.to_excel(writer, sheet_name=sa, index=False)
        if (m == 7):
            ds7 = []
            if ch not in ds7:
                ds7.append(ds6)
                ds7.append(ch)
                #print('ds7', ds7)
                js7 = pd.DataFrame({sa: ds7})
                js7.to_excel(writer, sheet_name=sa, index=False)
        if (m == 8):
            ds8 = []
            ds8.append('serviceAccountAdmin')
            js8 = pd.DataFrame({sa: ds8})
            js8.to_excel(writer, sheet_name=sa, index=False)
   
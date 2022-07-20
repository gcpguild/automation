import json
import re
from pathlib import Path
import pandas as pd

infile="role.json"

clientdir="thyrve"
basepath = "C:"
skey = 'name'
av='roles'

"""
NO CHANGE SHOULD BE DONE AFTERWARDS ...
"""
def prt(p):

    width = len(p) + 4
    print('┏' + "━"*width + "┓")
    print('┃' + p.center(width) + '┃')
    print('┗' + "━"*width + "┛")

clientpath = ("{}{}{}".format(basepath,"\\", clientdir))

jsonfile = ("{}{}{}{}{}".format(basepath,"\\", clientdir, "\\", infile))

checkinputjsonfile = Path(jsonfile)


if checkinputjsonfile.is_file():
    pi="\'GCP Roles JSON file format is available  \' :"
    p = ("{} {}".format(pi,jsonfile))
    prt(p)
else:
    pi="\'role.json is missing ! Execute below Command to create role.json @ dir: \' "
    p = ("{} {}".format(pi,clientpath))
    prt(p)
    pi="gcloud iam roles list --format=json > "
    p = ("{} {}".format(pi,jsonfile))
    prt(p)
    exit(1)


cserole=[]
with open(jsonfile) as jsonFile:
    data = json.load(jsonFile)

    for d in data:
        dn=(d['name'])
        dn = re.sub(av,'', dn)
        dn = re.sub('/','', dn)
    
        dn = re.split(r'(?<=\D)\.(?=.)|(?<=\d)\.(?=\D)', dn)
        if dn not in (cserole):
            print (dn)
            cserole.append(dn)
       

cserole.sort()
im = len(cserole)-1


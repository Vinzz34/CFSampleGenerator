from bs4 import BeautifulSoup
import requests
import os
import time
import sys

#---Global---
contestid=sys.argv[1]
url="https://codeforces.com/contest/{}".format(str(contestid))
print("Fetching "+url+"...")
page=requests.get(url).text
soup=BeautifulSoup(page,'lxml')
parentpath="/home/vinzz/c++/cf"

#create folder
path=os.path.join(parentpath,str(contestid))
print("Creating directory "+str(contestid)+" ...")
os.mkdir(path)

#template
templatef=open('/home/vinzz/Templates/template.txt',"r")
template=templatef.read().strip()
templatef.close()

#problem create
path=path+"/"
def probcreate(prob_id):
    filename=prob_id+".cpp"
    print("Creating "+filename+" ...")
    filename=path+filename
    fname=open(filename,"a")
    fname.write(template)
    fname.close()

#get input and output
def io(prob_id):
    print("Creating input output for "+prob_id+" ...")
    ifile=prob_id+".in"
    ifile=path+ifile
    ofile=prob_id+".out"
    ofile=path+ofile
    wf=open(ifile,"a")
    of=open(ofile,"a")
    purl=url+"/problem/"+prob_id
    ppage=requests.get(purl).text
    psoup=BeautifulSoup(ppage,'lxml')
    inp=psoup.find('div',class_='input')
    oup=psoup.find('div',class_='output')
    wf.write(inp.text)
    of.write(oup.text)
    wf.close()
    of.close()
    with open(ifile, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(ifile, 'w') as fout:
        fout.writelines(data[1:])
    with open(ofile, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(ofile, 'w') as fout:
        fout.writelines(data[1:])

#main

problems=soup.find('div',class_='datatable').find('table').findAll('a')

for i in range(len(problems)):
    if(i%4!=0): continue
    prob_id=problems[i].text.strip()
    probcreate(prob_id)
    io(prob_id)

print("Almost done ...")
print("Generated codeforces "+str(contestid)+".")
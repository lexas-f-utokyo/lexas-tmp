import pandas as pd
from ahocorapy.keywordtree import KeywordTree
import datetime
dic_hgnc = KeywordTree(case_insensitive=True)
dic_expe = KeywordTree(case_insensitive=True)

#dic_hgncを宣言
print("import",datetime.datetime.now())

import pickle
with open("gene_to_sym_0919.pickle","rb") as f:
   gene_to_sym = pickle.load(f)

l = set()
for key in gene_to_sym.keys():
   if len(key) < 3:continue
   else:l.add(key.lower()) #1,2文字Filter

with open('./removal_0919.csv') as remo:
    for word in remo:
      word = word.strip()
      try: l.remove(word.lower())
      except KeyError: 
        print(word) 
        pass
print("genename",datetime.datetime.now())
print("for" in l,"FOR")

for ll in l:
    dic_hgnc.add(" " + ll + " ")

expes = set()
with open('./expe_8.txt') as expe:
    for line in expe:
          line_splitted = line.strip().split('\t')
          a  = line_splitted[0]
          expes.add(a.lower())
for e in expes:
  dic_expe.add(" "+e+" ")

dic_hgnc.finalize()
dic_expe.finalize()
print("Dicfin",datetime.datetime.now())

def dependency_checker3(text,dig,die):
  tmpt = text
  text = " "+text+" "
  text = text.replace(",","").replace(".","")
  ges = list(dig.search_all(text))
  if len(ges) == 0: return []
  tmp = []
  ret = []
  for g in ges:
    tmp.append((text[:g[1]]+" [GENE] "+text[g[1]+len(g[0]):],g[0].strip()))
  for t,tg in tmp:
    exs = list(die.search_all(t))
    if len(exs) == 0: return []
    for e in exs:
      ret.append((t[:e[1]]+" [EXPE] "+t[e[1]+len(e[0]):],tg,e[0].strip()))
  return ret

import sys
args = sys.argv
part = int(args[1])
import datetime

done =set()

f = open("./Part{}_parse_2109.csv".format(part),"r")
f2 = open("./Part{}_chikan_2109.csv".format(part),"w")

i = 0
for line in f:
    #if i == 10000:break
    if i % 10000 == 0: print(part,i)
    i += 1
    ls = line.strip().split("@@@@@")
    if len(ls) == 3:
        ls2 = ls[2].strip().split("#####") #textの集合体
        for lll in ls2: #lllは文章
           tmp = dependency_checker3(lll,dic_hgnc,dic_expe)
           if len(tmp) == 0:
             continue
           for t in tmp:
              f2.write(ls[0]+"\t"+ls[1]+"\t"+t[1]+"\t"+t[2]+"\t"+lll+"\t"+t[0]+"\n")

f.close()
f2.close()

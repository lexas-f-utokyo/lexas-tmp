import datetime
import xml.etree.ElementTree as ET
import sys
args = sys.argv
part = int(args[1])
start= int(args[2])
end  = int(args[3])

def p_j():
    print(datetime.datetime.now())
    f = open("oa_file_list.csv", "r")
    pmcid_list = []
    jours_list = []
    pappend = pmcid_list.append
    jappend = jours_list.append

    #j_p  = {} #dict
    t = 0
    for line in f:
      t +=1
      line_splitted = line.strip().split(",")
      journal = line_splitted[1].split(".")[0]
      PMCID = line_splitted[2]
      pappend(PMCID)
      jappend(journal.replace(" ", "_"))
      #j_p[PMCID] = journal.replace(" ", "_")
      if t % 1000000 == 0:
          print(t)
    f.close()
    print(datetime.datetime.now())
    return pmcid_list[start:end],jours_list[start:end]

import pickle
f = open("pmcid_list.pickle","rb")
pmcid_list = pickle.load(f)[start:end]
f.close()
f = open("jours_list.pickle","rb")
jours_list = pickle.load(f)[start:end]
f.close()
def scrape(jour,pmcid):
  try:
#    tree = ET.parse("E:\/PMC/nxml/"+ jour + "/" + pmcid+ ".nxml")
    tree = ET.parse("/media/user/HDD/PMC_210902/"+ jour + "/" + pmcid+ ".nxml")
  except FileNotFoundError:
    try:tree = ET.parse("/media/user/HDD/PMC_210912/"+ jour + "/" + pmcid+ ".nxml")
    except FileNotFoundError:return "Year","NotFound"
    except OSError:return "Year","OSError"
    except: return "Year","Others"
  except OSError:
    return "Year","OSError"
  except:
    return "Year","Others"
  try:
    root = tree.getroot()
    art = root[0].find("article-meta")
    pubd = art.find("pub-date")
    year = pubd.find("year")
    year = year.text
    sent = []
  except: return "Year","Others"
  #一番上の階層の要素を取り出します
  if len(root) < 2:
    return year,""
  for chichi in root[1]:  #root1はbodyのこと-これは共通項目
    #chichi_1 : Abstract, chichi_2 = Intro
    status = 0
    if len(chichi) < 1: #階層がない場合・・・。
      #print("s")
      continue
    for c in chichi: #title タグを探して判定
        if "title" not in c.tag.lower():#念のため
            continue
        else:
            #print(" ".join(c.itertext()).lower())
            status = 1
            break
    if status == 0: break
        
    for chichichi in chichi:
      if chichichi.tag == "p":
         sent.append(" ".join(chichichi.itertext()).replace("\n",""))
      for a in chichichi:
        for ccccc in a:
          if ccccc.tag == "fig":
           a.remove(ccccc)     #Figure legend を削除
        if a.tag == "p":
            sent.append(" ".join(a.itertext()).replace("\n",""))
            
  return year," ".join(sent)
#scrape("2d_Mater","PMC7047727")
t = 0
#with open("Part{}.csv".format(part),"r", encoding='UTF-8') as f:
#  done = set()
#  for line in f:
#     ls = line.strip().split("@@@@@")
#     try:done.add(ls[1])
#     except IndexError:continue
#  print("donefin",list(done)[:5])

with open("Part{}_2109.csv".format(part),"a", encoding='UTF-8') as f:
  pa = 1
  for i in range(len(pmcid_list)):
    t += 1
    if t % 10000 == 0:
      print("survive,part"+str(part)+" now:"+str(t))
    if pmcid_list[i]=="PMC6786290":
       pa=0
       continue
    if pa ==1:continue
    p = pmcid_list[i]
    j = jours_list[i]
    #if p in done:
    #    continue
    y,s = scrape(j,p)
    f.write(y+"@@@@@"+p+"@@@@@"+s+"\n")

print("end:"+str(part))

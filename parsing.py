import sys
args = sys.argv
part = int(args[1])
#scispacy==0.1.0
#en_core_sm==0.1.0
import datetime
import scispacy
import en_core_sci_sm

done =set()
#f = open("Part{}_parse_2109.csv".format(part),"r")
#for line in f:
#    ls = line.strip().split("@@@@@")
#    done.add(ls[1])
#f.close()

f = open("Part{}_parse_2109.csv".format(part),"a")
f2 = open("Part{}_2109.csv".format(part),"r")

nlp = en_core_sci_sm.load()


def parse(sent):
   doc = nlp(sent)
   ret = "#####".join([str(a) for a in doc.sents])
   return ret

if __name__ == "__main__":
   t = 0
   for line in f2:
      t += 1
      if t % 10000 == 0:
         print("Part",part,":",t, datetime.datetime.now())
      ls = line.strip().split("@@@@@")
      if len(ls) ==3:
         if ls[1] in done:continue
         sent = ls[2]
         if len(sent) > 1000000:sent= sent[:1000000]
         par = parse(sent)
         f.write(ls[0]+"@@@@@"+ls[1]+"@@@@@"+par+"\n")
f.close()
f2.close()

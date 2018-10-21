def Pika_Translator(INPUT):
  Comd=INPUT
  Comd_P = ""
  for i in range(0,len(Comd)):
    Comd_P += bin(ord(Comd[i])).replace('0b','').replace("1","皮").replace("0","卡") + "丘"
  return Comd_P

fname = 'Desktop/ComGenome/note'
with open(fname) as f:
  content = f.readlines()
NN = ''
for i in content:
  NN += Pika_Translator(i)+'\n'
fo = open("foo.txt", "w")
fo.write(NN)
fo.close()

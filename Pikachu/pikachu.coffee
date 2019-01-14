import os, time
import argparse
'''
parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input')     #输入文件

args = parser.parse_args()
INPUT = args.input
'''
########

def Pikachu(i):
  pix = '\u2588'*2
  f = open("/media/ken/Data/script/System_display/elements/pika1.txt")
  f2 = open("/media/ken/Data/script/System_display/elements/pika1-1.txt")
  f3 = open("/media/ken/Data/script/System_display/elements/pika2.txt")
  f4 = open("/media/ken/Data/script/System_display/elements/pika2-1.txt")
  Type1 = f.read()
  Type2 = f2.read()
  Type3 = Type1
  Type4 = f3.read()
  Type5 = f4.read()
  Type6 = Type4

  Type_c = locals()["Type"+str(i)]
  return Type_c.replace("$","\x1b[30;2;6m"+ pix +"\x1b[0m").replace('l',"\x1b[33;3;6m"+ pix +"\x1b[0m").replace('/',"\x1b[30;0;2m"+ pix +"\x1b[0m").replace('B',"\x1b[31;3;2m"+ pix +"\x1b[0m").replace('C',"\x1b[0;1;1m"+ pix +"\x1b[0m").replace('L',"\x1b[33;2;1m"+ pix +"\x1b[0m").replace(' ','  ')

Num=0
while 1 == 1:
  Num += 1
  A =  Pikachu(Num%6+1)
  os.system('clear')
  print(A)
  time.sleep(1)

#!/usr/local/bin/python3.7

import os, time
import argparse
'''
parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input')     #输入文件


args = parser.parse_args()
INPUT = args.input
'''
########
def tailN_rm(String):
  String = String+"\n+_____tag"
  return String.replace("\n\n+_____tag",'')

def Easy_Com(A_l,A_r,N_blank=2):
  result = ''
  Ll = len(A_l.split('\n'))
  Lr = len(A_r.split('\n'))
  for i in range(Ll):
    if i > (Lr-1):
      AR = len_UC(A_r.split('\n')[0])*"-"
    else:
      AR = A_r.split('\n')[i]
    result += A_l.split('\n')[i] +N_blank*" " +AR + "\n"
  result += "\n======="
  return result.replace("\n\n=======",'')

def Pikachu(i):
  Base_p = {1:'/media/ken/Data/script/System_display/elements/pika1.txt',
            2:'/media/ken/Data/script/System_display/elements/pika1-1.txt',
            3:'/media/ken/Data/script/System_display/elements/pika1.txt',
            4:'/media/ken/Data/script/System_display/elements/pika2.txt',
            5:'/media/ken/Data/script/System_display/elements/pika2-1.txt',
            6:'/media/ken/Data/script/System_display/elements/pika2.txt'}
  f = open(Base_p[i])
  Type_c = f.read()

  Pika_patern = {"  ":" ",
  ' l':'\x1b[33;33;6m\u2584\x1b[0m' , 'l ':'\x1b[33;33;6m\u2580\x1b[0m',
  " $":"\x1b[30;3;6m\u2584\x1b[0m"  , "$ ":"\x1b[30;3;6m\u2580\x1b[0m",
  ' /':'\x1b[30;0;2m\u2584\x1b[0m'  , '/ ':'\x1b[30;0;2m\u2580\x1b[0m',
  'll':'\x1b[33;40;6m\u2588\x1b[0m' ,
  'l$':'\x1b[33;40;6m\u2580\x1b[0m' , '$l':'\x1b[33;40;6m\u2584\x1b[0m',
  'l/':'\x1b[0;43;2m\u2584\x1b[0m'  , '/l':'\x1b[0;43;2m\u2580\x1b[0m',
  'lB':'\x1b[33;41;6m\u2580\x1b[0m' , 'Bl':'\x1b[33;41;6m\u2584\x1b[0m',
  'lC':'\x1b[0;43;6m\u2584\x1b[0m'  , 'Cl':'\x1b[0;43;6m\u2580\x1b[0m',
  'lL':'\x1b[33;100;6m\u2580\x1b[0m', 'Ll':'\x1b[33;100;6m\u2584\x1b[0m',
  "$$":"\x1b[30;3;6m\u2588\x1b[0m"  ,
  "$/":'\x1b[0;40;2m\u2584\x1b[0m'  , "/$":'\x1b[0;40;2m\u2580\x1b[0m',
  '$C':'\x1b[0;40;6m\u2584\x1b[0m'  , "C$":'\x1b[0;40;6m\u2580\x1b[0m',
  '$L':'\x1b[30;100;6m\u2580\x1b[0m', 'L$':'\x1b[30;100;6m\u2584\x1b[0m',
  '//':'\x1b[30;0;2m\u2588\x1b[0m'  ,  'BB':'\x1b[31;3;6m\u2588\x1b[0m'}

  Pika_list = Type_c.split("\n")
  Pika_r1 = []
  for i in range(len(Pika_list)//2):
    Num = i*2
    Line_tmp = []
    for ii in range(len(Pika_list[Num])):
      Line_tmp += [Pika_list[Num][ii] + Pika_list[Num+1][ii]]
    Pika_r1 += [Line_tmp]

  Pikachu = ""
  for i in Pika_r1:
    Line_tmp2=""
    for ii in i:
      Line_tmp2 += Pika_patern[ii]
    Pikachu += Line_tmp2 +'\n'

  return Pikachu

for i in range(50):
  os.system('clear')
  print(Pikachu(i%6+1))
  time.sleep(0.6)

'''
Num=0
while 1 == 1:
  Num += 1
  A =  Pikachu(Num%6+1)
  os.system('clear')
  print(A)
  time.sleep(1)
'''

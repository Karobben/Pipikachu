#!/usr/local/bin/python3.7

######################
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input',default="Pika!!")     #输入文件
parser.add_argument('-f','-F','--formate',default="En",help ='En / Cn')     #输入文件

args = parser.parse_args()
INPUT = args.input
FORMATE = args.formate
########################

import os, time
import argparse
from pyparsing import *

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

def len_UC(String):
  ESC = Literal('\x1b')
  integer = Word(nums)
  escapeSeq = Combine(ESC + '[' + Optional(delimitedList(integer,';')) +
                  oneOf(list(alphas)))
  nonAnsiString = lambda s : Suppress(escapeSeq).transformString(s)
  unColorString = nonAnsiString(String)
  return(len(unColorString))

def Comple(TB):
  N_sp = 0
  line_T = len(TB.split("\n"))
  for i in range(line_T):
    if len_UC(TB.split("\n")[i]) > N_sp:
      N_sp = len_UC(TB.split("\n")[i])
  result = ""
  for i in range(line_T):
    result += TB.split("\n")[i]+" "*(N_sp-len_UC(TB.split("\n")[i]))+'\n'
  result = tailN_rm(result)
  return result

def Easy_Com(A_l,A_r,N_blank=2):
  result = ''
  Ll = len(A_l.split('\n'))
  Lr = len(A_r.split('\n'))
  for i in range(Ll):
    if i > (Lr-1):
      AR = len_UC(A_r.split('\n')[0])*" "
    else:
      AR = A_r.split('\n')[i]
    result += A_l.split('\n')[i] +N_blank*" " +AR + "\n"
  result += "\n======="
  return result.replace("\n\n=======",'')

def Pick_pos(i):
  Pikc_base={"1"   : "     $$         $  \n    $/$        $l$ \n    $l$       $lll$\n   $ll$    $$$llll$\n   $ll$  $$//$lll$ \n  $llll$$ll/$lll$  \n $lllllllll$$ll$   \n$Clllllllll$llll$  \n$$lllllllll$ll$l$  \n$llllC$lllll$$l$   \n $lll$$BBlll$$$    \n  $llllBlll$$$     \n $llllllllllL$     \n  $$lllll$lll$     \n   $llll$lllL$     \n  $l$llll$lll$     \n  $$$$$lllll$      \n       $$$l$$      \n        $lll$      \n         $$$       \n",
             "1_1" : '                   \n     $$        $   \n    $/$   $   $l$  \n    $l$  $/$ $lll$ \n   $ll$  $/$$llll$ \n   $ll$ $ll$$lll$  \n  $llll$$ll$$ll$   \n $lllllllll$$l$    \n$Clllllllll$l$     \n$$lllllllll$ll$    \n$llllC$lllll$l$    \n $lll$$BBlll$$$    \n $lllllBlll$L$     \n  $$lllll$lll$     \n   $llll$lllL$     \n  $l$llll$lll$     \n  $$$$$lllll$      \n       $$$l$$      \n        $lll$      \n         $$$       \n',
             "2"   : '  $         $$     \n $l$        $/$    \n$lll$       $l$    \n$llll$$$    $ll$   \n $lll$//$$  $ll$   \n  $lll$/ll$$llll$  \n   $ll$$lllllllll$ \n  $llll$lllllllllC$\n  $l$ll$lllllllll$$\n   $l$$lllll$Cllll$\n    $$$lllBB$$lll$ \n     $$$lllBllll$  \n     $Lllllllllll$ \n     $lll$lllll$$  \n     $Llll$llll$   \n     $lll$llll$l$  \n      $lllll$$$$$  \n      $$l$$$       \n      $lll$        \n       $$$         \n',
             "2_2" : '                   \n   $        $$     \n  $l$   $   $/$    \n $lll$ $/$  $l$    \n $llll$$/$  $ll$   \n  $lll$$ll$ $ll$   \n   $ll$$ll$$llll$  \n    $l$$lllllllll$ \n     $l$lllllllllC$\n    $ll$lllllllll$$\n    $l$lllll$Cllll$\n    $$$lllBB$$lll$ \n     $L$lllBlllll$ \n     $lll$lllll$$  \n     $Llll$llll$   \n     $lll$llll$l$  \n      $lllll$$$$$  \n      $$l$$$       \n      $lll$        \n       $$$         \n'
           }
  return Pikc_base[i]

def Pikachu(i):
  stat_dic = {1:"1",2:"1_1",3:"1",4:"2",5:"2_2",6:"2"}
  Type_c = Pick_pos(stat_dic[i])

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

def Saysomething(something):
  T_rows, T_columns = os.popen('stty size', 'r').read().split()
  Num_T  = int(int(T_columns))
  if FORMATE == "Cn":
    Num_T = int(Num_T/2) -10
    Blan_N =2
  else:
    Num_T = Num_T -20
    Blan_N =1
  Line_w = int(len(something) / Num_T)
  if Line_w > 0:
    A =''
    for  i in range(Line_w+1):
      N_blank = ((Line_w+1)* Num_T - len(something))*' '
      something += N_blank
      A_tmp =""
      for ii in range(Num_T):
        A_tmp += something[ii+i*Num_T]
      A += '\x1b[33;7;6m' + A_tmp + '\x1b[0m' + '\n'
  else:
    A ='\x1b[33;7;6m' + str(something) + '\x1b[0m'+'\n'
  if FORMATE == 'Cn':
    A = A#.replace(N_blank,N_blank*2)
  A += '\x1b[33;33;6m\u2588\x1b[0m\x1b[33;33;6m\u2580\x1b[0m'
  return str(A)



Num = 0
while 1 == 1:
  Words = Saysomething(INPUT)
  Num +=1
  #Pi_A = Comple(" \n"+Pikachu(i%6+1))
  Pi_pika = Comple(" \n"*(len(Words.split("\n")) - 1)+tailN_rm(Pikachu(Num%6+1)))
  Pi_pika = Easy_Com(Pi_pika,Words,0)
  os.system("clear")
  print(Pi_pika)
  #print(Words,Pikachu(Num%6+1),sep='\n')
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

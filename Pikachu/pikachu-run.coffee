import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input')     #输入文件

args = parser.parse_args()
INPUT = args.input
########

pix = '\u2588'*2
f = open(INPUT)
f = f.read()
A=f.replace("$","\x1b[30;2;6m"+ pix +"\x1b[0m").replace('l',"\x1b[33;3;6m"+ pix +"\x1b[0m").replace('/',"\x1b[30;0;2m"+ pix +"\x1b[0m").replace('B',"\x1b[31;3;2m"+ pix +"\x1b[0m").replace('C',"\x1b[0;1;1m"+ pix +"\x1b[0m").replace('L',"\x1b[30;2;1m"+ pix +"\x1b[0m").replace(' ','  ')


print(A)

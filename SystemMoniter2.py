#time
'''
for  CPU tm model
Ubunt
sudo apt-get install lm-sensors
sudo sensors-detect
sudo service kmod start

'''
import os, time
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pyfiglet


def time_get():
  Time = os.popen("date").read().replace('  ',' ').replace('\n','').split(' ')
  T = Time[3].split(':')
  Now_time = pyfiglet.figlet_format(T[0]+" : "+T[1])
  T_Date = Time[-1]+" "+Time[1] +" "+Time[2]+" "+Time[0]
  return Now_time,T_Date

def FtoC(A):
  if len(A.split(" ")) == 1 and "°" in A :
    A = int(str(A).replace("°",'').replace('F',''))
    Result = str(round((A - 32) * 5/9,1))+'°C'
  else:
    Result = ''
    for i in A.split(' '):
      if "°" in i :
        A = int(str(i).replace("°",'').replace('F',''))
        B = str(round((A - 32) * 5/9,1))+'°C'
      else:
        B = i
      Result += B + ' '
    Result += "  "
    Result = Result.replace("   ",'')
  return Result

def weather_get():
  try:
    url = 'https://weather.com/weather/today/l/32.75,-117.06?par=google'
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    # get result
    Now_Tm = soup.find('div',{'class':'today_nowcard-temp'}).get_text()
    Now_weather = soup.find('div',{'class':'today_nowcard-phrase'}).get_text()
    Now_feels = soup.find('div',{'class':'today_nowcard-feels'}).get_text()
    Now_hilo = soup.find('div',{'class':'today_nowcard-hilo'}).get_text()
    try:
      Now_hilo = Now_hilo.replace("UV",' UV')
    except:
      Now_hilo = Now_hilo
    # table result
    Now_table = soup.find('div',{'class':'today_nowcard-sidecar component panel'}).find_all('tr')
    Now_TB = ""
    for i in Now_table:
      TB_H = i.find('th').get_text()
      TB_T = i.get_text().replace(TB_H,"")
      TB_T = FtoC(TB_T)
      TB_T = "\t"+TB_T
      if len(TB_H) <= 4 :
        TB_H = TB_H + "\t"
      Now_TB += TB_H+TB_T+'\n'
    #remove tail
    Now_TB = Now_TB + "\n"
    Now_TB = Now_TB.replace("\n\n",'')
    # result
    Now_result=FtoC(Now_Tm)+"\t"+FtoC(Now_feels)+'\n'+FtoC(Now_hilo)+'\n'+Now_TB
    Now_TM = pyfiglet.figlet_format(FtoC(Now_Tm))
  except:
    Now_TM = pyfiglet.figlet_format(FtoC("XX"))
    Now_result = "Some thing wrong with the weather, please check the inter"
  return Now_TM,Now_result

def align_lift(STR):
  T_rows, T_columns = os.popen('stty size', 'r').read().split()
  N_lift = int(T_columns) - len(STR)
  return  " "*N_lift + STR

def power_get():
  CMD = "cat /sys/class/power_supply/BAT0/capacity"
  CMD2 = "cat /sys/class/power_supply/BAT0/uevent| grep 'POWER_SUPPLY_STATUS='| sed 's/POWER_SUPPLY_STATUS=//'"
  Now_power_N = os.popen(CMD).read()
  Power_Charge = os.popen(CMD2).read().replace('\n','')
  if Power_Charge =="Charging":
    P_head = "\u26A1 Battery "
    N_num=11
  else:
    P_head = "Battery "
    N_num=8
  #Now_power_N = "4"
  Clo1 = "93"
  Clo2 = "32"
  if int(Now_power_N) < 90:
    Clo2="33"
  if int(Now_power_N) < 50:
    Clo2="35"
  if int(Now_power_N) < 20:
    Clo2="31"
  if int(Now_power_N) < 10:
    Clo1="43"
  Now_power = Now_power_N+"%"+"\x1b["+str(Clo1)+";"+(Clo2)+";6m"+"\u4DF2\u2758"*int(int(Now_power_N)/4) +"\x1b[0m"
  Now_power = P_head +Now_power.replace('\n','')
  Now_power =  " "*(int(T_columns) - int(int(Now_power_N)/4)*2-N_num-len(Now_power_N))+ Now_power
  return Now_power
# the rows and the columns of current terminal

def Mem_get():
  Me_used = int(Top_list[3].split(" ")[8])/1024/1024
  Me_free = int(Top_list[3].split(" ")[5])/1024/1024
  Me_used_n = str(round(Me_used,2))+"G"
  Me_free_n = str(round(Me_free,2))+"G"
  Me_used_bar = Col_bar2(Me_used,62,6,32,47)
  return Me_used_bar,Me_used_n,Me_free_n

Bar_sub={'0':' ','1':"\u2581",'2':"\u2582",'3':"\u2583",'4':"\u2584",'5':"\u2585",'6':"\u2586",'7':"\u2587",'8':"\u2588"}

def Col_bar(N_1,N_2,Clo,Clo2=44):
  if int(N_1) != int(N_2):
    B_tail = ("\n\x1b["+str(Clo)+";104;6m\u2588\x1b[0m")*int(N_1)
    B_head = " \n"*(int(N_2-N_1))
    #B_head = "\n"+B_head
    #B_head = B_head.replace("\n\n",'')
    B_mid = "\x1b["+str(Clo)+";"+str(Clo2)+";6m"+Bar_sub[str(int(int(str(float(N_1)).split('.')[1][0])/10*8))]+"\x1b[0m"
    Bar = B_head +B_mid +B_tail
  else:
    Bar  = "\u2588"+"\n\u2588"*(N_2-1)
  return Bar

def Col_bar2(N_real,N_max,N_bar=6,Clo_B1=32,Clo_B2=44,Clo_Tr=0.7,Clo_C1=92,Clo_C2=44):
  N_rate = round(float(N_real)/float(N_max),2)
  if int(N_real) != int(N_max):
    if int(N_real)/int(N_max) < Clo_Tr:
      Clo_B1=Clo_B1
    else:
      Clo_B1 = Clo_C1
      Clo_B2 = Clo_C2
    B_tail = ("\n\x1b["+str(Clo_B1)+";104;6m\u2588\x1b[0m")*int(N_rate*N_bar)
    #print(B_tail)
    if int(N_rate*N_bar) == float(N_rate*N_bar):
      B_head = " \n"*(int((1-N_rate)*(N_bar-1)))
    else:
      B_head = " \n"*(int((1-N_rate)*(N_bar)))
    N_mid = str(round(float(N_rate*N_bar),2)).split(".")[1]
    N_mid = str(int(float("0."+N_mid)*8))
    #B_head = B_head.replace("\n\n",'')
    B_mid = "\x1b["+str(Clo_B1)+";"+str(Clo_B2)+";6m"+Bar_sub[N_mid]+"\x1b[0m"
    Bar = B_head +B_mid +B_tail
    Bar = Bar.replace('\n\n','\n')
  else:
    Bar  = "\x1b[91;104;6m\u2588\x1b[0m"+"\n\x1b[91;104;6m\u2588\x1b[0m"*(N_bar-1)
  return Bar
  #for test
  #result =''
  #for i in range(len(Bar.split('\n'))):
  #  result +=Bar.split('\n')[i]+str(i+1)+'\n'
  #return result

def Row_bar2(N_real,N_max,N_bar=6,Clo_B1=32,Clo_B2=44,Clo_Tr=0.7,Clo_C1=92,Clo_C2=44):
  N_rate = round(float(N_real)/float(N_max),2)
  if int(N_real) != int(N_max):
    if int(N_real)/int(N_max) < Clo_Tr:
      Clo_B1=Clo_B1
    else:
      Clo_B1 = Clo_C1
      Clo_B2 = Clo_C2
    B_tail = ("\x1b["+str(Clo_B1)+";104;6m\u2588\x1b[0m")*int(N_rate*N_bar)
    #print(B_tail)
    if int(N_rate*N_bar) == float(N_rate*N_bar):
      B_head = " "*(int((1-N_rate)*(N_bar-1)))
    else:
      B_head = " "*(int((1-N_rate)*(N_bar)))
    N_mid = str(round(float(N_rate*N_bar),2)).split(".")[1]
    N_mid = str(int(float("0."+N_mid)*8))
    #B_head = B_head.replace("\n\n",'')
    B_mid = "\x1b["+str(Clo_B1)+";"+str(Clo_B2)+";6m"+Bar_sub[N_mid]+"\x1b[0m"
    Bar = B_head +B_mid +B_tail
    #Bar = Bar.replace('\n\n','\n')
  else:
    Bar  = "\x1b[91;104;6m\u2588\x1b[0m"+"\x1b[91;104;6m\u2588\x1b[0m"*(N_bar-1)
  return Bar
  #for test
  #result =''
  #for i in range(len(Bar.split('\n'))):
  #  result +=Bar.split('\n')[i]+str(i+1)+'\n'
  #return result

def Cpu_TM():
  CMD = "sensors| grep Package| awk '{print $4}'"
  TM_cpu = os.popen(CMD).read().replace("\n",'')
  TM_n = TM_cpu.replace('+','').replace("°C",'')
  TM_n = float(TM_n)
  TM_cpuBar = Col_bar2(TM_n,100,6,32,44,0.6,31,47)
  return TM_cpu,TM_cpuBar

def Cpu_use():
  for i in Top_list:
    if "Cpu" in i:
      Cpu_u = i.replace("  ",' ')
  Cpu_u = Cpu_u.split(' ')[1]
  Cpu_bar = Col_bar2(float(Cpu_u),100,6,92,43,0.4,31,44)
  return Cpu_u+"%",Cpu_bar

def Cpu_top1():
  return Top_list[6]+Top_list[7]


Now_TM,Now_weather = weather_get()
'''
while 1 < 2:
  os.system('clear')
  print(Col_bar(2,3))
  time.sleep(1)


Now_time = time_get()
Now_power = power_get()
Mem = Mem_get()
TM_cpu,TM_cpuBar = Cpu_TM()

os.system("clear")
Line_1 = ""
for i in range(5):
  Line_1 += Now_time.split("\n")[i]+'\t\t'+Now_TM.split('\n')[i] + "\n"

print(Now_power,Line_1,Now_weather,Mem,TM_cpuBar,sep='\n')
'''

Num=0
while 1 < 2:
  Top_board= os.popen("top -d0.2 -n 2").read()
  Top_list = Top_board.split('\n')
  T_rows, T_columns = os.popen('stty size', 'r').read().split()
  Num +=1
  if Num%30 == 0:
    Now_TM,Now_weather = weather_get()  # 30*10/60 = 5min, update the information of weather 5mins per time
  Now_time,Now_Date = time_get()
  Now_power = power_get()
  Mem_bar,Mem_used,Mem_free = Mem_get()
  TM_cpu,TM_cpuBar = Cpu_TM()
  Cpu_u,Cpu_bar = Cpu_use()
  Cpu_top = Cpu_top1()

  Line_1 = ""
  for i in range(5):
    Line_1 += Now_time.split("\n")[i]+'\t\t'+Now_TM.split('\n')[i] + "\n"
  Line_1 = Line_1+Now_Date+"\n" # add full date
  Line_2="\nMem used:\t"+Mem_used+"\nMem free:\t"+Mem_free+"\nCPU Tem:\t"+TM_cpu+'\nCPU use:\t'+Cpu_u+'\n\n'

  Bar_all=''
  for i in range(6):
    Bar_all +=   Mem_bar.split('\n')[i]+" "+  TM_cpuBar.split('\n')[i] +" "+Cpu_bar.split('\n')[i]+"\t\t" + Line_2.split('\n')[i]+'\n'


  os.system("clear")
  print(Now_power,Line_1,Now_weather,Bar_all,Cpu_top,sep='\n')
  time.sleep(3) # upadate the 10s per time



'''
for i in range(100):
  B = "\x1b["+str(i)+";104;6m"+ "\u2588 "*20 +"\x1b[0m"
  print(B,i)

for i in range(100):
  B = "\x1b[31;"+str(i)+";6m"+ "\u2588 "*20 +"\x1b[0m"
  print(B,i)

B = "\x1b[91;104;6m"+ "\u2588 "*20 +"\x1b[0m"
print(B)
'''

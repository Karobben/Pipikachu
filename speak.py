#!/usr/local/bin/python3.7
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input')     #输入文件

args = parser.parse_args()
INPUT = args.input

import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice','english_rp') ##Change the voice
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50) ##spead rate
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+0.25) ##change the volume
print(INPUT)
engine.say(INPUT)
engine.runAndWait()

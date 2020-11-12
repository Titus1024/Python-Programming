#!/usr/bin/env python3
import subprocess
def GetProcess():
    result = subprocess.run(['ps','-axco','command'],stdout=subprocess.PIPE)
    return result
MyProc = GetProcess()
MyProcString = MyProc.stdout.decode()
MyProcList = MyProc.stdout.decode().split('\n')[1:]
print(type(MyProc))
print(type(MyProcString))
print(type(MyProcList))
print(len(MyProcList))
for Line in MyProcList:
    print(Line)
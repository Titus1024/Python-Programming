#!/usr/bin/env python3.8
import subprocess
def GetProcess():
    result = subprocess.run(['ps','-axco','command'],stdout=subprocess.PIPE)
    return result.stdout.decode.split()

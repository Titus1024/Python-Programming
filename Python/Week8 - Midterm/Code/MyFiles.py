#!/usr/bin/env python3
Data = open('PythonMidtermFile.txt','r')
strfiletext = Data.readlines()
print(len(strfiletext))
print(type(strfiletext))
Data.close
#!/usr/bin/env python3
MyFQDN = dict()
MyFQDN['server1.testlab.com'] = '192.168.1.10'
MyFQDN['server2.testlab.com'] = '192.168.1.11'
MyFQDN['server3.testlab.com'] = '192.168.1.12'
MyFQDN['server4.testlab.com'] = '192.168.1.13'
MyFQDN['server5.testlab.com'] = '192.168.1.14'
MyFQDN['server6.testlab.com'] = '192.168.1.15'
MyFQDN['server7.testlab.com'] = '192.168.1.17'
MyFQDN['server8.testlab.com'] = '192.168.1.16'
print(MyFQDN.keys())
print(MyFQDN.values())
print(MyFQDN.items())
print('server2.testlab.com' in MyFQDN)
print('server10.testlab.com' in MyFQDN)
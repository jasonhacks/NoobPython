#!/usr/bin/python
sortList = open('ip.txt').read().splitlines()
sortList.sort(key=lambda x: int(x.split('.')[0]))

for ip in sortList:
        print ip

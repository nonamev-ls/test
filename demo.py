#!/bin/python
import uuid
import sys
times = 0
end = 0
id = input('Please enter your id:')
def priuuid(times):
    name = str(id)+str(times)
    namespace = uuid.NAMESPACE_URL
    pri = uuid.uuid5(namespace,name)#.replace("-","  ")
    print('Your private key is '+str(pri))#.replace("  ","-"))
def exit(exitmun):
    if exitmun == 2:
        print('About')
        sys.exit()
priuuid(times)
y = input('Do you want to spawn it again?[Y/n]')
if y == 'y' or y == 'Y':
    while end == 0:
        times += 1
        priuuid(times)
        y1 = input('Do you want to spawn it again?[Y/n]')
        if y1 == 'y' or y1 == 'Y':
            pass
        else:
            if y1 == 'n' or y1 == 'N':
                exit(2)
            else:
                break
else:
    if y == 'n' or y == 'N':
        exit(2)
    else:
        sys.exit()

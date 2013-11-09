#!/usr/bin/env python3
from switch import AT8000_16
'''
#from Zabbix import ZabbixTemplate

#print(ITEMS)

#print(len(ITEMS))
#for item in ITEMS:
#        print(item[0],item[1],item[2],item[3],item[4])

import Models
print(Models.model_by_ip.__doc__)
for last_octet in range(1,255):
    try:
        model = (Models.model_by_ip('172.16.2.' + str(last_octet)))
    except NotImplementedError as exc:
        print(exc)
    tmpl = ZabbixTemplate(model)
'''

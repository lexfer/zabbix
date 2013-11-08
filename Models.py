#!/usr/bin/env python3
import sys
import os
from subprocess import getstatusoutput

def model_by_ip(ip_addr):
    """Get model switch by snmp. Return name of switch as
    name of module in switch packadge"""
    status,out =  getstatusoutput('snmpwalk -v 1 -c mrtg ' + \
            ip_addr + ' sysDescr.0')
    if status == 0 and '8000S' in out:
        status,model_port =  getstatusoutput('snmpwalk -v 1 -c mrtg ' + \
            ip_addr + ' mib-2.47.1.1.1.1.7.68420352')
        if '8000S/16' in model_port:
            model = 'AT8000_16'
        elif '8000S/24' in model_port:
            model = 'AT8000_24'
        elif '8000S/48' in model_port:
            model = 'AT8000_48'
        else:
            raise NotImplementedError('Unknown model Allied Telesis')
    elif status == 0 and '8012' in out:
        model = 'AT8012'
    elif status == 0 and 'AT-9924SP' in out:
        model = 'AT_9924SP'
    elif status == 0 and 'MES-3124F' in out:
        model = 'MES_3124F'
    elif status == 0 and 'MES-1024' in out:
        model = 'MES_1024'
    elif status == 0 and 'MES-3124' in out:
        model = 'MES_3124'
    elif status == 0 and 'MES-3024' in out:
        model = 'MES_3024'
    elif status == 0 and 'MES-2124' in out:
        model = 'MES_2124'
    elif status == 0 and 'ES-2024A' in out:
        model = 'ES_2024A'
    elif status == 0 and 'ES-2108' in out:
        model = 'ES_2108'
    elif status == 0 and 'DGS-3627G' in out:
        model = 'DGS_3627G'
    elif status == 0 and 'DES-2108' in out:
        model = 'DES_2108'
    elif status == 0 and 'C3550' in out:
        status,model_port = getstatusoutput('snmpwalk -v1 -c mrtg ' + \
                ip_addr +' SNMPv2-SMI::mib-2.47.1.1.1.1.2.1')
        if '3550 24' in model_port:
            model = 'C3550_24'
        elif '3550 48' in model_port:
            model = 'C3550_48'
        elif '3550 10' in model_port:
            model = 'C3550_12'
        else:
            raise NotImplementedError('Unknown model Cisco 3550')
    elif status == 0 and '3Com SuperStack 3 Switch 3250' in out:
        model = '3Com_SuperStack_50'
    elif status == 0 and '3Com SuperStack 3 Switch 3226' in out:
        model = '3Com_SuperStack_26'
    elif status == 0:
        raise NotImplementedError('switch with ip: \
                {0} is {1}'.format(ip_addr,'UNKNOWN'))
    else:
        raise NotImplementedError('no answer from ip: ' + ip_addr)
    return model

if __name__ == '__main__':
    try:
        model = model_by_ip(sys.argv[1])
        print(model)
    except NotImplementedError as exc:
        print(exc)

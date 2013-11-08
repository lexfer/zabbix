PORT_COUNT = 26
TEMPLATE_NAME = 'AT8000-24 switch'
TEMPLATE_GROUP = 'Switches'
PORT_NAMES = {n:'ethernet e' + str(n) for n in range(1,25)}
PORT_NAMES[25] = 'ethernet g1'
PORT_NAMES[26] = 'ethernet g2'
#list: ItemName, SNMP OID Name, SNMP_OID, UNIT, DESCRIPTION, color, drawtype
ITEMS_TMPL = [[ 'ifInOctets',
                'ifInOctets.',
                '.1.3.6.1.2.1.2.2.1.10.',
                'bps',
                'RX(input) byte port',
                '0000C8',
                '2'],
                [
                'ifOutOctets',
                'ifOutOctets.',
                '.1.3.6.1.2.1.2.2.1.16.',
                'bps',
                'TX(output) byte port ',
                '00BB00',
                '2'],
                [
                'ifInBroadcastPkts',
                'ifInBroadcastPkts.',
                '.1.3.6.1.2.1.31.1.1.1.3.',
                'pps',
                'RX(input) broadcast packet port',
                'EE0000',
                '1'],
                [
                'ifOutBroadcastPkts',
                'ifOutBroadcastPkts.',
                '.1.3.6.1.2.1.31.1.1.1.5.',
                'pps',
                'TX(output) broadcast packet port',
                'EEEE00',
                '1'],
                [
                'ifInMulticastPkts',
                'ifInMulticastPkts.',
                '.1.3.6.1.2.1.31.1.1.1.2.',
                'pps',
                'RX(input) multicast packet port',
                'FF66FF',
                '1'],
                [
                'ifOutMulticastPkts',
                'ifOutMulticastPkts.',
                '.1.3.6.1.2.1.31.1.1.1.4.',
                'pps',
                'TX(output) multicast packet port',
                '99FFFF',
                '1']]

#list of lists with items
#generate item list for 1-24 port
ITEMS = [] #for GenItems
PORT_ITEMS = {} #for GenGraphs

for port in range(1,25):
    ITEMS_SETS = []
    for item_list in ITEMS_TMPL:
        mod_item_list = item_list.copy()
        mod_item_list[0] = item_list[0] + ' ' + PORT_NAMES[port]
        mod_item_list[1] = item_list[1] + str(port)
        mod_item_list[2] = item_list[2] + str(port)
        mod_item_list[4] = item_list[4] + ' ' + PORT_NAMES[port]
        ITEMS_SETS.append(mod_item_list)
        ITEMS.append(mod_item_list)
    PORT_ITEMS[PORT_NAMES[port]] = ITEMS_SETS

#for port g1 and g2 snmp OID with offset 24
#Example: .1.3.6.1.2.1.31.1.1.1.2.[49]
for port in (25,26):
    ITEMS_SETS = []
    for item_list in ITEMS_TMPL:
        mod_item_list = item_list.copy()
        mod_item_list[0] = item_list[0] + ' ' + PORT_NAMES[port]
        mod_item_list[1] = item_list[1] + str(port + 24)
        mod_item_list[2] = item_list[2] + str(port + 24)
        mod_item_list[4] = item_list[4] + ' ' + PORT_NAMES[port]
        ITEMS_SETS.append(mod_item_list)
        ITEMS.append(mod_item_list)
    PORT_ITEMS[PORT_NAMES[port]] = ITEMS_SETS

#for i in ITEMS:
#    print(i)
'''
for port in PORT_ITEMS.keys():
    for item in (PORT_ITEMS[port]):
        print(item[0])
'''

PORT_COUNT = 28
TEMPLATE_NAME = 'MES_3124 switch'
TEMPLATE_GROUP = 'Switches'
PORT_NAMES = {n:'gigabitethernet 1/0/' + str(n) for n in range(1,25)}
PORT_NAMES[25] = 'tengigabitethernet 1/0/1'
PORT_NAMES[26] = 'tengigabitethernet 1/0/2'
PORT_NAMES[27] = 'tengigabitethernet 1/0/3'
PORT_NAMES[28] = 'tengigabitethernet 1/0/4'

#list: ItemName, SNMP OID Name, SNMP_OID, UNIT, DESCRIPTION, color, drawtype
from switch.common import ITEMS_TMPL
#list of lists with items
#generate item list for 1-24 port
ITEMS = [] #for GenItems
PORT_ITEMS = {} #for GenGraphs

for last_octet_oid in range(49,73):
    port = last_octet_oid - 48
    ITEMS_SETS = []
    for item_list in ITEMS_TMPL:
        mod_item_list = item_list.copy()
        mod_item_list[0] = item_list[0] + ' ' + PORT_NAMES[port]
        mod_item_list[1] = item_list[1] + str(last_octet_oid)
        mod_item_list[2] = item_list[2] + str(last_octet_oid)
        mod_item_list[4] = item_list[4] + ' ' + PORT_NAMES[port]
        ITEMS_SETS.append(mod_item_list)
        ITEMS.append(mod_item_list)
    PORT_ITEMS[PORT_NAMES[port]] = ITEMS_SETS

#for port g1 and g2 snmp OID with offset 24
#Example: .1.3.6.1.2.1.31.1.1.1.2.[49]
for last_octet_oid in range(105,109):
    port = last_octet_oid - 80	 
    ITEMS_SETS = []
    for item_list in ITEMS_TMPL:
        mod_item_list = item_list.copy()
        mod_item_list[0] = item_list[0] + ' ' + PORT_NAMES[port]
        mod_item_list[1] = item_list[1] + str(last_octet_oid)
        mod_item_list[2] = item_list[2] + str(last_octet_oid)
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

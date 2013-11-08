PORT_COUNT = 8
TEMPLATE_NAME = 'Zyxel es2108 switch'
TEMPLATE_GROUP = 'Switches'
PORT_NAMES = {n:'port-channel ' + str(n) for n in range(1,PORT_COUNT+1)}
#list: ItemName, SNMP OID Name, SNMP_OID, UNIT, DESCRIPTION, color, drawtype
from switch.common import ITEMS_TMPL
#list of lists with items
#generate item list for 1-24 port
ITEMS = [] #for GenItems
PORT_ITEMS = {} #for GenGraphs

for port in range(1,PORT_COUNT+1):
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

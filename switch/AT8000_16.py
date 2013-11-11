from switch.common import getItem
PORT_COUNT = 28
TEMPLATE_NAME = 'Eltex MES3124F switch'
TEMPLATE_GROUP = 'Switches'
prange1 = { 'pnum': set(range(1,24 + 1)),
            'last_oid': set(range(49,72 + 1)),
            'ifname': 'GigabitEthernet'}
prange2 = {'pnum': set(range(25,28 + 1 )),
            'last_oid': set(range(105,108 + 1)),
            'ifname': 'TenGigabitEthernet'}

ITEMS,GRAPHS = getItem(prange1,prange2)

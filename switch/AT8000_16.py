from switch import common_new
PORT_COUNT = 16
TEMPLATE_NAME = 'AT8000-16 switch'
TEMPLATE_GROUP = 'Switches'
prange1 = { 'pnum': set(range(1,24 + 1)),
            'last_oid': set(range(49,72 + 1)),
            'ifname': 'GigabitEthernet'}
prange2 = {'pnum': set(range(25,28 + 1 )),
            'last_oid': set(range(105,108 + 1)),
            'ifname': 'TenGigabitEthernet'}

ITEMS = common_new.getItem(prange1,prange2)
for i in ITEMS:
    print(i)

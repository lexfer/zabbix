ifInOctets =  { 'item_key': 'ifInOctets.',
                'item_name': 'ifInOctets',
                'item_oid': '.1.3.6.1.2.1.2.2.1.10.',
                'item_unit': 'bps',
                'item_description': 'RX(input) byte ',
                'graph_color': '0000C8',
                'graph_drawtype': '2',
               }

ifOutOctets = { 'item_key': 'ifOutOctets.',
                'item_name': 'ifOutOctets',
                'item_oid': '.1.3.6.1.2.1.2.2.1.16.',
                'item_unit': 'bps',
                'item_description': 'TX(output) byte ',
                'graph_color': '00BB00',
                'graph_drawtype': '2',
                }

ifInBroadcastPkts = { 'item_key': 'ifInBroadcastPkts.',
                      'item_name': 'ifInBroadcastPkts',
                      'item_oid': '.1.3.6.1.2.1.31.1.1.1.3.',
                      'item_unit': 'pps',
                      'item_description': 'RX(input) broadcast packet ',
                      'graph_color': 'EE0000',
                      'graph_drawtype': '1',
                    }

ifOutBroadcastPkts = { 'item_key': 'ifOutBroadcastPkts.',
                       'item_name': 'ifOutBroadcastPkts',
                       'item_oid':  '.1.3.6.1.2.1.31.1.1.1.5.',
                       'item_unit': 'pps',
                       'item_description': 'TX(output) broadcast packet ',
                       'graph_color': 'EEEE00',
                       'graph_drawtype': '1',
                       }

ifInMulticastPkts = { 'item_key': 'ifInMulticastPkts.',
                      'item_name': 'ifInMulticastPkts',
                      'item_oid':  '.1.3.6.1.2.1.31.1.1.1.2.',
                      'item_unit': 'pps',
                      'item_description': 'RX(input) multicast packet ',
                      'graph_color': 'FF66FF',
                      'graph_drawtype': '1',
                    }

ifOutMulticastPkts = { 'item_key': 'ifOutMulticastPkts.',
                       'item_name': 'ifOutMulticastPkts',
                       'item_oid': '.1.3.6.1.2.1.31.1.1.1.4.',
                       'item_unit': 'pps',
                       'item_description': 'TX(output) multicast packet ',
                       'graph_color':'99FFFF',
                       'graph_drawtype': '1',
                    }
_itemlist = [ifInOctets,ifOutOctets,ifInBroadcastPkts,
        ifOutBroadcastPkts,ifInMulticastPkts,
        ifOutMulticastPkts]
'''
def getItem(*args):
    for prange in args:
        for p,z in zip(range(prange['pnum'][0],
                prange['pnum'][1] + 1),
                range(prange['last_oid'][0],
                    prange['last_oid'][1] + 1)):
            print(p,z)
'''
def getItem(*args):
    items = []
    for prange in args:
        for pn,on in zip(prange['pnum'],
                prange['last_oid']):
            for item_instance in _itemlist:
                item = item_instance.copy()
                item['item_key'] = item_instance['item_key'] + str(pn)
                item['item_name'] = item_instance['item_name'] + str(pn)
                item['item_oid'] = item_instance['item_oid'] + str(on)
                item['item_description'] = item_instance['item_description'] + \
                        prange['ifname'] + str(pn)
                items.append(item)
    return(items)

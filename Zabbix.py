import xml.etree.ElementTree as etree
from xml.dom import minidom
import sys
#from importlib import import_module
# -*- coding: utf-8 -*-

class ZabbixTemplate:
    """класс создаёт темплейты свитчей для zabbix"""
    root = etree.Element("zabbix_export")
    version = etree.SubElement(root, "version")
    version.text = '2.0'
    date = etree.SubElement(root, "date")
    date.text = '013-10-18T07:20:05Z'
    groups = etree.SubElement(root, "groups")
    group = etree.SubElement(groups, "group")
    ngroup = etree.SubElement(group, "name")
    ngroup.text = 'Switches'
    templates = etree.SubElement(root, "templates")
    template = etree.SubElement(templates, "template")
    template_1 = etree.SubElement(template, "template")
    template_name = etree.SubElement(template, "name")
    groups_template = etree.SubElement(template, "groups")
    group_template = etree.SubElement(groups_template, "group")
    group_name = etree.SubElement(group_template, "name")
    etree.SubElement(template, "applications")
    items = etree.SubElement(template, "items")

    def __init__(self, model):
        """Ищем в каталоге switch соответствующий модуль и если он существует
        пытаемся загрузить его атрибуты"""
        self.model = model
        try:
            mod = __import__('switch.'+model,globals(),locals(),
                    ['ITEMS', 'GRAPHS', 'TEMPLATE_NAME','TEMPLATE_GROUP'],0)
            self.ITEMS = mod.ITEMS
            self.GRAPHS = mod.GRAPHS
            self.TEMPLATE_NAME = mod.TEMPLATE_NAME
            self.TEMPLATE_GROUP = mod.TEMPLATE_GROUP
            print("for switch {0} uses module {1}".format(model,mod),
                    file=sys.stderr)
        except ImportError:
            print(" Not found module for switch " + model)

    def GenItems(self):
        """self.ITEMS импортированный из модуля свитча кортеж кортежей
        self.ITEMS=((ItemName, SNMP OID Name, SNMP_OID, UNIT, DESCRIPTION),)"""
        for itemdict in self.ITEMS:
                item = etree.SubElement(self.items, "item")
                name = etree.SubElement(item, "name")
                name.text = itemdict['item_name']
                type_item = etree.SubElement(item, "type")
                type_item.text = '1'
                snmp_community = etree.SubElement(item, "snmp_community")
                snmp_community.text = 'mrtg'
                multiplier = etree.SubElement(item, "multiplier")
                multiplier.text = itemdict['item_multiplier']
                snmp_oid = etree.SubElement(item, "snmp_oid")
                snmp_oid.text = itemdict['item_oid']
                key = etree.SubElement(item, "key")
                key.text = itemdict['item_key']
                delay = etree.SubElement(item, "delay")
                delay.text = '60'
                history = etree.SubElement(item, "history")
                history.text = '30'
                trends = etree.SubElement(item, "trends")
                trends.text = '365'
                status = etree.SubElement(item, "status")
                status.text = '0'
                value_type = etree.SubElement(item, "value_type")
                value_type.text = '3'
                units = etree.SubElement(item, "units")
                units.text = itemdict['item_unit']
                delta = etree.SubElement(item, "delta")
                delta.text = '1'
                formula = etree.SubElement(item, "formula")
                formula.text = itemdict['item_formula']
                data_type = etree.SubElement(item, "data_type")
                data_type.text = '0'
                authtype = etree.SubElement(item, "authtype")
                authtype.text = '0'
                snmp_port = etree.SubElement(item, "port")
                snmp_port.text = '161'
                desctiption = etree.SubElement(item, "description")
                desctiption.text = itemdict['item_description']
                desctiption = etree.SubElement(item, "description")
                inventory_link = etree.SubElement(item, "inventory_link")
                inventory_link.text = '0'

    def GenGraphs(self):
        graphs = etree.SubElement(self.root, "graphs")
        for iface in self.GRAPHS.keys():
            graph = etree.SubElement(graphs, "graph")
            name = etree.SubElement(graph, "name")
            name.text = iface
            width = etree.SubElement(graph, "width")
            width.text = '500'
            height = etree.SubElement(graph, "height")
            height.text = '100'
            graph_items = etree.SubElement(graph, "graph_items")
            for graph in self.GRAPHS[iface]:
                graph_item = etree.SubElement(graph_items, "graph_item")
                sortorder = etree.SubElement(graph_item, "sortorder")
                sortorder.text = graph['graph_sortorder']
                drawtype = etree.SubElement(graph_item, "drawtype")
                drawtype.text = graph['graph_drawtype']
                color = etree.SubElement(graph_item, "color")
                color.text = graph['graph_color']
                yaxisside = etree.SubElement(graph_item, "yaxisside")
                yaxisside.text = '0'
                calc_fnc = etree.SubElement(graph_item, "calc_fnc")
                calc_fnc.text = '2'
                type_graph = etree.SubElement(graph_item, "type")
                type_graph.text = '0'
                item_g = etree.SubElement(graph_item, "item")
                host = etree.SubElement(item_g, "host")
                host.text = self.TEMPLATE_NAME
                key = etree.SubElement(item_g, "key")
                key.text = graph['item_key']

    def GetTemplate(self):
        """Установка названий темплейтов и групп,
        вызов функуии генерации items"""
        self.template_1.text = self.TEMPLATE_NAME
        self.template_name.text = self.TEMPLATE_NAME
        self.group_name.text = self.TEMPLATE_GROUP
        self.GenItems()
        self.GenGraphs()
        string_xml = etree.tostring(self.root,encoding="unicode",method="xml")
        dom = minidom.parseString(string_xml)
        prettyXML=dom.toprettyxml(indent='\t',newl='\n')
        sys.stdout.write(prettyXML)

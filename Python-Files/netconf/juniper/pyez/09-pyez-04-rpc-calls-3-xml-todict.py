from pprint import pprint
from jnpr.junos import Device
from lxml import etree
import xmltodict
import json

junos_device = Device(host='10.4.4.41', user='sntuser', password='Ilovenetworks99' )
junos_device.open()

output_file1 = open('09-pyez-04-rpc-calls-3-xml-todict.json', 'w')

output = junos_device.rpc.get_interface_information(interface_name='fxp0.0')

xml_serial = etree.tostring(output)
# xml_serial is serialized xml without all the prettin indenting.

# Make a dictionary from the serail xml.
# xmltodict.unparse for the opposite is available.
xml_dict = xmltodict.parse(xml_serial)
output_file1.write(json.dumps(xml_dict, indent=4))
print(json.dumps(xml_dict))

junos_device.close()
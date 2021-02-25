from pprint import pprint
from jnpr.junos import Device
from lxml import etree
import xmltodict

junos_device = Device(host='10.4.4.41', user='sntuser', password='Ilovenetworks99' )
junos_device.open()

output_file1 = open('09-pyez-04-rpc-calls-2-to-file.xml', 'w')

output4 = junos_device.rpc.get_interface_information(interface_name='fxp0.0')
# output4 is an lxml.etree._Element, so we need etree from lmxl module
# to convert it for printing.
for_file = etree.tostring(output4, encoding='unicode', pretty_print=True)
output_file1.write(for_file)

junos_device.close()
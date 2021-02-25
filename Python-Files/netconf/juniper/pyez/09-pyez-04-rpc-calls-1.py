from pprint import pprint
from jnpr.junos import Device
from lxml import etree

junos_device = Device(host='10.4.4.41', user='sntuser', password='Ilovenetworks99' )
junos_device.open()

# This converts the cli command given into the correct rpc call if possible.
output2 = junos_device.cli_to_rpc_string('show interfaces terse')
print(type(output2))
pprint(output2)
# so the correct rpc command to execute would be:
# 'rpc.get_interface_information(terse=True)'
#  So we should run the full command:
output3 = junos_device.rpc.get_interface_information(terse=True)
print(type(output3))
# output3 is an lxml.etree._Element, so we need to etree from lmxl module
# to convert it for printing.
print (etree.tostring(output3, encoding='unicode', pretty_print=True))

output4 = junos_device.rpc.get_interface_information(interface_name='fxp0.0')
print('*****************************************************************')
print (etree.tostring(output4, encoding='unicode', pretty_print=True))


junos_device.close()
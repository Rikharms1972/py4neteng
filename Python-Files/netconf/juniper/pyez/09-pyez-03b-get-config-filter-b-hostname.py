from jnpr.junos import Device
from lxml import etree

filter = '<system><host-name/></system>'
with Device(host='10.4.4.41', user='sntuser', password='Ilovenetworks99', use_filter=True) as dev:
    data = dev.rpc.get_config(filter_xml=filter)
    print (etree.tostring(data, encoding='unicode', pretty_print=True))
    output = etree.tostring(data, encoding='unicode', pretty_print=True)
    output2 = etree.tostring(data, encoding='unicode')

output_file = open(f'09-pyez-03b-get-config-filter-b-hostname.xml', 'w')
output_file.write(output)

output_file2 = open(f'09-pyez-03b-get-config-filter-b-hostname2.xml', 'w')
output_file2.write(output2)


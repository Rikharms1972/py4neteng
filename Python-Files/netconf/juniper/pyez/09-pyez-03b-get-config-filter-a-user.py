from jnpr.junos import Device
from lxml import etree

filter = '<system><login/></system>'
with Device(host='10.4.4.41', user='sntuser', password='Ilovenetworks99', use_filter=True) as dev:
    data = dev.rpc.get_config(filter_xml=filter)
    print (etree.tostring(data, encoding='unicode', pretty_print=True))
    output = etree.tostring(data, encoding='unicode', pretty_print=True)

output_file = open(f'09-pyez-03b-get-config-filter-a-user.xml', 'w')
output_file.write(output)


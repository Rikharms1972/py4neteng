from jnpr.junos import Device
from lxml import etree

with Device(host='10.4.4.41', user='sntuser', password='Ilovenetworks99') as dev:
    data = dev.rpc.get_config()
    print(type(data))
    print (etree.tostring(data, encoding='unicode', pretty_print=True))
    output = etree.tostring(data, encoding='unicode', pretty_print=True)

output_file = open(f'09-pyez-03a-get-config.xml', 'w')
output_file.write(output)

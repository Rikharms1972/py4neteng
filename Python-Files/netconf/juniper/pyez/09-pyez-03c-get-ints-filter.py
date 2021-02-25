from jnpr.junos import Device
from lxml import etree

with Device(host='10.4.4.41', user='sntuser', password='Ilovenetworks99', use_filter=True) as dev:
    filter = '<interface-information><physical-interface><name/></physical-interface></interface-information>'
    result = dev.rpc.get_interface_information(filter_xml=filter)
    for_file = (etree.tostring(result, encoding='unicode'))
print(for_file)

# output_file = open(f'09-pyez-03c-get-ints-filter.xml', 'w')
# output_file.write(for_file)

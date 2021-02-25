from jnpr.junos import Device
from lxml import etree
import json

with Device(host='10.4.4.41', user='sntuser', password='Ilovenetworks99') as dev:
    data_dict = dev.rpc.get_config(options={'format':'json'})
    #  other formats available: text, set
    print(data_dict)

data_json= json.dumps(data_dict, indent=2)
print(data_json)
output_file = open(f'09-pyez-03a-get-config-format-json.json', 'w')
output_file.write(data_json)

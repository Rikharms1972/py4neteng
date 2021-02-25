from pprint import pprint
from jnpr.junos import Device

junos_device = Device(host='10.4.4.41', user='sntuser', password='Ilovenetworks99' )
junos_device.open()

output = junos_device.cli('show configuration')
# output is a str so we can pprint it.
pprint(output)

junos_device.close()
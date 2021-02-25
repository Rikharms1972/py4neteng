from pprint import pprint
from jnpr.junos import Device

junos_device = Device(host='10.4.4.41', user='sntuser', password='Ilovenetworks99' )
junos_device.open()
pprint( junos_device.facts )
junos_device.close()
from pprint import pprint
from jnpr.junos import Device

with Device(host='10.4.4.41', user='sntuser', password='Ilovenetworks99' ) as dev:
    pprint( dev.facts )
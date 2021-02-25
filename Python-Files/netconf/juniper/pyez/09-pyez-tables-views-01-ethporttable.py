from jnpr.junos import Device
# Do not worry if your IDE flags the next import up.
# It will work.
from jnpr.junos.op.ethport import EthPortTable

with Device(host='10.4.4.41', user='sntuser', password='Ilovenetworks99') as dev:
    eths = EthPortTable(dev)
    eths.get()
    for port in eths:
        print ("{}: {}".format(port.name, port.oper))
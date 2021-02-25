import napalm

driver=napalm.get_network_driver("ios")
device = driver(hostname='10.99.99.9',
                username='sntuser',
                password='Ilovenetworks99',
                optional_args={'secret':'cisco'}
                )
device.open()

device.rollback()

device.close()
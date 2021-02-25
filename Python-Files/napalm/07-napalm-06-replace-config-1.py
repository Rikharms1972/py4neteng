import napalm

driver=napalm.get_network_driver("ios")
device = driver(hostname='10.99.99.9',
                username='sntuser',
                password='Ilovenetworks99',
                optional_args={'secret':'cisco'}
                )
device.open()

config_file = './Sw1-replace-banner-good.conf'

device.load_replace_candidate(config_file)

print(device.compare_config())

device.commit_config()

device.close()
import napalm

driver=napalm.get_network_driver("ios")
device = driver(hostname='10.99.99.9',
                username='sntuser',
                password='Ilovenetworks99',
                optional_args={'secret':'cisco'}
                )
device.open()

# config_file = './Sw1-merge.conf'
config_file = './Sw1-replace-banner-test.conf'
device.load_merge_candidate(config_file)

print(device.compare_config())

device.commit_config()

device.close()
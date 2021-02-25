import napalm

driver=napalm.get_network_driver("ios")

# The following is called a context manager and is
# the preferred pyhon way to do this as it opens/closes
# the connection automatically and cleans up after itself.
with driver(hostname='10.99.99.9',
                username='sntuser',
                password='Ilovenetworks99',
                optional_args={'secret':'cisco'}
                ) as device:

    config_file = './Sw1-merge.conf'
    device.load_merge_candidate(config_file)
    print(device.compare_config())
    device.commit_config()
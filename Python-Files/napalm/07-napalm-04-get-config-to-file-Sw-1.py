import napalm

driver=napalm.get_network_driver("ios")
router = driver(hostname='10.99.99.9',
                username='sntuser',
                password='Ilovenetworks99',
                optional_args={'secret':'cisco'}
                )
router.open()

# router_config = open('router_config.conf')
rtr_running_config = router.get_config(retrieve='running')
# router_config.write(router.get_config(retrieve='running'))
print(rtr_running_config)

router.close()
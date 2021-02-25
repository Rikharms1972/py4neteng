import napalm
import json
import pprint

driver=napalm.get_network_driver("ios")
router = driver(hostname='10.99.99.11',
                username='sntuser',
                password='Ilovenetworks99',
                optional_args={'secret':'cisco'}
                )
router.open()

validation_report = router.compliance_report('R1-config-check-2-facts-more.yaml')

# The indendation of the following can be a bit difficult.
print(json.dumps(validation_report, indent=4))

# Pretty printed Python object for easier reading.
pprint.pprint(validation_report)

router.close()
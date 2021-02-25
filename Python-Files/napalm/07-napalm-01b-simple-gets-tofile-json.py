import napalm
import json

driver=napalm.get_network_driver("ios")
router = driver(hostname='10.99.99.11',
                username='sntuser',
                password='Ilovenetworks99',
                optional_args={'secret':'cisco'}
                )
router.open()

# This will give an alphabetically sorted list of the available methods on the router object.
methods = dir(router)
print(json.dumps(methods, sort_keys=True, indent=4))

facts = router.get_facts()
# facts is a dictionary so the following is not very readable
print(facts)
# We need to use the json module to add readability.
# We could throw facts straight in but we have used the getter instead.
facts_json = json.dumps(router.get_facts(), indent=4)
print(facts_json)
# writing to a file
output_file = open('07-napalm-01b-simple-gets-tofile-json.json','w')
output_file.write(facts_json)
output_file.close()

interfaces = router.get_interfaces()
print(json.dumps(interfaces, indent=4))

router.close()
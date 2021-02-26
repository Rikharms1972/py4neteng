from nornir import InitNornir
from nornir.core.inventory import Host
import json


my_nornir = InitNornir(config_file = "config.yaml")

# this displays the default schema for the inventory
# hosts and groups file. Defaults is same without repetition
# for individual devices.
print(json.dumps(Host.schema(), indent=4))

# my_nornir
# now has an inventory with dict-like attributes hosts and groups
print(my_nornir.inventory.hosts)
print(my_nornir.inventory.groups)
# you can access the like regular dictionaries
print(my_nornir.inventory.hosts.keys())
print(my_nornir.inventory.hosts['R1'])

# Showing inheritance hosts --> groups --> defaults
router1 = my_nornir.inventory.hosts['R1']
rtr_priority =router1['priority']
print("Router1 priority is: " + str(rtr_priority))

router2 = my_nornir.inventory.hosts['R2']
print("Router2 priority is: {}".format(router2['priority']))

router4 = my_nornir.inventory.hosts['R4']
print("Router4 priority is: {}".format(router4['priority']))

# filters can be based on key: value pairs from the inventory yaml files
inv_filtrd = my_nornir.filter(priority=1).inventory.hosts.keys()
# will show all the items with priority 1
print(inv_filtrd)

#  filter using multiple items
inv_filtrd = my_nornir.filter(priority=1, site='london').inventory.hosts.keys()
# will show all the items with priority 1
print(inv_filtrd)

# find group members
print(my_nornir.inventory.children_of_group('junos_rtrs'))

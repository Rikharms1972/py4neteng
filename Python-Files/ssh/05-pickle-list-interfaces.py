import pickle

int_list = [
             {'intf': 'FastEthernet0/0', 'ipaddr': '10.99.99.11', 'status': 'up', 'proto': 'up'},
             {'intf': 'FastEthernet1/0', 'ipaddr': 'unassigned', 'status': 'administratively down', 'proto': 'down'},
             {'intf': 'FastEthernet2/0', 'ipaddr': 'unassigned', 'status': 'administratively down', 'proto': 'down'},
             {'intf': 'FastEthernet3/0', 'ipaddr': 'unassigned', 'status': 'administratively down', 'proto': 'down'},
             {'intf': 'FastEthernet4/0', 'ipaddr': 'unassigned', 'status': 'administratively down', 'proto': 'down'},
             {'intf': 'FastEthernet5/0', 'ipaddr': 'unassigned', 'status': 'administratively down', 'proto': 'down'},
             {'intf': 'FastEthernet6/0', 'ipaddr': 'unassigned', 'status': 'administratively down', 'proto': 'down'}
             ]

int_list_short = [
                {'intf': 'FastEthernet0/0', 'ipaddr': '10.99.99.11', 'status': 'up', 'proto': 'up'},
                {'intf': 'FastEthernet1/0', 'ipaddr': '10.99.99.12', 'status': 'down', 'proto': 'down'},
                {'intf': 'FastEthernet2/0', 'ipaddr': 'unassigned', 'status': 'administratively down', 'proto': 'down'},
                ]

with open("picklelist-ints.pickle", "wb") as pickle_file:
    pickle.dump(int_list, pickle_file)

with open("picklelist-ints-short.pickle", "wb") as pickle_file:
    pickle.dump(int_list_short, pickle_file)
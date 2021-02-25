import netmiko

import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)

R1 = {
    'device_type': 'juniper',
    'host': '10.4.4.41',
    'username': 'sntuser',
    'password': 'Ilovenetworks99'
    }
device_connection = netmiko.ConnectHandler(**R1)
device_connection.enable()
response = device_connection.send_command('show version')
print(response)

router_config = ['set system host-name vSRX-4-1',
                'commit'
                ]
response = device_connection.send_config_set(router_config)
print(response)

# response = device_connection.send_config_from_file('./router-config.txt')
print(response)

import netmiko

import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)

R1 = {
    'device_type': 'cisco_ios',
    'host': '10.99.99.11',
    'username': 'sntuser',
    'password': 'Ilovenetworks99',
    'secret' : 'cisco'}
device_connection = netmiko.ConnectHandler(**R1)
device_connection.enable()
response = device_connection.send_command('show clock')
print(response)

router_config = ['interface loopback0',
                 'ip address 1.1.1.1 255.255.255.255']
response = device_connection.send_config_set(router_config)
print(response)

response = device_connection.send_config_from_file('./router-config.txt')
print(response)

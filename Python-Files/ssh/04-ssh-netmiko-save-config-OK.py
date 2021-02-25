import netmiko 

R1 = {
    'device_type': 'cisco_ios',
    'host': '10.99.99.11',
    'username': 'sntuser',
    'password': 'Ilovenetworks99',
    'secret' : 'cisco'}
device_connection = netmiko.ConnectHandler(**R1)
device_connection.enable()

# # this only saves the remote config to NVRAM
output = device_connection.save_config(cmd='write mem')
print(output)

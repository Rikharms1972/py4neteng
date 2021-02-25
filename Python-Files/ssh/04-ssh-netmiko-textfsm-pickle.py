import netmiko
import pickle

R1 = {
    'device_type': 'cisco_ios',
    'host': '10.99.99.11',
    'username': 'sntuser',
    'password': 'Ilovenetworks99',
    'secret' : 'cisco'}
device_connection = netmiko.ConnectHandler(**R1)
device_connection.enable()

#  Use the textfsm ntc-template from my venv
# ls ~/.virtualenvs/ssh/lib/python3.6/site-packages/ntc_templates/templates/
# show what is available.
# They conveniently return the output from the show command as a list which
# is easier to manipulat than text strings.
response = device_connection.send_command('show ip interface brief', use_textfsm=True)

print(response)

# Save the list by pickling it for future use, "wb" is write and binary
# so the file will not be viewable by a normal text editor.
with open("pickletest.pickle", "wb") as pickle_file:
    pickle.dump(response, pickle_file)

# unpickling
with open("pickletest.pickle", "rb") as pickle_file:
    interfaces = pickle.load(pickle_file)
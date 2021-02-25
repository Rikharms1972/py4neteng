import napalm
import json

driver=napalm.get_network_driver("ios")
router = driver(hostname='10.99.99.11',
                username='sntuser',
                password='Ilovenetworks99',
                optional_args={'secret':'cisco'}
                )
router.open()

cmds = ['show ip int brief', 'show version', 'show platform']
response = router.cli(cmds)
# response is a dictionary of command: output pairs
# where output is a string of the complete output from a command
# including new line \n characters.

# The following iterates through the dictionary and 
# for each key i (command) takes the value (response[i] which is the output)
# and splits it at the newline characters to form a list of lines.
for i in response.keys():
    response[i] = response[i].split('\n')
# response is now a dictionary of commands (keys) to output (values)
# where the output (values) are now lists of strings.

# This would iterate through and print it all out
# but the json method further below is more readable.
for key in response:
    print(key, '\n')
    output = response[key]
    for line in output:
        print(line, '\n')

print(json.dumps(response, indent=4))

router.close()
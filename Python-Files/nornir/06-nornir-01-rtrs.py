from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

# the config_file is optional and by default the InitNornir will
# look in the same context for the config.yaml file.
# If you didn't have one you would have to throw in
# the runner and inventory parameters from variable declarations here
# instead.
# Add dry_run=True to only simulate changes
my_nornir = InitNornir("config.yaml")

# the return type is a Result
result = my_nornir.run(netmiko_send_command, command_string="show clock")

# need the print_result method as the return type of the run above
# is a nornir Task Result so normal print wouldn't work.
print_result(result)

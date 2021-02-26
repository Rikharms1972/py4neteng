from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result


my_nornir = InitNornir()

result = my_nornir.run(
    task=netmiko_send_command,
    command_string="show arp"
)

print_result(result)
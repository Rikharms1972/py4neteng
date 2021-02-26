from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_config
from nornir_netmiko.tasks import netmiko_send_command
from nornir_netmiko.connections import Netmiko



def set_loopbacks(task: Task,):
    loopbacks = task.host.data['loopbacks']
    task.run(task=netmiko_send_config, config_commands = ["interface loopback 99"])
        
    # clock=task.run(task=netmiko_send_command, command_string="show clock")

    return Result(
        host=task.host,
        result=f"{task.host.name} loopbacks configured to - {loopbacks}"
    )






my_nornir = InitNornir(config_file="config.yaml")
results = my_nornir.run(task=set_loopbacks)
print_result(results)


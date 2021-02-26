from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_config
from nornir_netmiko.tasks import netmiko_send_command

# for the progress bars
from tqdm import tqdm


def set_loopbacks(task: Task,):
    loopbacks = task.host.data['loopbacks']
    for key in loopbacks:
        interface = 'interface loopback' + str(key)
        # ip_addr = 'ip address ' + loopbacks[key] + ' 255.255.255.255'
        ip_addr = f'ip address {loopbacks[key]} 255.255.255.255'
        config_cmds = [interface, ip_addr]
        task.run(task=netmiko_send_config, config_commands=config_cmds)





def actions_with_progress_bar(task, action_1_bar):
    """
    This task takes one paramter that is in fact a progress bar;
    action_1_bar. When we want to tell the bar 
    that we are done and should update
    the progress we can do so with bar_name.update()
    """
    result=task.run(
        name="Setting loopbacks.",
        task=set_loopbacks,
        )
    action_1_bar.update()
    tqdm.write(f"{task.host}: Action-1 done.")
    

my_nornir = InitNornir(config_file="config.yaml")


# we create the first bar named napalm_get_bar
with tqdm(
    total=len(my_nornir.inventory.hosts), desc="Action-1",
) as action_1_bar:
    # we call our grouped task passing both bars
    my_nornir.run(
        task=actions_with_progress_bar,
        action_1_bar=action_1_bar,
    )


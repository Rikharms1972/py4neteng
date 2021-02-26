from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result

# a task has task: Task as the first parameter
def hello_world(task: Task) -> Result:
    return Result(
        host=task.host,
        result=f"{task.host.name} says hello world!"
    )


def say(task: Task, text: str) -> Result:
    return Result(
        host=task.host,
        result=f"{task.host.name} says {text}"
    )

# the config_file is optional but you would have to throw in
# the runner and inventory parameters instead, add dry_run=True to simulate changes
my_nornir = InitNornir(config_file = "config.yaml")

result = my_nornir.run(task=hello_world)
print_result(result)

result = my_nornir.run(
    #  this name can be seen in the screen output
    name="Saying goodbye in a very friendly manner",
    # task to run
    task=say,
    # argument
    text="buhbye!"
)
print_result(result)
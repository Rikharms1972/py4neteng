# source: https://nornir.readthedocs.io/en/latest/tutorial/tasks.html
from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result

def say(task: Task, text: str) -> Result:
    return Result(
        host=task.host,
        result=f"{task.host.name} says {text}"
    )

def count(task: Task, number: int) -> Result:
    return Result(
        host=task.host,
        result=f"{[n for n in range(0, number)]}"
    )


def greet_and_count(task: Task, number: int) -> Result:
    task.run(
        name="Greeting is the polite thing to do",
        task=say,
        text="hi!",
    )

    task.run(
        name="Counting beans",
        task=count,
        number=number,
    )
    task.run(
        name="We should say bye too",
        task=say,
        text="bye!",
    )

    # let's inform if we counted even or odd times
    even_or_odds = "even" if number % 2 == 1 else "odd"
    return Result(
        host=task.host,
        result=f"{task.host} counted {even_or_odds} times!",
    )

my_nornir = InitNornir(config_file = "config.yaml")

# Returns a dict-like AggregateResult as mutliple hosts.
# Each entry is a list-like MultiResult
result = my_nornir.run(
    task=greet_and_count,
    number=5,
)
print_result(result)
print(type(result))

# to print he result for single host
print_result(result["R1"])
print(type(result["R1"]))

# to print he result for single method on host
print_result(result["R1"][3])
print(type(result["R1"][3]))
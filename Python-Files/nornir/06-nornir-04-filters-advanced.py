# source: https://nornir.readthedocs.io/en/latest/howto/advanced_filtering.html
from nornir import InitNornir
from nornir.core.filter import F

nr = InitNornir(config_file="./inventory/advanced_filtering/config.yaml")

print(nr.inventory.hosts)
print(nr.inventory.groups)

# All the following filters the dict-like inventory

# DUNDER/MAGIC METHOD has __ at the beginning and is notionally hidden
# and not generally called as an object method.
# __contains
birds = nr.filter(F(groups__contains="bird"))
print(birds.inventory.hosts.keys())
print(birds.inventory.hosts.values())


# invert by prepending ~
not_birds = nr.filter(~F(groups__contains="bird"))
print(not_birds.inventory.hosts.keys())

# OR
domestic_or_bird = nr.filter(F(groups__contains="bird") | F(domestic=True))
print(domestic_or_bird.inventory.hosts.keys())

# AND
domestic_mammals = nr.filter(F(groups__contains="mammal") & F(domestic=True))
print(domestic_mammals.inventory.hosts.keys())

# combination
flying_not_carnivore = nr.filter(F(fly=True) & ~F(diet="carnivore"))
print(flying_not_carnivore.inventory.hosts.keys())

# lifespan is nested under additional_data and can be accessed using a __ ,
# additional_data__lifespan . We can then access builtin magic methods
# additional_data__lifespan__ge=15
long_lived = nr.filter(F(additional_data__lifespan__ge=15))
print(long_lived.inventory.hosts.keys())

# must have ALL elements listed
marine_and_invertebrates = nr.filter(F(groups__all=["marine", "invertebrate"]))
print(marine_and_invertebrates.inventory.hosts.keys())

# must have ANY of the elements listed
bird_or_invertebrates = nr.filter(F(groups__any=["bird", "invertebrate"]))
print(bird_or_invertebrates.inventory.hosts.keys())
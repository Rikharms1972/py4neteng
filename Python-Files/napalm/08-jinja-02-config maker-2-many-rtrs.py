import jinja2
import yaml
import os

# finds the path to this file
here = os.path.abspath(__file__)
# finds the directory path not including the file
root = os.path.dirname(here)

# Creates the sting of the path to the jinja templates directory
# by joining two paths.
path_to_templates = os.path.join(root, 'jinja-templates')
# ditto for the configuration data files
path_to_config_data = os.path.join(root, 'jinja-data')

# We need the jinja environment as our core, and we create it with a
# loader which is a path to the templates directory.
my_j2_environment = jinja2.Environment(loader = jinja2.FileSystemLoader(path_to_templates), trim_blocks=True, lstrip_blocks=True)

# loads a specific template
my_template = my_j2_environment.get_template('j2-tmplt-lpbks.j2')

# Opens then loads the yaml configuration data file
my_yaml_cfg_file = open('{}/j2-data-lpbks.yml'.format(path_to_config_data))
my_config_data = yaml.load(my_yaml_cfg_file, Loader=yaml.FullLoader)
# my_config_data is a dictionary whose keys are the router names R1, R2, R3.
# The keys are the top level of the yaml file.

# We can now iterate through that dictionary for each key (host)
for host in my_config_data:
    # Create the file path to the new config file for that host.
    config_filename = os.path.join(root, 'j2-config-files', f'{host}.cfg')
    # Open that new config file with write access (overwrites file)
    with open(config_filename, 'w') as new_config_file:
        # Merge/render the host branch of the yaml file with the template.
        new_config_file.write(my_template.render(my_config_data[host]))


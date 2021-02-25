from jnpr.junos import Device
from jnpr.junos.utils.config import Config

logon_creds ={'host': '10.4.4.41', 'user': 'sntuser', 'password': 'Ilovenetworks99'}

print ("\nConnecting to Juniper...\n")
junos_device = Device(**logon_creds)
junos_device.open()
junos_device.timeout = 300

# Create a configurator for the device
cfg = Config(junos_device)

print ("Setting hostname using set notation...")
new_hostname = input('Enter the new hostname: ')
cfg.load(f"set system host-name {new_hostname}", format="set", merge=True)

print ("Current config differences: ")
config_difference = cfg.diff()
if not config_difference:
    print('No configuration changes to bemade.')
else:
    print(config_difference)
    confirm_commit = input('Confirm commit for these changes. (y/n): ')
    if confirm_commit is 'y':
        print ("Performing commit...")
        cfg.commit()
        confirm_rollback = input('Would you like to rollback these changes? (y/n): ' )
        if confirm_rollback is 'y':
            print ("Performing rollback...")
            # rb_id is 0 most recent commit.
            # rb_id is 1 commit before that... 
            cfg.rollback(rb_id=1)
            cfg.commit()


from ncclient import manager

with manager.connect(host="10.4.4.41",
                    port=830, 
		            username="sntuser", 
                    password="Ilovenetworks99",
		            device_params={'name':'junos'},
		            hostkey_verify=False) as nc_conection:
                    
    config_running = nc_conection.get_config(source='running').data_xml
    # config_running is an xml string.
    with open("09-ncclient-04-junos-get-config-%s.xml" % host, 'w') as output_file:
        output_file.write(config_running)
import getpass

# function to connect using ssh and execute single command
def ssh_run_cmd(hostname, port, username, password, command):
    import paramiko

    ssh_connection_1 = paramiko.client.SSHClient()
    # the policy is a predefined subclass of paramiko.client and says what to do when presented with unknown certs from other end.
    ssh_connection_1.set_missing_host_key_policy(paramiko.client.AutoAddPolicy)

    ssh_connection_1.connect(hostname, port=port, username=username, password=password)

    stdin,stdout,stderr=ssh_connection_1.exec_command(command)

    for oneline in stdout.readlines():
        print(oneline)

    # file objects should be to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    ssh_connection_1.close()

if __name__ == '__main__':
    run_command = True
    run_again = False
    
    while run_command:
        if not(run_again):
            hostname = input("Enter the target hostname: ")
            port = input("Enter the target port: ")
            if (port == ""):
                port = 22
                print('default port 22 will be used')
            username = input("Enter username: ")
            password = getpass.getpass(prompt="Enter password: ")

        command = input("Enter command: ")
        ssh_run_cmd(hostname, port, username, password, command)
        run_again = input("To run another command enter 'y': ") == "y"
        if not(run_again):
            run_command=False
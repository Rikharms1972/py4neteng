import paramiko
import time

ssh_connection_1 = paramiko.client.SSHClient()
HOST="10.99.99.11"

# the policy is a predefined subclass of paramiko.client and says what to do when presented with unknown cert. from other end.
ssh_connection_1.set_missing_host_key_policy(paramiko.client.AutoAddPolicy)

ssh_connection_1.connect(HOST, username="sntuser", password="Ilovenetworks99")

# open an interactive shell session with remote host (of type paramiko.channel.Channel)
interactive_shell = ssh_connection_1.invoke_shell()

# send the command to execute
interactive_shell.send("show clock\n")

# gives chance for the output of the command to get back
time.sleep(0.1)

response = interactive_shell.recv(65535)
print(response.decode('utf8'))

# use a file for the commands to send and one for the response
outfile = open("./fileout.txt", "a")
cmd_file = open("./file1.txt")
for oneline in cmd_file:
    interactive_shell.send(oneline)
    time.sleep(0.1)
    response = interactive_shell.recv(65535)
    print(response.decode('utf8'))
    outfile.write(response.decode('utf8'))

ssh_connection_1.close()
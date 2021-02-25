import os
# run single command
os.system("ls -l")

import subprocess
# call single command
subprocess.call("ls")

# with arguments
subprocess.call(['ls', '-l'])
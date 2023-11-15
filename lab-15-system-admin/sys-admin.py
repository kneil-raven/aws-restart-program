# exercise 1
# import os

# os.system("ls")

# exercise 2
import subprocess

# # subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)
# subprocess.run(["ls"])

# exercise 3 
# subprocess.run(["ls","-l"])

# exercise 4
# use subprocess.run with 3 arguments
# subprocess.run(["ls","-l","README.md"])

# exercise 5
# retrieve system information
# command="uname"
# commandArgument="-a"
# print(f'Gathering system information with command: {command} {commandArgument}')
# subprocess.run([command,commandArgument])

# exercise 6
# retrieving information about disk space
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
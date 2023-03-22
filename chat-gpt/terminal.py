import subprocess

# Run a terminal command
subprocess.run(['ls', '-la'])

# Run a terminal command and capture the output
result = subprocess.run(['echo', 'Hello, world!'], stdout=subprocess.PIPE)
output = result.stdout.decode('utf-8')
print(output)

'''
In this example, the subprocess.run() function is used to run two different 
terminal commands. The first command runs the ls -la command to list the files 
in the current directory. The second command runs the echo command to print the 
message "Hello, world!" to the console. The output of the second command is 
captured using the stdout=subprocess.PIPE argument and then decoded from bytes 
to a string using the decode() method.

You can modify this script to run any terminal command you need. Just replace 
ls -la or echo 'Hello, world!' with the command you want to run, and pass the 
command as a list of strings to subprocess.run(). You can also add additional 
arguments to subprocess.run() to control things like the working directory, 
environment variables, and more.
'''
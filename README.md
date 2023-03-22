# py-auto

## Subprocess

```python

# The below will only run with shell=True set
# otherwise you need to separate the commands
subprocess.run('ls -la', shell=True)

# capture_output=True will not print anything out to 
# the terminal if it is set. You'll have to set it to a varible 
subprocess.run('ls', capture_output=True)

# stdout=subprocess.PIPE is similar to capture_output=True
# with 1 difference being it also captures stderr


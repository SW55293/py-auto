
import subprocess

p = subprocess.run(['ls', '-la'])

print(p.args)

print(p.returncode)

print(p.stdout)

#capturing output to stdout instead of printing it to the terminal
x = subprocess.run('ls', capture_output=True)
print(x.stdout.decode())

#open a file to store the output or logs into
with open('output.txt', 'w') as f:
    x2 = subprocess.run(['ls','-la'], stdout=f, text=True)

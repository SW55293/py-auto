
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

print(x2.stderr)
#ask if stderr is 0(meaning no errors) to run a block of code
if x2.returncode != 0:
    print('our code had no errors')

#redirect stderr to a subprocess if you want to ignore errors
x3 = subprocess.run('x', stderr=subprocess.DEVNULL)
print(x3.stderr)

#output of one command going to imput of another
capture = subprocess.run(['cat', 'output.txt'], capture_output=True, text=True)
print(capture.stdout)
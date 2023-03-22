import subprocess


capture = subprocess.run(['cat', 'out.txt'], capture_output=True, text=True)
print(capture.stdout)

# -n gives us the line number
#the third variavle (file) is just the word we want to
#search for in the file
greping = subprocess.run(['grep', '-n', 'file'],capture_output=True, text=True, input=capture.stdout)
print(greping.stdout)
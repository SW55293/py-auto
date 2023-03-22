#this script opens that file and prints out the 
#contents of it

# r stands for read
f = open('/etc/passwd', 'r')

for line in f.readlines():
    print(line)

f.close()


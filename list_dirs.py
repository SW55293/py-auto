import os

path = "/Users/steph/projects/automate-everything/py-scripting"

for filename in os.listdir(path):
   # print(filename)
   #un-comment to just print files in that path
  
  #this prints out the whole path of each file name
   pathname = os.path.join(path, filename)
   if os.path.isfile(pathname):
       #print(pathname) un-commnet to only print paths
       
       #this here reads all the files in the path
       f = open(pathname, 'r')
       for line in f.readlines():
           print(line)
           #split the lines at every space and place in single quotes
           split_line = line.split(' ')
           print(split_line)
       f.close()



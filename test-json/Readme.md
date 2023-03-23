### you can delete a range of lines using the following with sed

```bash
sed -i "" '1,3d' file.json 
```

### to try this on stdout and use jq to see it nicer try

```bash 
#1 >> da name@blah.com > file.json 
#2 >> sed -i "" '1,3d' file.json | jq '.' file.json

#the line range will need to be modified to remove the top portion
#that always prints out

```

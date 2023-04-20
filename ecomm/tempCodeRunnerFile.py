from urllib.request import urlopen

file=open("C:\\Users\\abhin\\Desktop\\code\\2.cpp")
prog=file.readlines()
print(prog[1])
cid=prog[1].split(' ')
print(cid)
url = "http:"
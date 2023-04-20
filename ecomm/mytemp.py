from urllib.request import urlopen

file=open("C:\\Users\\abhin\\Desktop\\code\\2.cpp")
prog=file.readlines()
print(prog[1])
cid=prog[1].split(' ')
cid[1]=cid[1][0:1]
print(cid)
url = "https://codeforces.com/problemset/problem/"+cid[0]+"/"+cid[1]+"/"
print(url)
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
test_index = html.find('<div class="sample-test">')
print(test_index)


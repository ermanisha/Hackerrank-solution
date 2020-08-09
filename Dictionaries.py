#DICTINARY PRACTICE PROBLEM USED TO FIND THE COUNT OF WORD IN TXT FILE AND RETURNS THE MAXIMUM COUNT
fh=input("enter the file")
fhand=open(fh)
di=dict()
for line in fhand:
    line.strip()
    wd=line.split()
    for word in wd:
        di[word]=di.get(word,0)+1
       
large=-1
for k,v in di.items():
    print(k,v)
    if v>large:
        large=v
print(large)
    
 # socket programming
import socket
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org",80))
cmd='GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)


while True:
    data=mysock.recv(512)
    if len(data) <1:
        break
    print(data.decode(),end=" ")
mysock.close()

#dictionary assignment USED TO READ A FILE GET THE COUNT OF THE PERSON WHO HAS SEND THE MAXIMUM NUMBER OF EMAILS.
name = input("Enter file:")
if len(name) < 1 : name = "sample.txt"
handle = open(name)
di=dict()
for line in handle:
    line.strip
    if line.startswith('From '):
        wd=line.split()
        di[wd[1]]=di.get(wd[1],0)+1
        print(di[wd[1]])

print(di)
large=-1 
word=None
for k,v in di.items():
    if v>large:
        large=v
        word=k
print(word,large)
        
        
        

    


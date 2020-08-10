file=input("enter the file name")
fhand=open(file)
di=dict()
for line in fhand:
	line.strip()
	wd=line.split()
	for w in wd:
		di[w]=di.get(w,0)+1
print(sorted(di.items())

#print(sorted([(v,k) for k,v in di.items()],reverse=True))
#lst=list()
#for k,v in di.items():
#	lst.append((v,k))
#lst=sorted(lst,reverse=True)
#for k,v in lst[:10]:
#	print(k,v)

      
      ***** PY4E ASSIGNMENT ***********
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
di=dict()
for line in handle:
    line.strip()
    if line.startswith('From '):
        wd=line.split()
        wd=wd[5].split(':')
        di[wd[0]]=di.get(wd[0],0)+1

lst=list()        
for k,v in di.items():
    lst.append((k,v))
    lst.sort()
for k,v in lst:
    print(k,v)
    
                
            
        
            
        
            
    

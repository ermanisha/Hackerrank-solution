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

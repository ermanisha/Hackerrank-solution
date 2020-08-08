import PyPDF2
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
    

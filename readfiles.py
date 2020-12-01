fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    words=line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)


    
a{
    display:block;
    font-weight:bold;
    color:#ffffff;
    background-color: #0006CC;
    width:200px;
    text-align:center;
    padding:4px;
    text-decoration:none;
    margin:0 auto;
    margin-top:10px;
}

a:hover{
    background: #B3B3B3;
    color:#0006CC;
}

a:focus{
    background:#B3B3B3;
    color:#0006CC;
}

a:active{
    border:3px solid #000000;
}

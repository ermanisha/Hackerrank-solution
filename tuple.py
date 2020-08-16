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
   
      
      
*******************************
      """var1=5
def some_func():
	var2=6
	print(var1,var2)
	def some_inner_func():
		var3=7
		print(var1,var2,var3)
	some_inner_func()
print(var1)
some_func()
"""
count=5
def some_method():
	global count
	count=count+1
	print(count)
some_method()
#******************************************
class Difference:
    def __init__(self, a):
        self.__elements = a
    
    def computeDifference(self):
            self.maximumDifference = abs(max(self.__elements) - min(self.__elements)) 



	

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
      
      
*******************************************
# 2D array input technique 1
 r=int(input("enter the number of rows "))
c=int(input("entre the number of columns"))
qui=[]
for i in range(3):
    qui.append(list(map(int,input().rstrip().split())))

print(qui)
      
# 2D array input technique 2
      R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  
# Initialize matrix 
matrix = [] 
print("Enter the entries rowwise:") 
  
# For user input 
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries 
         a.append(int(input())) 
    matrix.append(a) 
  
# For printing the matrix 
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print() 
      
      
      
    
            
        
            
        
            
    

class node:
    def __init__(self,data):
        self.data=data
        self.next=None;
class Linkedlist:
    def __init__(self):
        self.start=None;
    def insertLast(self,value):
        newNode=node(value)
        if self.start==None:
            self.start=newNode
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
    def deleteFirst(self):
        if self.start==None:
            print("list is empty ")
        else:
            temp=self.start
            self.start=self.start.next
    def viewList(self):
        if self.start==None:
            print("list is empty")
        else:
            temp=self.start
            while temp!=None:
                print(temp.data,end=" ")
                temp=temp.next

mylist=Linkedlist()
mylist.insertLast(30)
mylist.insertLast(40)
mylist.insertLast(50)
mylist.insertLast(60)
mylist.viewList()
print()
mylist.deleteFirst()
mylist.viewList()
        
                

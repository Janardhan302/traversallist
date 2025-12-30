class Node:
    def __init__(self,val):
        self.val=val 
        self.next=None
def iterate(head):
    temp=head
    while temp!=None:
        print(temp.val,end=" ")
        temp=temp.next
        
head=Node(1)
head.next=Node(3)
head.next.next=Node(5)
head.next.next.next=Node(7)
head.next.next.next.next=Node(9)
iterate(head)
class Node:
   def __init__(self,coeff,p):
       self.coeff=coeff
       self.p=p
       self.next=None
class Polynomial:
    def __init__(self):
        self.head=None
    def append(self,coeff,p):
        new_node=Node(coeff,p)
        if self.head is None:
             self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
                temp.next=new_node
    def printPolynomial(self):
        temp=self.head
        result=[]
        while temp:
            result.append(f"{temp.coeff}x^{temp.p}")
            temp=temp.next
        print(" + ".join(result))
    def addPolynomial(self,P1,P2):
        a=P1
        b=P2
        newHead=Node(0,0)
        c=newHead
        while a is not None or b is not None:
            if a is None:
                c.next=b
                break
            elif b is None:
                c.next=a
                break
            elif a.p == b.p:
                c.next=Node(a.coeff + b.coeff, a.p)
                a=a.next
                b=b.next
            elif a.p > b.p:
                c.next=Node(a.coeff , a.p)
                a=a.next
            else:
                c.next=Node(b.coeff , b.p)
                b=b.next
            c=c.next
        return newHead.next

poly1=Polynomial()
poly1.append(5,3)
poly1.append(4,2)
poly1.append(2,0)
poly2=Polynomial()
poly2.append(5,1)
poly2.append(5,0)
print("first Polynormial:")
poly1.printPolynomial()
print("second Polynomial:")
poly2.printPolynomial()
result=Polynomial()
result.head=result.addPolynomial(poly1.head , poly2.head)
print("resultant polynomial:")
result.printPolynomial()
        
        
            

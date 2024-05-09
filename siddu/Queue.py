class Queue: 
 def __init__(self): 
 self.items = [] 
 def enqueue(self,item): 
 self.items.append(item) 
 def dequeue(self): 
 if self.isEmpty(): 
 print("Queue is Empty cannot delete") 
 else: 
 item=self.items.pop(0) 
 print("Deleted Item is:",item) 
 def display(self): 
 if self.isEmpty(): 
 print("Queue is Empty") 
 else: 
 print(self.items) 
 def length(self): 
 return len(self.items) 
 def isEmpty(self): 
 return len(self.items) == 0 
q = Queue() 
while True: 
 print("1:Enqueue 2:Dequeue 3:Display 4:Length 5:Exit") 
 choice = int(input("Enter your choice:")) 
 if choice==1: 
 item=input("Enter the element:") 
 q.enqueue(item) 
 elif choice==2: 
 q.dequeue() 
 elif choice==3: 
 q.display() 
 elif choice==4: 
 n = q.length()
 print("Length of the queue is ",n) 
 elif choice==5: 
 break 
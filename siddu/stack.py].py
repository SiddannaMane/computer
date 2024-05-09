class Stack: 
 def __init__(self): 
 self.items = []
 def isEmpty(self):
     return len(self.items) == 0
    def push(self,item):
        self.items.append(item)
        def pop(self): 
 if self.isEmpty(): 
 print("Stack is Empty") 
 else: 
 item = self.items[-1] 
 del(self.items[-1]) 
 print("The popped element is:",item) 
 def display(self): 
 if self.isEmpty(): 
 print("Stack is Empty") 
 else: 
 for i in reversed(self.items): 
 print(i) 
 def peek(self): 
 if self.isEmpty(): 
 print("Stack is Empty") 
 else: 
 print("Top item is ", self.items[-1]) 
s = Stack() 
while(True): 
 print("1:push 2:pop 3:display 4:peek 5:exit") 
 choice = int(input("Enter your choice:")) 
 if choice == 1: 
 item = input("Enter the item to push:") 
 s.push(item) 
 elif choice == 2: 
 s.pop() 
 elif choice == 3: 
 s.display() 
 elif choice == 4: 
 s.peek() 
 else: 
 break
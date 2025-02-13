# Stack using array implementation 

class Stack:
    def __init__(self,size):
        self.size = size
        self.stack = [None]*size
        self.top = -1
    
    def push(self,val):
        if self.top == self.size -1:
            print("Overflow")
            return
        else:
            self.top+=1
            self.stack[self.top] = val
            return
    
    def pop(self):
        if self.top == -1:
            print("stack is empty")
            return
        else:
            print(self.stack[self.top])
            self.stack[self.top] = None
            self.top-=1
            return
        
    def traverse(self):
        for i in range(self.top+1):
            print(self.stack[i], end =' ')
    

s = Stack(3)
s.push(1)
s.push(1)
s.push(3)
# # s.push(3)
# print(s.stack)

s.traverse()
s.pop()
s.traverse()
s.pop()
s.traverse()
# s.pop()
s.traverse()
# # s.pop()
# print(s.stack)


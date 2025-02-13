class Node:
    def __init__(self,data):
        self.data = data
        self.nextAddress = None

class Stack:
    def __init__(self):
        self.top = None
        self.numNodes = 0

    #insert to the top of stack or push
    def push(self,value):
        newNode = Node(value)

        newNode.nextAddress = self.top
        self.top = newNode

        self.numNodes +=1

    # to remove the top element of the stack

    def pop(self):

        if self.top == None:
            return "Stack is Empty"
        
        item = self.top
        self.top = self.top.nextAddress
        self.numNodes -= 1
        return item.data
    
    # to peek the top element
    def peek(self):
        return self.top.data
    
    # to check if the stack is empty
    def isEmpty(self):
        if self.top == None:
            return True
        return False
    
    # to return the size of the stack

    def __len__(self):
        return self.numNodes
    

    # to show all the elements of the stack
    def __str__(self):
        if self.top == None:
            return "Stack is Empty"
        
        current = self.top
        while current !=None:
            print(current.data, end = " --> ")
            current = current.nextAddress 

        print("None")
        return ""
    

s = Stack()

print(s.isEmpty())
print(len(s))
print(s)

s.push(5)
s.push(4)
s.push(3)
s.push(2)
s.push(1)

print(s)

print(s.peek())
print(len(s))

print(s.pop())

print(s)

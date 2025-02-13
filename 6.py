class Node:
    def __init__(self,data):
        self.data = data
        self.nextAddress = None


class Stack:
    def __init__(self):
        self.top = None
        self.numNodes = 0
    
    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
    
    def push(self,value):
        node = Node(value)
        if self.top == None:
            self.top = node

        else:
            node.nextAddress = self.top
            self.top = node
        self.numNodes += 1

    def traverse(self):
        current = self.top
        while current!= None:
            print(current.data,end= ' -> ')
            current= current.nextAddress
        print(None)

    def size(self):
        return self.numNodes
    
    # returns the top item
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.top.data
        
    def pop(self):
        if self.isEmpty():
            return None
        
        temp = self.top
        self.top = self.top.nextAddress
        self.numNodes -= 1
        return temp.data
    
    # 2. text editor
def text_editor(str, operation="uur"):
    undo = Stack()
    redo = Stack()
    for i in str:
        undo.push(i)
    operation = operation.lower()
    for i in operation:
        if i == 'u':
            x = undo.pop()
            if x!=None:
                redo.push(x)
            

        elif i == 'r':
            x = redo.pop()
            if x!=None:
                undo.push(x)
    
    res=""
    current = undo.top
    while current!= None:
        res = undo.pop() + res
        current  = current.nextAddress
    
    return res

# Celebrity problem
def find_celebrity(l):
    # putting number of each row in stack
    s = Stack()
    for i in range(len(l)):
        s.push(i)

    while s.size()>=2:
        i = s.pop()
        j = s.pop()

        if l[i][j] == 0: #then i is celebrity
            s.push(i)
        else:# j is celebrity
            s.push(j)
        # s.traverse()
    
    for i in range(len(l)):
        if i != s.top.data:
            if l[s.top.data][i] == 1 or l[i][s.top.data] == 0:
                print("No Celebrity")
                return
    print(s.top.data)  
    



# s = Stack()

# 1. Reversing a stack
# str = "World"

# for i in str:
#     s.push(i)

# popItem = 1
# while popItem:
#     popItem = s.pop()
#     if popItem!= None:
#         print(popItem,end=" ")
    

# edit = text_editor("hello","uuuurrrrrrrr");
# print(edit)

l= [[0,0,1,1],
    [0,0,1,0],
    [0,0,0,0],
    [0,0,1,0]]

find_celebrity(l)
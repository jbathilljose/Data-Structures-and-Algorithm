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


s = Stack()

print(s.isEmpty())

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

s.traverse()

# print(s.size())

# print(s.peek())
print(s.pop())
s.traverse()

print(s.peek())
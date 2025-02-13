# Queues using linked list

# take two pointer front and rear

class Node:
    def __init__(self,data):
        self.data = data
        self.nextAddress = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.numNodes = 0
    
    # insertion or enqueue
    def enqueue(self,data):
        newNode = Node(data)

        if self.front == None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.nextAddress = newNode
            self.rear = newNode
        
        self.numNodes += 1
    
    #deletion or dequeue
    def dequeue(self):
        if self.front!=None and self.front !=self.rear:
            self.front = self.front.nextAddress
        else:
            self.front= None
            self.rear = None
            print("Empty Queue")
        
        self.numNodes -= 1

    # traverse or print
    def __str__(self):
        result = ''
        current = self.front
        while current!=None:
            result += str(current.data) + ' -> '
            current = current.nextAddress
        
        return result[:-4]
    
    #is Empty
    def isEmpty(self):
        if self.numNodes == 0:
            return True
        else:
            return False
        
    #size
    def size(self):
        return self.numNodes
    
    #peak at front
    def frontPeek(self):
        if self.front != None:
            return self.front.data
        else:
            return None
    
    #peak at rear
    def rearPeek(self):
        if self.rear != None:
            return self.rear.data
        else:
            return None

q = Queue()
# q.enqueue(1)
# print(q)
# q.enqueue(2)
# print(q)
# q.enqueue(3)
# print(q)
# q.dequeue()
# print(q)
# q.dequeue()
# print(q)
# q.dequeue()
# print(q) 

print(q.isEmpty())
print(q.size())
print(q.frontPeek())
print(q.rearPeek())  
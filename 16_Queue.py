class Nodes:
    def __init__(self,data):
        self.data = data
        self.nextAddress = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.numNodes = 0

    # to insert in a queue from the rear
    def enqueue(self,data):
        newNode = Nodes(data)
        self.numNodes += 1

        if self.front == None:
            self.front = newNode
            self.rear = newNode
            return
        
        newNode.nextAddress = self.rear
        self.rear = newNode

    # to remove an element from the front of the queue
    def dequeue(self):
        if self.front == None:
            return "The Queue is Empty"
        elif self.numNodes == 1:
            self.front = None
            self.rear = None
        else:
            current = self.rear
            while current != None:
                if current.nextAddress.nextAddress == None:
                    current.nextAddress = None
                    self.front = current 
                
                current = current.nextAddress
        
        self.numNodes -= 1

    
    # to check id the queue is empty
    def isEmpty(self):
        if self.front == None:
            return True
        return False
    
    #to ge the length of Queue

    def  __len__(self):
        
        return self.numNodes
    
    # to peek front

    def peekFront(self):
        if self.front == None:
            return "The Queue is Empty"
        return self.front.data
    
        # to peek rear

    def peekRear(self):
        if self.front == None:
            return "The Queue is Empty"
        return self.rear.data
    
    #to display the entire Queue
    def __str__(self):
        if self.front == None:
            return "The Queue is Empty"
        
        current = self.rear
        while current!= None:
            print(current.data, end = ' --> ')
            current = current.nextAddress
        
        print("None")
        return ''
    



q = Queue()
q.enqueue(1)
print(q)
q.enqueue(2)
print(q)
q.enqueue(3)
print(q)
q.dequeue()
print(q)
# q.dequeue()
# print(q)
# q.dequeue()
# print(q) 

print(q.isEmpty())
print(len(q))
print(q.peekFront())
print(q.peekRear())  
class Nodes:
    def __init__(self,data):
        self.data = data
        self.nextAddress = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.numNodes = 0

    #insertion
    def insertHead(self,value):
        newNode = Nodes(value)

        if self.numNodes == 0:
            self.head = newNode
            
        else:
            newNode.nextAddress = self.head
            self.head = newNode
        
        self.numNodes += 1
        print("***Inserted from head***")
        return
    
    # from middle
    def insertMiddle(self,value,index):
        newNode = Nodes(value)

        if self.numNodes == 0:
            self.head = newNode
            self.numNodes +=1

        else:
            if index < 0 or index >= self.numNodes:
                print("Invalid index")
                return
            count = 0
            current = self.head
            while current != None:
                if count == index:
                    newNode.nextAddress = current.nextAddress
                    current.nextAddress = newNode
                    self.numNodes +=1
                    print("***Inserted from middle***")
                    return
                count += 1
                current = current.nextAddress

    #  from end
    def insertTail(self,value):
        newNode = Nodes(value)

        if self.numNodes == 0:
            self.head = newNode
            self.numNodes += 1
            return


        current = self.head
        while current!= None:
            if current.nextAddress == None:
                current.nextAddress = newNode
                self.numNodes += 1
                print("***Inserted from Tail***")
                return
            current = current.nextAddress


        return
    
    #length
    def __len__(self):
        return self.numNodes
    
    #print the entire linked list
    def __str__(self):
        current = self.head
        while current != None:
            print(current.data,end = " ")
            current = current.nextAddress

        return ''
    
    #search: node with a specific value
    def search(self,value):
        current = self.head
        index = 0
        while current!=None:
            if current.data == value:
                return index
            current = current.nextAddress
            index+=1
        
        return "item not Found"
    
    #clear: delete all nodes
    def clear(self):
        self.head = None
        return 
    
    #get the value
    def __getitem__(self,index):
        current = self.head
        if index < -1* self.numNodes or index >= self.numNodes:
            return "Index out of range"
        else:
            if index < 0:
                index = index + self.numNodes
            
            for i in range(index+1):
                if i == index:
                    return current.data
                current = current.nextAddress

    
    #deletion

    #delete head
    def deleteHead(self):
        if self.head == None:
            return "List is empty"
        self.head = self.head.nextAddress
        self.numNodes -= 1
        return "Head Deleted"
    
    #delete tail
    def deleteTail(self):
        if self.head == None:
            return "List is empty"
        
        if self.numNodes == 1:
            self.head = None

        
        current = self.head
        while current !=None:
            if current.nextAddress.nextAddress == None:
                current.nextAddress = None
                self.numNodes -= 1
            current = current.nextAddress
        
        self.numNodes -= 1
        return "Tail deleted"
    
    #remove an item
    def remove(self,value):
        if self.head == None:
            return "List is empty"
        else:
            if self.head.data == value:
                self.head = self.head.nextAddress
                self.numNodes -= 1
                return "Item removed"
            else:
                current = self.head
                while current!=None:
                    if current.nextAddress.data == value:
                        current.nextAddress = current.nextAddress.nextAddress
                        self.numNodes -= 1
                        return "Item removed"
                    current = current.nextAddress
                
                return "Itewm not found"
    




l = LinkedList()

l.insertTail(1)
l.insertTail(2)
l.insertTail(3)

l.insertMiddle(4,0)
l.insertHead(10)

# print(l.numNodes)

# print(len(l))
# print(l)
# print(l.search(7))
# l.clear()
# print(l)
# print(l[-2])

# print(l.deleteHead())
# print(l.deleteTail())
print(l.remove(3))
print(l)
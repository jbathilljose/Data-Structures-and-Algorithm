class Node:
    def __init__(self,data):
        self.data = data
        self.nextAddress = None
    


# a = Node(10);
# # print(a.data,a.nextAddress);
# # print(id(a)

# b = Node(1)
# c = Node(2)
# # a.nextAddress = id(b);
# # b.nextAddress = id(c);
# # print(a.nextAddress,b.nextAddress,c.nextAddress)

class LinkedList:
    def __init__(self):
        self.head = None
        self.numNodes = 0;
    
    # length of Linked list
    def __len__(self):
        return self.numNodes
    
    #insert
    #from head
    def insertHead(self,value):
        # create the new node 
        newNode = Node(value)

        #connection
        newNode.nextAddress = self.head

        #reassignment
        self.head = newNode

        #increase number of nodes
        self.numNodes += 1

    # insert from tail
    def append(self,value):
        # create the node
        newNode = Node(value)

        if self.head == None:
            self.head = newNode
            self.numNodes += 1
            return 

        # traverse the linked list to the tail
        current = self.head
        while True:
            if(current.nextAddress == None):
                current.nextAddress = newNode
                self.numNodes += 1
                break;
            

            current = current.nextAddress

    
    # insert at the middle
    def insert(self,value,item):

        # create the node
        newNode = Node(value)

        if self.head == None:
            self.head = newNode
            self.numNodes += 1
            return
        
        current = self.head
        for i in range(self.numNodes):
            if current.data == item:
                current.nextAddress, newNode.nextAddress = newNode , current.nextAddress
                self.numNodes += 1
                return
            current = current.nextAddress
        
        if i+1 == self.numNodes:
            print("Item not found")

    # traverse OR print
    def __str__(self):
        current = self.head
        result = ''
        while current !=None:
            result+= str(current.data) + ' -> '
            current = current.nextAddress
        
        return result[:-3]
    
    # CLEAR
    def clear(self):
        self.head = None
        self.numNodes = 0    
        return    
    
    # delete
    # delete head
    def delete_head(self):
        if self.head == None:
            print("empty linked list")
            return
        self.head = self.head.nextAddress
        self.numNodes-=1
        return
    
    # delete tail
    def delete_tail(self):
        if self.head == None:
            print("empthy Linked list")
            return
        if self.head.nextAddress == None:
            self.delete_head()
            return
        current = self.head
        while  current.nextAddress.nextAddress!= None:
            current = current.nextAddress
        
        # current is the scond last item
        current.nextAddress = None
        self.numNodes-=1

    # delete with Value 
    def remove(self,item):
        if self.head == None:
            print("empty linked list")
            return
        if(self.head.data == item):
            self.delete_head()
            return
        
        current = self.head
        while current.nextAddress.data != item:
            current = current.nextAddress
            if current.nextAddress == None and current.data!= item:
                print("item not found")
                return
        current.nextAddress = current.nextAddress.nextAddress
        self.numNodes-=1

    def search(self,item):
        current = self.head
        index = 0
        while current!=None:
            if current.data == item:
                print(item, " is found at index ",index)
                return 
            current = current.nextAddress
            index+=1
        
        print("item not found")
    
    def __getitem__(self,index):
        if index < 0:
            print("negative indexing not available")
            return
        elif index >= self.numNodes:
            print("index out of range")
            return
    
        current = self.head
        for i in range(index+1):
            if i == index:
                return current.data
            current = current.nextAddress
        

        



l = LinkedList()

l.insertHead(5)
l.insertHead(4)
l.insertHead(3)
l.insertHead(2)
l.insertHead(1)
# print(len(l));
# print(l);

l.append(6);

l.insert(100,5);

# l.clear()

print(l);
print(len(l))
# l.delete_head();
# l.delete_tail()

l.remove(2)
print(l);
print(len(l));

l.search(2);

print(l[-6]);






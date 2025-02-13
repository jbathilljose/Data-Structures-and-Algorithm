# Hashing using closed address : chaining

class Node: #a node having key,value and nextAddress
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.nextAddress = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.numNodes = 0;
    
    # length of Linked list
    def __len__(self):
        return self.numNodes
    

    # insert from tail
    def add(self,key,value):
        # create the node
        newNode = Node(key,value)

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



    # traverse OR print
    def __str__(self):
        current = self.head
        result = ''
        while current !=None:
            result+= str(current.key) + ' --> ' + str(current.value) + "   "
            current = current.nextAddress
        
        return result[:-3]
    
    # CLEAR
    def clear(self):
        self.head = None
        self.numNodes = 0    
        return    
    
    # delete

    
    
    # delete with Value 
    def remove(self,key):
        if self.head == None:
            print("empty linked list")
            return
        if(self.head.key == key):
            self.head = self.head.nextAddress
            return
        
        current = self.head
        while current.nextAddress.key != key:
            current = current.nextAddress
            if current.nextAddress == None and current.key!= key:
                print("item not found")
                return
        current.nextAddress = current.nextAddress.nextAddress
        self.numNodes-=1

    def search(self,key):
        current = self.head
        index = 0
        while current!=None:
            if current.key == key:
                # print(key, " is found at index ",index)
                return index
            current = current.nextAddress
            index+=1
        
        return -1
    
    # to return a specific node
    def get_node(self,index):
        current = self.head
        for i in range(index+1):
            if i == index:
                return current
            current = current.nextAddress
    
    
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


class Dictionary:
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        # create an array of linked list here
        self.buckets = self.make_array(self.capacity)# buckets is a terminology for the array of linked list( each element of the array is a linked list which is a bucket so an array in whole is called buckets)

    def make_array(self,capacity):
        l = []
        for i in range(capacity):
            l.append(LinkedList()) #making an array of linked  list or making buckets
        
        return l
    
    def __setitem__(self,key,value):
        return self.put(key,value)

    def put(self,key,value):
        bucket_index = self.hash_function(key)

        node_index = self.get_node_index(bucket_index,key)
        
        # insert case
        if node_index == -1:
            self.buckets[bucket_index].add(key,value)
            self.size+=1
            # print("inserted")
            loadFactor = self.size/self.capacity
            print("Load factor of the array is: ",loadFactor)

            if (self.size/self.capacity) >= 2:
                self.rehash()

        else: #update case 
            # current = self.buckets[bucket_index].head
            # for i in range(node_index+1):
            #     if(i == node_index):
            #         current.value = value
            #         return
            #     current = current.nextAdderess
            self.buckets[bucket_index].get_node(node_index).value = value
            print("updated")
        
    
    def rehash(self):
        # create a new array of linked list with double the capacity
        print("Incresing the size of the array to decrease load factor")
        oldBuckets = self.buckets
        self.capacity*=2
        self.size = 0
        self.buckets = self.make_array(self.capacity)

        # putting all the nodes from oldbuckets to the new Buckets
        for i in oldBuckets:
            current = i.head
            while current!= None:
                self.put(current.key,current.value)
                current = current.nextAddress

    def __getitem__(self,key):
        return self.get(key)

    def get(self,key):
        bucket_index = self.hash_function(key)

        node_index = self.get_node_index(bucket_index,key)

        if node_index == -1:
            print(key," is not present.")
            return
        else:
            node = self.buckets[bucket_index].get_node(node_index)
            print(node.key, " = ", node.value)
            return 
        
    def __str__(self):
        for i in self.buckets:
            current = i.head
            while current!=None:
                print(current.key, " = ", current.value)
                current = current.nextAddress
            
        return "****End of Dictionary****"
    
    
    def __delitem__(self,key):
        return self.delete(key)
    

    def delete(self,key):
        bucket_index = self.hash_function(key)
        self.buckets[bucket_index].remove(key)
        print(key, " is deleted");
        self.size-=1
        return
    
    def __len__(self):
        return self.size


    def get_node_index(self,bucket_index,key):
        node_index = self.buckets[bucket_index].search(key)

        return node_index


    def hash_function(self,key):
        return abs(hash(key))% self.capacity
    


d = Dictionary(3)

d.put("python",1)
d.put("java",2)
d.put("JS",3)
# print(d.buckets)
d.put("GO",4)
d.put("Excel",5)
d.put("MS",6)
d["React"] = 10


# l = LinkedList()
# l.add(1,2)
# l.add(3,5)
# l.add(4,6)

# print(l)

# print(l.get_node(1),l.get_node(1).key,l.get_node(1).value)

d.get("React")

d.put("HTML", 7)

print(d["python"])

# print(d.buckets)

# d.delete("JS")

del d["python"]
print(d)
print(len(d))

# Hashing

# linear probing : making a python dictionary using hashing

class Dictionary:
    def __init__(self,size):
        self.size = size
        self.slots = [None]*size #takes oin the keys of the dictionary
        self.data = [None]*size #takes in the values of the dictionary as in the same position as slots or keys

    
    def put(self,key,value):
        print('Y')
        
        # if len(self.slots) > self.size:
        #     self.size*=2
        #     self.slots+=[None]*2
        #     self.data+=[None]*2
        #     print(d.slots)
        #     print(d.data)
        hash_value = self.hash_function(key)



        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slots[hash_value] == key:#if value is updated
                self.data[hash_value] = value
            else:
                i=1
                while self.slots[hash_value] != None and self.slots[hash_value] != key:
                    hash_value = self.hash_function(key,i)
                    if self.slots[hash_value] == None:
                        self.slots[hash_value] = key
                        self.data[hash_value] = value
                        i+=1

                    elif self.slots[hash_value] == key:
                        self.data[hash_value]= value
                        break
        return
    
    def __setitem__(self,key,value):
        print('x')
        self.put(key,value)
    
    def get(self,key):
        start_position = self.hash_function(key)
        current_position = start_position
        i= 1;

        while self.slots[current_position]!=None:
            if  self.slots[current_position] == key:
                return self.data[current_position]
            
            current_position = self.hash_function(key,i)
            i+=1

            if current_position == start_position:
                return "Not found"
        
        return "not found"
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __str__(self):
        for i in range(len(self.slots)):
            if self.slots[i] != None:
                print(self.slots[i],":",self.data[i],end=' ')

        return ""        
            


    def hash_function(self,key,i=0):
        return (abs(hash(key))+i)%self.size #so that string can also be hashed
    
                    
        





d = Dictionary(3)
print(d.slots)
print(d.data)

# d.put('python',1)
# d.put('python',4)
# d.put('java',2)
# d.put('JS',3)


# print(d.slots)
# print(d.data)

d['python'] = 1
d['java'] = 3
d['js'] = 5

# d['python'] = 100


# print(d.slots)
# print(d.data)

# print(d.get('python'))
# print(d['java'])
# print(d['js'])
# print(d['php'])

print(d)
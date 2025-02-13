import ctypes

class MyList:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.array = self.__makeArray(self.size)
    
    def __makeArray(self,capacity):
        # makes a c type array(static and referential) with size capacity
        return (capacity*ctypes.py_object)();

    def __resize(self,newCapacity):
        # resizes the array to newCapacity
        b = self.__makeArray(newCapacity);
        self.size = newCapacity;
    
        #copy content from array to b
        for i in range(self.n):
            b[i] = self.array[i]

        # reassign B to array
        self.array = b;

    def __len__(self):
        return self.n;

    def append(self,item):
        # appends an element to the end of the list 
        if self.n == self.size:
            #resize
            self.__resize(self.size*2)
        
        #append
        self.array[self.n] = item;
        self.n += 1;

    #print
    def __str__(self):
        result = ''
        result+= '['
        for i in range(self.n):
            result+= str(self.array[i])+','
        result = result[:-1]
        result+= ']'
        return result
    
    #indexing i.e it is called when code like l[1] is called
    def __getitem__(self,index):
        if 0<=index <= self.n:
            return self.array[index];
        else:
            return "Index out of bounds"
    
    # pop
    def pop(self):
        # removes the last element from the list
        if self.n == 0:
            return "List is empty"
        else:
            item = self.array[self.n-1];
            self.n -=1;
            return item;
    #clear
    def clear(self):
        self.n = 0
        self.size = 1;

    #find
    def find(self,item):
        #finds the index of the first occurrence of the item in the list
        for i in range(self.n):
            if self.array[i] == item:
                return i 
        return "Not in list";

    #insert
    def insert(self,item,index):
        #inserts the item at the specified index
        if index < 0 or index > self.n:
            return "index out of bounds"
        if(self.n == self.size):
            self.__resize(self.size*2)
        
        for i in range(index,self.n+1):
            if i == self.n:
                self.array[i] = item
            x = self.array[i];
            self.array[i] = item
            item = x;
        self.n+=1

    #delete
    def __delitem__(self,index):
        #deletes the item at the specified index
        if index < 0 or index >= self.n:
            print("index out of bounds")
        else:
            for i in range(index,self.n):
                if i == self.n - 1:
                    break;
                self.array[i]= self.array[i+1]
            self.n-=1;

    #remove
    def remove(self,item):
        #removes the first occurrence of the item in the list
        x=self.find(item);
        if x == "Not in list":
            return "Not in list"
        else:
            self.__delitem__(x);
        





             



l = MyList();
print(type(l));
print(len(l))

l.append(1);
l.append(3);
l.append(4);
print(len(l));
# print(l.array[0]);
print(l);
print(l[2]);
print(l[359]);

# print(l.pop());
# print(l.pop());
# print(l.pop());

# l.clear();

print(l.find(1));

l.insert(0,0);
print(l);

# del(l[3])
l.remove(3);
print(l);

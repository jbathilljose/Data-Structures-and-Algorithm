# example to show list is a dynamic array
import sys
l = [];
print(sys.getsizeof(l));
m = [1,2,3,4,"hello","world"];
for i in m:
    l.append(i);
    print(sys.getsizeof(l));


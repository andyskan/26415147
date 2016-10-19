#!/usr/bin/python3

#this is a list, that looks like an array, just say that this is array
list = [ 'John', 1998 , 'Cena', 70.2,4020 ]
list2 = ['ganteng', 91]

print (list)          # print complete list
print (list[0])       # print element n
print (list[1:3])     # print element on a range 
print (list[2:])      # prints elements starting from n th element
print (list2 * 2)  # prints list n times
print (list + list2) # print two tuples

#this is tuple, like a list but cannot modify the value

tuple = ( 'John', 1998 , 'Cena', 70.2, 4020  )
tuple2 = ('ganteng',91)

print (tuple)           # prints complete tuple
print (tuple[0])        # prints element n
print (tuple[1:3])      # prints element on a range 
print (tuple[2:])       # prints elements starting from n-th  element
print (tuple2 * 2)   # prints tuple n times
print (tuple + tuple2) # print two tuples

list[0]='Meong'
print (list)


#tuple cannot be modified unlike list

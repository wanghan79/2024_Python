# #Test1:int is a stable type
# a=1
# print("Original 'int' variable 'a' address: "+str(id(a)))
# a=2
# print("Re-assigned 'int' variable 'a' address: "+str(id(a)))
# b=a
# print("Another 'int' variable 'b' shared 'a' address: "+str(id(b)))
# a=3
# print("'a' address: "+str(id(a)))
# print("'b' address: "+str(id(b)))

# #Test2:str is a stable type
# a="PY is great!"
# print(id(a))
# a="PY is so great!!"
# print(id(a))
# b=a
# print(id(a))
# print(id(b))

#a[2]="X"
#print(id(a))

#Test3:tuple is a stable type
# a=(1,2.0,'3',int)
# b=a
# print(id(a))
# a=(5,6,7)
# print(id(a))
# c=a+b
# print(id(c))
# c=c+a
# print(id(c))

# #c[3]=100

# a=[1,2,3]
# b=a
# print(id(a))
# a=[5,6,7]
# print(id(a))
# a[0]=10
# print(id(a))
# a.append(9)
# print(id(a))

# #Test4:set is a flexible type
# a={1,2,3}
# print(id(a))
# a.add(4)
# print(id(a))
# b=a
# print(id(a))
# print(id(b))

#Test5:dict is a flexible type
# a={1:"one",2:"teo",3:"three"}
# print(id(a)) #2072534747520
# a.update({4:"four"})
# print(id(a)) #2072534747520

# b=a #浅拷贝
# print(id(a)) #2072534747520
# print(id(b)) #2072534747520
# b.clear()
# print(a) #{}
# print(b) #{}

# b=a.copy() #中拷贝   #深拷贝deepcopy()
# print(id(a))
# print(id(b))
# b.clear()
# print(a) #{1: 'one', 2: 'teo', 3: 'three', 4: 'four'}
# print(b) #{}

#Test6:tuple,list,set,dict are dropbox of mixed data types
# a=(1,"str",[5,6,7])
# print(a)

# a=[1,"str",[5,6,7]]
# print(a)
# print(id(a))
# a.append({"aaa",000})
# print(a)
# print(id(a))

# strtmp="tmp string"
# a.append(strtmp)
# print(a)

# print(id(a))
# a[1]="another str"
# print(id(a))

# print(id(a))
# a[3].add("another str")
# print(id(a))
# print(a)

#Test7:copy() and deepcopy()
import copy
lista=[4,5]
listb=[1,2,3,lista]
lista.append(6)

listc=copy.copy(listb)
listd=copy.deepcopy(listb)
print(id(listb))
print(id(listc))
print(id(listd))

lista.append(7)
print(id(listb))
print(id(listc))
print(id(listd))


s=set([1,2,3])
t=set("hello")
print(s)
print(t)

a= s|t
print(a)
b=s&t
print(b)
print(a)
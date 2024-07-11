def list_find(lst,target):
    for index,x in enumerate(lst):
        print(index,x)
        if x==target:
            break
    else:
        index=-1
    return index

listA=[1,"2",("abc",1)]
print(enumerate(listA))
print(list(enumerate(listA)))
print(list(enumerate(listA,start=2)))
print(tuple(enumerate(listA,start=1)))

seq = ['one', 'two', 'three']
for temp in enumerate(seq):
    print(temp)


print(list_find(seq,999))
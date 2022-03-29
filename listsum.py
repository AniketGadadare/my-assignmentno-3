def summetion(list1):
    s=0
    for i in range(len(list1)):
        list1[i]=int(list1[i])
        s=list1[i]+s
    return s

list1=[8,2,3,0,7]
summ=summetion(list1)
print(summ)
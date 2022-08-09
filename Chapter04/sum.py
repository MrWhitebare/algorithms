def sum(list:list):
    if list==[]:
        return 0
    return list[0]+sum(list[1:])

def count(list:list):
    if list==[]:
        return 0
    return 1+count(list[1:])

sum=sum([1,2,3,4,5])
count=count([1,2,3,4,5])
print("sum:{0},count:{1}".format(sum,count))
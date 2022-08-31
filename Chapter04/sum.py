def sum(list:list):
    if list==[]:
        return 0
    return list[0]+sum(list[1:])

def count(list:list):
    if list==[]:
        return 0
    return 1+count(list[1:])

def max(list:list):
    if(len(list)==0):
        return None
    if(len(list)==1):
        return list[0]
    else:
        sub_max=max(list[1:])
        return list[0] if list[0]>sub_max else sub_max             

sum=sum([1,2,3,4,5])
count=count([1,2,3,4,5])
print("sum:{0},count:{1}".format(sum,count))
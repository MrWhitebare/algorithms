from array import array

def quickSort(array:list):
    if(len(array)<2):
        return array
    else:
        pivot=array[0]
        #小于基准值的区间
        less=[]
        #大于基准值的区间
        greater=[]
        for i in array[1:]:
            if(i<=pivot):
                less.append(i)
            else:
                greater.append(i)
        return quickSort(less)+[pivot]+quickSort(greater)        
array=[10,5,2,3]
print(quickSort(array))        
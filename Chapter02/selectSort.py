# 选择排序
def findSmallest(arr):
    """[查找最小元素]

    Args:
        arr ([list]): [数组]

    Returns:
        [int]: [index]
    """
    smallest=arr[0]
    smallestIndex=0
    for i in range(len(arr)):
        if(smallest>arr[i]):
            smallest=arr[i]
            smallestIndex=i
    return smallestIndex

def selectionSort(arr):
    """[选择排序]

    Args:
        arr ([list]): [待排序数组]

    Returns:
        [type]: [list]
    """
    newArray=[]
    while(len(arr)>0):
        smallestIndex=findSmallest(arr)
        newArray.append(arr.pop(smallestIndex))
    return newArray
my_array=[5, 3, 6, 2, 10]
print(selectionSort(my_array))
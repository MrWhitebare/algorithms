# 二分查找
from typing import List

def binarySearch(list:list[int],item:int):
    """[二分查找有序列表index]

    Args:
        list (list[int]): [有序列表]
        item (int): [目标值]

    Returns:
        [type]: [int|None]
    """
    low=0
    high=len(list)-1

    while(low<=high):
        mid=(low+high)//2
        guess=list[mid]
        if(guess==item):
            return mid
        if(guess>item):
            high=mid-1
        else:
            low=mid+1
    return None

my_list=[1,3,5,7,9]
print(binarySearch(my_list,3))
print(binarySearch(my_list,-1))
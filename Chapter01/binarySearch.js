/* 二分查找 */
/**
 * @description 二分查找
 * @param {Array} list 有序列表
 * @param {Number} desValue 目标值
 * @returns 
 */
function binarySearch(list,desValue){
    let low=0;
    let high=list.length-1;
    while(low<=high){
        let mid=Math.floor((low+high)/2);
        let guess=list[mid];
        if(guess===desValue) return mid;
        if(desValue>guess){
            low=mid+1;
        }else{
            high=mid-1;
        }
    }
    return undefined;
}

let my_list=[1,3,5,7,9];
console.log(binarySearch(my_list,7));
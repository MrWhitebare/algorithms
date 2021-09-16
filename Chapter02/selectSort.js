/* 选择排序 */
/**
 * @description 筛选最小值
 * @param {Array} arr 待筛选数组 
 * @returns {Number}
 */
function findSmallest(arr){
    smallest=arr[0];
    smallestIndex=0;
    for(let i=0;i<arr.length;i++){
        if(smallest>arr[i]){
            smallest=arr[i];
            smallestIndex=i;
        }
    }
    return smallestIndex;
}
/**
 * @description 选择排序
 * @param {Array} arr 
 * @returns {Array}
 */
function selectSort(arr){
    let newArray=[];
    while(arr.length>0){
        smallestIndex=findSmallest(arr);
        let smallestValue=arr.splice(smallestIndex,1)[0];
        newArray.push(smallestValue);
    }
    return newArray;
}
let my_array=[5, 3, 6, 2, 10];
console.log(selectSort(my_array));
const quickSort=array=>{
    if(array.length<2){
        return array;
    }

    let pivot=array[0],//基准值
        less=[],//小于基准值的区间
        greater=[];//大于基准值的区间
    for (const iterator of array.slice(1)) {
        if(pivot>=iterator)
            less.push(iterator)
        else
            greater.push(iterator)    
    }        
    return [...quickSort(less),pivot,...quickSort(greater)];
}

let array=[10,5,2,3];
console.log(quickSort(array));
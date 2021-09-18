const factorial=num=>{
    if(num<=0) return 1;
    else{
        return num*factorial(num-1);
    }
}

let num=factorial(7);
console.log(num);
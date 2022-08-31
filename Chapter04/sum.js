const sum=(args)=>{
    if(args.length===0){
        return 0;
    }
    return args[0]+sum(args.slice(1))
}
const count=(args)=>{
    if(args.length===0){
        return 0;
    }
    return 1+count(args.slice(1));
}

const max=(args)=>{
    if(args.length===0){
        return;
    }
    if(args.length===1)
        return args[0]
    else{
        let sub_max=max(args.slice(1));
        return args[0]>sub_max?args[0]:sub_max;
    }    
}

let ArraySum=sum([1,2,3,4,5]),
    ArrayCount=count([1,2,4,5,6]),
    maxValue=max([1,5,2,3,6]);
console.log(ArraySum,ArrayCount,maxValue);
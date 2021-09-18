/* 汉诺塔 */
const move=(x,y)=>{
    console.log(`${x}===>${y}`);
}

const hanoiTower=(n,a,b,c)=>{
    if(n==1){
        move(a,c);
    }else{
        hanoiTower(n-1,a,c,b);
        move(a,c);
        hanoiTower(n-1,b,a,c);
    }
}

hanoiTower(3,"A塔","B塔","C塔");
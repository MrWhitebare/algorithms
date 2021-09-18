# 汉诺塔
def move(x:str,y:str):
    print("{0}===>{1}".format(x,y))
def hanoiTower(n:int,a:str,b:str,c:str):
    if n==1:
        move(a,c)
    else:
        hanoiTower(n-1,a,c,b)
        move(a,c)
        hanoiTower(n-1,b,a,c)

hanoiTower(3,"A塔","B塔","C塔")
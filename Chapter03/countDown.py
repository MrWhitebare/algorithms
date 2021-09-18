#递归
def countDown(num):
    #基线条件————结束递归
    if(num<=0):
        return
    else:
        #递归条件，继续递归
        print(num)
        countDown(num-1)

countDown(9)
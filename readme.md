## 算法图解

### 1. 二分查找

二分查找是一种算法，其输入是一个有序的元素列表（必须有序的原因稍后解释）。如果要
查找的元素包含在列表中，二分查找返回其位置；否则返回null。  

```C#
class algorithms
    {
        /// <summary>
        /// 二分查找有序列表
        /// </summary>
        /// <param name="orderList">有序列表</param>
        /// <param name="desValue">目标值</param>
        /// <returns></returns>
        public static int BinarySearch(int[]orderList,int desValue)
        {
            int low = 0;
            int high = orderList.Length - 1;
            while (low<=high)
            {
                int mid = (low + high) / 2;
                int guess = orderList[mid];
                if (guess == desValue) return mid;
                if (guess < desValue)
                {
                    low = mid + 1;
                }
                else
                {
                    high = mid - 1;
                }
            }
            return -1;
        }
    }
```

> **运行时间**
>
> 简单查找逐个地检查数字，如果列表包含100个数字，最多需要猜100次。如果列表包含40亿个数字，最多需要猜40亿次。换言之，最多需要猜测的次数与列表长度相同，这被称为线性
> 时间（ linear time）。  
>
> ![image-20210916143911944](https://cdn.jsdelivr.net/gh/MrWhitebare/algorithms@1.0/IMG/binarySearch.png)

### 2. 大![O](http://latex.codecogs.com/svg.latex?O)表示法

大![O](http://latex.codecogs.com/svg.latex?O)表示法是一种特殊的表示法，指出了算法的速度有多快。

![大O表示法](https://cdn.jsdelivr.net/gh/MrWhitebare/algorithms@1.0/IMG/compare.png)

随着元素数量的增加，二分查找需要的额外时间并不多，而简单查找需要的额外时间却很多。因此，随着列表的增长，二分查找的速度比简单查找快得多。 Bob以为二分查找速度为简单查找的15倍，这不对：列表包含10亿个元素时，为3300万倍。  

大![O](http://latex.codecogs.com/svg.latex?O)表示法指出了算法有多快。例如，假设列表包含![O](http://latex.codecogs.com/svg.latex?n)个元素。简单查找需要检查每个元素，因此需要执行次![n](http://latex.codecogs.com/svg.latex?n)操作。使用大![O](http://latex.codecogs.com/svg.latex?O)表示法，这个运行时间为![O](http://latex.codecogs.com/svg.latex?O(n))。单位秒呢？没有——大表示法![O](http://latex.codecogs.com/svg.latex?O)指的并非以秒为单位的速度。 大表示法![O](http://latex.codecogs.com/svg.latex?O)让你能够比较操作数，它指出了算法运行时间的增速。  

为检查长度为![O](http://latex.codecogs.com/svg.latex?n)的列表，二分查找需要执行![O](http://latex.codecogs.com/svg.latex?log_2n)次操作。大![O](http://latex.codecogs.com/svg.latex?O)表示为![O](http://latex.codecogs.com/svg.latex?O(log_2n))

#### 2.1 一些常见的大![O](http://latex.codecogs.com/svg.latex?O)运行时间

下面按从快到慢的顺序列出了你经常会遇到的5种大O运行时间。  

- ![O](http://latex.codecogs.com/svg.latex?O(log_2n)) 对数时间，这样的算法包括二分查找；

- ![O](http://latex.codecogs.com/svg.latex?O(n))线性时间，这样的算法包括简单查找；

- ![O](http://latex.codecogs.com/svg.latex?O(n*log_2n))这样的算法包括快速排序；

- ![O](http://latex.codecogs.com/svg.latex?O^2) 这样的算法包括选择排序；

- ![O](http://latex.codecogs.com/svg.latex?O(n!)) 这样的算法包括旅行商问题的解决方案。

![算法运行时间](https://cdn.jsdelivr.net/gh/MrWhitebare/algorithms@1.0/IMG/time.png)

#### 2.2 旅行商问题

有一位旅行商需要前往5个城市。

![cities](https://cdn.jsdelivr.net/gh/MrWhitebare/algorithms@1.0/IMG/cities.png)

这位旅行商（姑且称之为Opus吧）要前往这5个城市，同时要确保旅程最短。为此，可考虑
前往这些城市的各种可能顺序。  

![](https://cdn.jsdelivr.net/gh/MrWhitebare/algorithms@1.0/IMG/order.png)

对于每种顺序，他都计算总旅程，再挑选出旅程最短的路线。 5个城市有120种不同的排列方式。因此，在涉及5个城市时，解决这个问题需要执行120次操作。涉及6个城市时，需要执行720次操作（有720种不同的排列方式）。涉及7个城市时，需要执行5040次操作！ 

![](https://cdn.jsdelivr.net/gh/MrWhitebare/algorithms@1.0/IMG/factorial.png)

### 3. 选择排序

#### 3.1 内存的工作原理

计算机就像是很多抽屉的集合体，每个抽屉都有地址。`fe0ffeeb`是一个内存单元的地址。    

![内存](https://cdn.jsdelivr.net/gh/MrWhitebare/algorithms@1.0/IMG/memory.png)

数组与链表操作的运行时间比较

|      | 数组                                           | 链表                                           |
| :--: | ---------------------------------------------- | ---------------------------------------------- |
| 读取 | ![O](http://latex.codecogs.com/svg.latex?O(1)) | ![O](http://latex.codecogs.com/svg.latex?O(n)) |
| 插入 | ![O](http://latex.codecogs.com/svg.latex?O(n)) | ![O](http://latex.codecogs.com/svg.latex?O(1)) |
| 删除 | ![O](http://latex.codecogs.com/svg.latex?O(n)) | ![O](http://latex.codecogs.com/svg.latex?O(1))                                     |

![4](http://latex.codecogs.com/svg.latex?\sum_{n=1}^\infty\frac{1}{n^2}=\frac{\pi^2}{6})

```C#
private static int FindSmallest(int[] iArray)
{
    int smallest = iArray[0];
    int smallestIndex = 0;
    for (int i = 0; i < iArray.Length; i++)
    {
        if (smallest > iArray[i])
        {
            smallest = iArray[i];
            smallestIndex = i;
        }
    }
    return smallestIndex;
}

private static int[] RemoveListItem(int[] iArray,int index)
{
    ArrayList arrayList = new ArrayList();
    for (int i = 0; i < iArray.Length; i++)
    {
        if (i != index)
        {
            arrayList.Add(Convert.ToInt32(iArray[i]));
        }
        else continue;
    }
    int[] newArray = new int[arrayList.Count];
    int j = 0;
    while (j < newArray.Length)
    {
        newArray[j] = (int)arrayList[j];
        j++;
    }
    return newArray;
}
//生成新的数组
public static int[] SelectSort(int[] iArray)
{
    int[] newArray=new int[iArray.Length];
    for (int i = 0; i < newArray.Length; i++)
    {
        int smallestIndex = FindSmallest(iArray);
        newArray[i] = iArray[smallestIndex];
        iArray = RemoveListItem(iArray, smallestIndex);
    }
    return newArray;
}
```

```C#
//改变原有数组
public static int[] SelectSortArray(int[] iArray)
{
    int temp = 0;
    int i = 0;
    while (i < iArray.Length - 1)
    {
        int smallest = iArray[i];
        int smallestIndex = i;
        for(int j=i+1; j < iArray.Length; j++)
        {
            if (smallest > iArray[j])
            {
                smallest = iArray[j];
                smallestIndex = j;
            }
        }
        temp = iArray[i];
        iArray[smallestIndex] = temp;
        iArray[i] = smallest;
        i++;
    }
    return iArray;
}
```

### 4. 递归

**递归**就是套娃。

#### 4.1 基线条件和递归条件

由于递归函数调用自己，因此编写这样的函数时很容易出错，进而导致无限循环。例如，假设你要编写一个像下面这样倒计时的函数。  

编写递归函数时，必须告诉它何时停止递归。正因为如此， 每个递归函数都有两部分：**基线**
**条件**（ base case）和**递归条件**（ recursive case） 。递归条件指的是函数调用自己，而基线条件则
指的是函数不再调用自己，从而避免形成无限循环。  

#### 4.2 栈 Stack

栈是一种数据结构，它按照后进先出的原则存储数据，先进入的数据被压入栈底，最后的数据在栈顶，需要读数据的时候从栈顶开始弹出数据。

```C#
public static void CountDown(int number)
{
    if (number <= 0) return;
    else
    {
        Console.WriteLine(number);
        CountDown(number - 1);
    }
}
```


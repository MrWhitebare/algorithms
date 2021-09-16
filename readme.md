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
> ![image-20210916143911944](C:\Users\17669\Documents\MyWork\记录\算法\algorithms\IMG\binarySearch.png)

### 2. 大O表示法

大O表示法是一种特殊的表示法，指出了算法的速度有多快。

![](C:\Users\17669\Documents\MyWork\记录\算法\algorithms\IMG\compare.png)

随着元素数量的增加，二分查找需要的额外时间并不多，而简单查找需要的额外时间却很多。因此，随着列表的增长，二分查找的速度比简单查找快得多。 Bob以为二分查找速度为简单查找的15倍，这不对：列表包含10亿个元素时，为3300万倍。  

大$O$表示法指出了算法有多快。例如，假设列表包含$n$个元素。简单查找需要检查每个元素，因此需要执行$n$次操作。使用大$O$表示法，这个运行时间为$O(n)$。单位秒呢？没有——大$O$表示法指的并非以秒为单位的速度。 大$O$表示法让你能够比较操作数，它指出了算法运行时间的增速。  

为检查长度为$n$的列表，二分查找需要执行$log_2 n$次操作。大$O$表示为$O(\log_2 n)$

#### 2.1 一些常见的大$O$运行时间

下面按从快到慢的顺序列出了你经常会遇到的5种大O运行时间。  

- $O(log_2 n)$ 对数时间，这样的算法包括二分查找；

- $O(n)$ 线性时间，这样的算法包括简单查找；

- $O(n*\log_2 n)$ 这样的算法包括快速排序；

- $O(n^2)$ 这样的算法包括选择排序；

- $O(n!)$  这样的算法包括旅行商问题的解决方案。

![算法运行时间](C:\Users\17669\Documents\MyWork\记录\算法\algorithms\IMG\time.png)

#### 2.2 旅行商问题

有一位旅行商需要前往5个城市。

![cities](C:\Users\17669\Documents\MyWork\记录\算法\algorithms\IMG\cities.png)

这位旅行商（姑且称之为Opus吧）要前往这5个城市，同时要确保旅程最短。为此，可考虑
前往这些城市的各种可能顺序。  

![](C:\Users\17669\Documents\MyWork\记录\算法\algorithms\IMG\order.png)

对于每种顺序，他都计算总旅程，再挑选出旅程最短的路线。 5个城市有120种不同的排列方式。因此，在涉及5个城市时，解决这个问题需要执行120次操作。涉及6个城市时，需要执行720次操作（有720种不同的排列方式）。涉及7个城市时，需要执行5040次操作！ 

![](C:\Users\17669\Documents\MyWork\记录\算法\algorithms\IMG\factorial.png)

### 3. 选择排序

#### 3.1 内存的工作原理

计算机就像是很多抽屉的集合体，每个抽屉都有地址。`fe0ffeeb`是一个内存单元的地址。    

![内存](C:\Users\17669\Documents\MyWork\记录\算法\algorithms\IMG\memory.png)

数组与链表操作的运行时间比较

|      | 数组   | 链表   |
| :--: | ------ | ------ |
| 读取 | $O(1)$ | $O(n)$ |
| 插入 | $O(n)$ | $O(1)$ |
| 删除 | $O(n)$ | $O(1)$ |


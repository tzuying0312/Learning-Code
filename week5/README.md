## Quick Sort 

## 簡介
快速排序使用分治法（Divide and conquer）策略來把一個序列（list）分為較小和較大的2個子序列，然後遞迴地排序兩個子序列。

## 運算流程
1.挑選基準值：從數列中挑出一個元素，稱為「基準」（pivot)。

基準值(Pivot)的選擇
* 固定位置：第一個數值、最後一個數值、中間的數值
* 亂數選擇
* 中位數

2.分割：重新排序數列，所有比基準值小的元素擺放在基準前面，所有比基準值大的元素擺在基準後面（與基準值相等的數可以到任何一邊。在這個分割結束之後，對基準值的排序就已經完成。

分割(Partition)：將數列依基準值分成三部份(快速排序作法中，第2,3步驟)
左子數列：比基準值小的數值
中子數列：基準值
右子數列：比基準值大的數值

3.遞迴排序子序列：遞迴地將小於基準值元素的子序列和大於基準值元素的子序列排序。

## 流程示意圖
![GITHUB](https://github.com/tzuying0312/Learning-Code/blob/master/photo/Quicksort.png)

## 時間複雜度
Best Case：Ο(n log n) 第一個基準值的位置剛好是中位數，將資料均分成二等份

Worst Case：Ο(n2) 當資料的順序恰好為由大到小或由小到大時，有分割跟沒分割一樣

Average Case：Ο(n log n)


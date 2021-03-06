## Merge Sort 

## 簡介
Merge Sort屬於Divide and Conquer演算法，把問題先拆解(divide)成子問題，並在逐一處理子問題後，將子問題的結果合併(conquer)。

## 運算流程
分為2個步驟:分割、合併

* 分割
1. 分割方法為:從長度的一半開始切割，分為左與右。
2. 不斷重複(1)，切至長度小於2停止。
3. 此時list中的元素只有1個。

* 合併
1. 合併的同時，比較大小。
2. 假如right元素中有[1,5]、left中有[3]。
3. 開時比較時，為left與right的第一位元素。
4. 有被變動到的list，下一回被比較的元素為第二位。
5. ex:right的1與left的3比較，因此下一位比較為5與3。

## 流程示意圖
![mergesort](https://github.com/tzuying0312/Learning-Code/blob/master/photo/mergesort.png)

## 學習歷程

藉由老師上課帶我們演練流程，因此打程式過程就知道會有左右兩個list需要比較，且比較時會有i+或j。
首先需要切割，參考了維基百科:

```python
def spilt(list):
    
    if len(list)<2:
        return list
    else:
        left=list[:len(list)//2]
        right=list[len(list)//2:]
        return merge_sort(spilt(left),spilt(right))
```
完成切割後，進入到合併:

```python
def merge_sort(left,right):
    while len(left)>0 and len(right)>0:
        done=[]
        i=0
        j=0
        if left[i]>right[j]:
            done.append(right[j])
            j+=1
            return merge_sort(left,right[j:])
        else:
            done.append(left[i])
            i+=1
            return merge_sort(left[i:],right)
           
```
    錯誤原因:TypeError: object of type 'NoneType' has no len()，while len(left)>0 and len(right)>0
    
```python
def merge_sort(left,right):
    done=[]
    i,j=0,0
    print(left[0],right[0])
    if left[i]>right[j]:
        done.append(right[j])
        j+=1
        return done+merge_sort(left,right[j:])
    else:
        done.append(left[i])
        i+=1
        return done+merge_sort(left[i:],right)
 ```
    錯誤原因:IndexError: list index out of range，print(left[0],right[0])
    
    上述原因皆是長度的問題，因此藉由i與j來跑，除此之外在return也有誤。
```python    
    def merge_sort(left,right):
        i=0
        j=0
        done=[]
        while i<len(left) and j<len(right) :

            if left[i]>right[j]:
                done.append(right[j])
                j+=1

            else:
                done.append(left[i])
                i+=1
    
        return done+left[i:]+right[j:]
 ```

###### 參考資料
[merge sort 維基百科](https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F#Python)
[merge sort 內容介紹](http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html)

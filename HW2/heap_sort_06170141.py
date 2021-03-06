class Solution(object):
    
    def heap_sort(self,mylist):
        self.mylist=mylist
        for i in range(len(mylist),-1,-1): #從最後開始比較至第一位
            root=i #root為1
            left=2*i+1 #root要比較的左右子節點
            right=2*i+2
            if left<len(mylist): #root若沒有左、右節點(代表left的值比mylist的長度大)，表示不用比較，反之需要。
                if mylist[root]>mylist[left]: #若mylist[root]的值比mylist[left]的值大，交換位置。
                    mylist[i],mylist[2*i+1]=mylist[2*i+1],mylist[i]
            if right<len(mylist):
                if mylist[root]>mylist[right]:
                    mylist[i],mylist[2*i+2]=mylist[2*i+2],mylist[i]
        return Solution().done(mylist) #當一輪結束後，list中第一位元素為最小的(排列完成)，將他丟至done。
    
    okay=[]#若此list放入done中，ok的list中，元素會不斷清空，因此放置在外。


    def done (self,mylist):
        ok=Solution().okay#取用Solution裡，def外的oky
        ok.append(mylist[0]) #由於第一位元素已是最小的，因此append至ok的list中。
        mylist[0]=mylist[-1] #最後一位會成為新的一位，在此最小的list被取代成最後一位。
        mylist.pop(-1) #已將最後一元素一至第一位，因此刪除最後
        
        #print(ok) 查看每次ok中被丟入的元素。
    
        if len(mylist)>0:
            mylist=Solution().heap_sort(mylist) #若mylist中還有元素，則丟回heap_sort。
        elif len(mylist)==0:
            print(ok)
            ok.clear() #若ok沒有清空，下一次跑時，將會繼續append到此後面

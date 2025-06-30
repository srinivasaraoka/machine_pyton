"auther:srinivas"
import logging
import logger

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class BST:
    def __init__(self, key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def insert(self,data):  #self.key means root.key
        if self.key==data:
            return
        if self.key==None:
            self.key=data
            return
        if self.key>data:
            if self.lchild:
                self.lchild.insert(data)                   
            else:
                self.lchild=BST(data) 
        else :
            if self.rchild:
                self.rchild.insert(data)                   
            else:
                self.rchild=BST(data)   
    def search(self,data):
        if self.key == data:
            print(f"given node {data} is found")  
            return  
        if self.key>data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print('given node not found')  
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print('given node not found')    
    def search_1(self,data, curr):
        if self.key == data:
            print(f"given node {data} {curr} is found")  
            print(curr)
            return curr 
        if self.key>data:
            if self.lchild:
                curr= self.lchild
                print(curr)
                self.lchild.search_1(data, curr )
            else:
                print('given node not found')  
        else:
            if self.rchild:
                curr= self.rchild
                self.rchild.search_1(data, curr)
            else:
                print('given node not found')   
                
    def serliaze(self, curr):
        result=[]
        print(curr)
        if not curr:
            return []
        queue= [curr]
        while queue:
            node= queue.pop(0) 
            if node:
                result.append(node.key)  
                queue.append(node.lchild)
                queue.append(node.rchild)
            else:
                result.append(None)
        while result and result[-1] is None:
            result.pop()        
        return result                                
                                            
    def pre_order_trans(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.pre_order_trans()
        if self.rchild: #restrart the excution once lchild is nono, squre up the lchild and then go to rchild
            self.rchild.pre_order_trans()    
    
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorder()
    def postorder(self):
        if self.lchild:
            self.lchild.inorder()
        if self.rchild:
            self.rchild.inorder()
        print(self.key, end=" ")
        
    def delete(self,data, curr):
        if self.key is None:
            print("tree epmty")
            return
        if data < self.key:
            if self.lchild:
                self.lchild= self.lchild.delete(data)
            else:
                print("given node not found")    
        elif data > self.key:
            if self.rchild:
                self.rchild= self.rchild.delete(data)
            else:
                print("node  not found") 
        else:
            #below twon codition cover deleet both single child or zero childs 
            if self.lchild is None:
                #for root node if it have only one child
                temp=self.rchild
                if data==curr:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild= temp.rchild
                    temp= None
                    return 
                self= None
                return temp
            if self.rchild is None:
                temp= self.lchild
                if data==curr:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild= temp.rchild
                    temp= None
                    return 
                self=None
                return temp               
            # node contais two childs 
            # two logics here, replace the parrent node with, node with largest key in left subtre
            # or
            # replace the parent node with, node with smallest key in right subtree
            # here we righting second option
            node = self.rchild
            while node.lchild:
                node =node.lchild
            self.key= node.key
            self.rchild= self.rchild.delete(node.key)
            return self  
    def min_key(self):
            current= self
            while self.lchild:
                current= current.lchild
            print(current.key) 
            
    def max_key(self):
            current= self
            while current.rchild:
                current= current.rchild
            print(current.key)   
                
          
def count(node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)                                     

root=BST(4)
count(root)
# logging.info(root.key)
# logging.info(root.lchild)
# logging.info(root.rchild)

# root.lchild=BST(5)
# logging.info(root.lchild.key)
# logging.info(root.lchild.lchild)
# logging.info(root.lchild.rchild)
# root.insert(2)
list1=[2,7,1,3]
for x in list1:
    root.insert(x)
#root.search(2)  
curr=root.search_1(2,root)  
print(curr)
z=root.serliaze(curr) 
print(z)
    
print('preorder')    
root.pre_order_trans() 
print('inorder')    
root.inorder() 
print('postorder')    
root.postorder() 
# print("deleteing calling")
# if count(root)>=1:
#     print(root.delete(96, root.key))
# else:
#     print("can't perform delete operation")    
root.postorder() 
'''
real time example for binary search tree is file system in operating system
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            for x in range(0,len(nums)):
                if nums[x]==target:
                    return x
        else:
            target_max=0
            target_min=0
            for x in range(0, len(nums)):
                if nums[x]> target:
                    target_max= x
                    print(x, target_max)
                    return x
                    
            return x+1  


def search_insert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left  # Insertion point if not found
          

        

    
        
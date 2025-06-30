# Insertion Sort
def insertsort(lst1):
    for index in range(1, len(lst1)):
        current_value= lst1[index]
        pos= index
        while current_value < lst1[pos-1] and pos>0:
            lst1[pos]=lst1[pos-1] 
            pos= pos-1
        lst1[pos]= current_value    
    print(lst1)     
insertsort([4,10,3,25])


#selection sort
list1=[53, 4,5,75,0,5]
for i in range(len(list1)):
    min_value= min(list1[i:])
    min_index = list1.index(min_value, i) # here i is the starting index
    list1[i], list1[min_index]= list1[min_index], list1[i]
print(list1)  

#bubble sort  
list1=[53, 4,5,75,0]
for j in range(len(list1)):
    for i in range(len(list1)-1-j):
        if list1[i] > list1[i+1]:
            list1[i], list1[i+1]= list1[i+1], list1[i]
print(list1)

# quick sort
'''
1, select a pivot element
2, findout the correct position of the pivot element in the list by rearranging the list
3, divide the list based on the pivot element
4, sort the sub recursively
'''
list1=[53, 4,5,75,0]
def pivot_place(list1, first, last): # to get the correct position of the pivot element
    pivot = list1[first]
    left= first+1
    right= last
    while True:
        while left <= right and list1[left] <= pivot:
            left= left+1
        while left <= right and list1[right] >= pivot:
            right = right-1
        if left < right: # we took the pivot element as the first element, so we need to swap the pivot element with the right element
            break
        else:
            list1[left], list1[right] = list1[right], list1[left]

    list1[first], list1[right] = list1[right], list1[first]
    return right

def quicksort(list1, first, last):
    if first < last:
        p= pivot_place(list1, first, last)
        quicksort(list1, first, p-1)
        quicksort(list1, p+1, last)
quicksort(list1, 0, len(list1)-1)        

#merge sort
'''
1, split the unsorted list
2, compare each of elements and group them
3, repeat the step 2 untill list is merged the sorted 

'''
list1=[53, 4,5,75,0]
def merge_sort(list1):
    if len(list1)>1:
        mid=len(list1)//2
        left_sub_list=lst1[:mid]
        right_sub_list= list1[mid:]
        print(left_sub_list)
        print(right_sub_list)
        merge_sort(lift_sub_list)
        merge_sort(leght_sub_list)
        i=j=k=0    
    while i<len(left_sub_list) and j<len(right_sub_list) :
        if left_sub_list[i] < right_sub_list[j]:
            list1[k]=left_sub_list[i]
            i=i+1  
            k=k+1 
        else:
            list1[k]=right_sub_list[j]
            j+=1
            k+=1  
    while i<len(left_sub_list):
        list1[k]=left_sub_list[i]
        i+=1
        k+=1
    while j< len(right_sub_list): 
        list1[k]=right_sub_list[j]
        j+=1
        k+=1
merge_sort(list1)
print(list1)

#insertion sort
list1=[53, 4,5,75,0]
for i in range(1, len(list1)):
    key = list1[i]
    j = i - 1
    while j >= 0 and key < list1[j]:
        list1[j + 1] = list1[j]
        j -= 1
    list1[j + 1] = key
print(list1)

#shell sort
'varriation of insertion sort, used for large list'
'by breaking the original list into a number of smaller sublists, each sublist is sorted using the insertion sort'
'it will move the items nearer to its original index'
'''
1, take the list of numbers
2,findout the gap/incrementor
3, create the sublist based on gap and sort them using insertion sort algorithm
4, reduce the gap and repeat step 3
5.stop when gap is 0

'''
list1=[54,26,93,17,77,31,44,55,20]
def Shellsort(alist):
    gap=len(alist)//2
    while gap>0:
        for i in range(gap, )
        




#liner search


#binary search



#my algardham
list1=[53, 4,5,75,0]
list2=[]
min_value= min(list1)
list2.append(min_value)
for i in range(1, max(list1)+1):
    z= min_value+i
    if z in list1:
        list2.append(z)
print(list2)        
    
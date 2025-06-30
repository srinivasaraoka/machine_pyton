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
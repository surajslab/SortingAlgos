

def quick_sort(arr):

    if(len(arr)<=1):
        return arr
    else:
        pivot=arr.pop()
    
    left=[]
    right=[]

    for i in arr:
        if i<pivot:
            left.append(i)
        
        else:
            right.append(i)
    
    return quick_sort(left)+[pivot]+quick_sort(right)


arr=[5,4,3,2,1]
print(quick_sort(arr))

    

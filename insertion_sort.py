

def insertion_sort(arr):

    leng=len(arr)
    
    for i in range(1,leng):
        for j in range(i-1,-1,-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            else:
                break

arr=[4,3,2]
insertion_sort(arr)
print(arr)



def merge_sort(arr,start,end):

    if(start<end):

        mid= (start+end)//2

        merge_sort(arr,start,mid)
        merge_sort(arr,mid+1,end)
        merge(arr,start,end)
    


def merge(arr,left,right):

    mid = (left+right)//2

    l_count=left
    temp=[]
    i=left
    j=mid+1


    while(i<=mid and j<=right):
        if arr[i]<arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1
    
    while(i<=mid):
        temp.append(arr[i])
        i+=1

    while(j<=right):
        temp.append(arr[j])
        j+=1

    i=0

    for i in range(len(temp)):
        arr[l_count]=temp[i]
        l_count+=1


arr=[2,1,4,5,7,9,8,3,3]
merge_sort(arr,0,len(arr)-1)

print(arr)



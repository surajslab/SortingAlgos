


def bubble(arr):

    leng=len(arr)-1

    for i in range(leng):
        for j in range(0,leng-i):

            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr=[4,3,2,1]
bubble(arr)

print(arr)
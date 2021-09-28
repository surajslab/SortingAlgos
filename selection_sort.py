

def selection(arr):

    leng=len(arr)

    for i in range(leng):
        minel=arr[i]
        minin=i

        for j in range(i+1,leng):
            if(arr[j]<minel):
                minin=j

        arr[i],arr[minin]=arr[minin],arr[i]

arr=[5,4,3,2,1]
selection(arr)
print(arr)


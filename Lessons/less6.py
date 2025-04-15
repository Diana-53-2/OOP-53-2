
def get_element(arr,index):
    return arr[index]

print(get_element([1,2,3,4,5,6,7,8,6,45,43,5,], 5))




def binary_search(arr,target):
    left, right = 0, len(arr) -1

    while left <= right:
       mid = (left+right)//2
       if arr[mid] == target:
           return mid
       elif arr[mid] < target:
           left = mid +1
       else:
           right = mid -1
       return -1
arr = [1,3,6,34,32,9,8]
target = 34
print (binary_search(arr,target))


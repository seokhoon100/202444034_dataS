import array

arr = array.array('f',[99, 8, -7, 0, 16])

for i in range(len(arr)):
    print(f"{arr[i]:3} {id(arr[i])}")












words = ['eat','ate','this','hist','that','your mum','racecar','carrace','eta']
sorted = []

def insertionSort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return ''.join(arr)

for i in words:
    split = list(i)
    sorted.append(insertionSort(split))

dict = {}
for i in range(len(sorted)):
    if sorted[i] not in dict:
        dict[sorted[i]] = [words[i]]
    else:
        dict[sorted[i]] = dict[sorted[i]] + [words[i]]
    print(dict[sorted[i]])    
print(dict)

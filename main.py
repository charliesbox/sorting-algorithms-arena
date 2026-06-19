import random
data = random.sample(range(1, int(input('max list value: ')) + 1), int(input('amount of samples: ')))


def check(data):
    loop = 0
    result = True
    for i in range(len(data) - 1):
        if data[loop] < data[loop + 1]:
            loop += 1
            continue
        if data[loop] > loop[data + 1]:
            result = False
            break
    if result != False:
        print('list is sorted.')
    else:
        print('list is NOT sorted.')


def bubblesort(data):
    dataset = data.copy()
    ci = 0
    changesmade = True
    comparisons = 0
    swaps = 0
    while changesmade:
        changesmade = False
        while ci < len(dataset) - 1:
            if dataset[ci] < dataset[ci + 1]:
                comparisons += 1
                pass
            if dataset[ci] > dataset[ci + 1]:
                dataset[ci+1], dataset[ci] = dataset[ci], dataset[ci+1]
                changesmade = True
                comparisons += 1
                swaps += 1
                pass
            ci += 1
        ci = 0
    check(dataset)
    print(f'BUBBLE SORT\ncomparisons made: {comparisons}, swaps made: {swaps}\ntotal operations: {comparisons + swaps}\n')


def brokeninsert(data):
    dataset = data.copy()
    mydata = []
    comparisons = 0
    insertions = 0
    while len(dataset) > 0:
        buffer = dataset[0]
        dataset.pop(0)
        ci = 0
        while True:
            if ci >= len(mydata) - 1:
                mydata.insert(ci + 1, buffer)
                comparisons += 1
                insertions += 1
                break
            if buffer > mydata[ci]:
                ci += 1
                comparisons +=1
                pass
            if buffer < mydata[ci]:
                mydata.insert(ci, buffer)
                comparisons +=1
                insertions += 1
                break
    check(dataset)
    print(f'BROKEN INSERTION SORT\ncomparisons made: {comparisons}, insertions made: {insertions}\ntotal operations: {comparisons + insertions}\n')


def insertionsort(data):
    dataset = data.copy()
    si = 0
    comp = 0
    insertions = 0
    while si < len(dataset) - 1:
        if dataset[si + 1] > dataset[si]:
            si += 1
            comp += 1
            insertions += 1
            continue
        if dataset[si + 1] < dataset[si]:
            key = dataset[si + 1]
            dataset[si + 1] = dataset[si]
            comp += 1
            passes = 0
            while True:
                if dataset[si - passes - 1] < key and si - passes - 1 >= 0:
                    dataset[si - passes] = key
                    si += 1
                    comp += 1
                    insertions += 1
                    break
                if dataset[si - passes - 1] > key and si - passes - 1 >= 0:
                    dataset[si - passes] = dataset[si - passes - 1] 
                    passes += 1
                    comp += 1
                    continue
                else:
                    dataset[0] = key
                    si += 1
                    comp += 1
                    insertions += 1
                    break
    check(dataset)
    print(f'INSERTION SORT\ncomparisons made: {comp}, insertions made: {insertions}\ntotal operations: {comp + insertions}\n')


def selectionsort(data):
    comparisons = 0
    swaps = 0
    dataset = data.copy()
    unsi = 0
    for i in range(len(dataset)):
        smallest = dataset[unsi]
        for i in range(len(dataset) - unsi):
            if dataset[unsi + i] > smallest:
                comparisons += 1
                i += 1
                continue
            if dataset[unsi + i] < smallest:
                smallest = dataset[unsi + i]
                comparisons += 1
                i += 1
                continue
        dataset[dataset.index(smallest)] = dataset[unsi]
        dataset[unsi] = smallest
        swaps += 1
        unsi += 1
    check(dataset)
    print(f'SELECTION SORT\ncomparisons made: {comparisons}, swaps made: {swaps}\ntotal operations: {comparisons + swaps}\n')


print(data)
bubblesort(data)
brokeninsert(data)
insertionsort(data)
selectionsort(data)
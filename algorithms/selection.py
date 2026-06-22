from algorithms.check import check

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
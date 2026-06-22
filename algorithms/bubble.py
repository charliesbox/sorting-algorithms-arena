from algorithms.check import check

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
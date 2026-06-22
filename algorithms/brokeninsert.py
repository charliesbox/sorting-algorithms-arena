from algorithms.check import check

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
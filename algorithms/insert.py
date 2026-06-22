from algorithms.check import check

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
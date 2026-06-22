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
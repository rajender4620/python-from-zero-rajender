def get_unique_items(items):
    uniqueList = []
    # print(uniqueList)

    # for item in items:
    #     if item not in uniqueList:
    #         uniqueList.append(item)

    for item in items:
        if item not in uniqueList:
            uniqueList.append(item)

    return uniqueList


result = get_unique_items(["a", "b", "a", "c", "b"])
print(result)


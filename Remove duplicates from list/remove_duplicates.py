#Write a function to remove duplicates from a list while preserving order.

def remove_duplicates(items):
    result = []
    for item in items:
        if item in result:
            continue
        result.append(item)
    return result
print(remove_duplicates([1,2,3,4,5,2,3,6]))
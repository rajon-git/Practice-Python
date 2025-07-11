#Problem: Write a function to find all pairs in a list that sum up to a given value.

def find_pairs(items,target):
    seen = set()
    pairs = []
    
    for num in items:
        complement = target - num
        if complement in seen:
            pairs.append((complement,num))
        seen.add(num)
        
    return pairs

print(find_pairs([1,2,3,4,5,6],6))
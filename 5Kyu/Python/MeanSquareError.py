def solution(array_a:list, array_b:list):
    length = len(array_a)
    res = []
    for duo in zip(array_a, array_b):
        res.append((duo[1] - duo[0]) ** 2)
    return sum(res)/length

    
    
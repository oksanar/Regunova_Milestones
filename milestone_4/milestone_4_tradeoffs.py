from typing import List, Tuple

def find_sum(target: int, li: List[int]) -> Tuple[int, int]:
    result = []
    for i in range(0, len(li)):
        for j in range(i, len(li)):
            if li[i] + li[j] == target:
                result.append((li[i], li[j]))
    return result

def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:
    result = []
    num_set = set()
    for n in li:
        current_n = target - n
        if current_n in num_set:
            result.insert(0, (current_n, n))
        else:
            num_set.add(n)

    return result

li = [0, 1, 2, 3, 4, 5]
target = 5
print(f"target: {target}, li: {li}")
print(find_sum(target, li))
print("The complexity of our algorithm: O(n^2)")
print(find_sum_fast(target, li))
print("The complexity of our algorithm: O(n)")

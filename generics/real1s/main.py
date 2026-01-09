"""
Mock Problem: Balanced Sampling from Classes

You are given a labeled dataset with multiple classes, where each example belongs to exactly one class.

You want to randomly sample n total examples such that the sample is as balanced as possible across classes (i.e., the difference between the number of sampled examples from any two classes is minimized), while not exceeding the available examples in each class.

inputs:
n = 10
class_counts = {
    "cat": 6,
    "dog": 4,
    "bird": 8
}

output:
{
    "cat": 3,
    "dog": 3,
    "bird": 4
}

Task

Write a function that returns how many examples to sample from each class, such that:

The total samples sum to n

No class is sampled more than its available count

The class distribution is as balanced as possible
"""

import heapq

def find_samples(n: int, class_counts: dict) -> dict:
    final = {k: 0 for k in class_counts}
    num_classes = len(class_counts)

    class_avg = n // num_classes
    for k in class_counts:
        take = min(class_avg, class_counts[k])
        final[k] = take
        n -= take

    # only min heaps in python so store negatives
    heap = []
    for k in class_counts:
        rem = class_counts[k] - final[k]
        if rem > 0:
            heapq.heappush(heap, (-rem, k))

    while n > 0 and heap:
        rem, k = heapq.heappop(heap)
        final[k] += 1
        n -= 1
        rem += 1  # since rem is negative
        if rem < 0:
            heapq.heappush(heap, (rem, k))

    return final


print(find_samples(10, {
    "cat": 6,
    "dog": 4,
    "bird": 8,
    "hippo": 7
}))
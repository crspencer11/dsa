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

def find_samples(n: int, class_counts: dict) -> dict:
    final = {}
    for k, v in class_counts.items():
        # find val average to even out distributuon
        val_avg = n // v
        print(val_avg)
        if val_avg > n:
            final[k] = v * val_avg
            print(final)
        else:
            final[k] = abs(n - val_avg)
        n -= val_avg
    return final

a = find_samples(10, {
    "cat": 6,
    "dog": 4,
    "bird": 8
})

print(a)
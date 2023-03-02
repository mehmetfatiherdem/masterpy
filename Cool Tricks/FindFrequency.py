### Count The Frequency of Items in a List Using The Collections Module ###

from collections import Counter

fruits = ["apple", "banana", "cherry", "apple", "banana", "apple"]

fruit_counts = Counter(fruits)

for fruit, count in fruit_counts.items():
    print(f"{fruit}: {count}")
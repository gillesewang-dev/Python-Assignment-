places = ["Tokyo", "Paris", "New York", "Dubai", "Sydney"]

print("Original list:",places)
print("Alphabetical order:",sorted(places))
print("Still original",places)
print("Reverse alphabetical order:",sorted(places, reverse=True))
print("Still original:",places)

places.reverse()
print("List after reverse():",places)

places.reverse()
print("Back to original:",places)

places.sort()
print("List after sort:",places)

places.sort(reverse=True)
print("Reverse alphabetical using sort():",places)
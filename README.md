## README

### Overview

This project contains two simple Python functions:

1. **`count_vowels(text)`**
   Counts how many vowels appear in a given string.

2. **`find_index(nums, target)`**
   Finds the index of a target value in a sorted list using **binary search (O(log n))**.

---

## 1) `count_vowels(text)`

### Purpose

`count_vowels` takes in a string and returns the total number of vowels inside it.

### Vowels counted

It counts these vowels:

* `a, e, i, o, u`

### How it works

* Goes through each character in the string
* Converts to lowercase so `A` counts as `a`
* Adds +1 when it sees a vowel
* Returns the final count

### Example

```python
count_vowels("Hello World")
# Output: 3
```

---

## 2) `find_index(nums, target)`

### Purpose

`find_index` searches for a number inside a **sorted** list and returns the index where it is found.

### Time Complexity

✅ Uses **binary search**, meaning the runtime is **O(log n)** because it repeatedly cuts the search range in half.

### Return values

* Returns the **index** if the target is found
* Returns **-1** if the target is not found

### Example

```python
find_index([1, 3, 5, 7, 9, 11], 11)
# Output: 5
```

---

## Running the Program

You can run the file using:

```bash
python your_file_name.py
```

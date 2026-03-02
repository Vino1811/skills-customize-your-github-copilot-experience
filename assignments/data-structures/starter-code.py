# Starter Code for 'Data Structures in Python' assignment

def get_unique_items(lst):
    """Return a list of unique items from lst preserving first-seen order."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def tuple_to_list(t):
    """Convert a tuple to a list."""
    return list(t)


def count_frequencies(items):
    """Return a dict mapping each item to its frequency."""
    freqs = {}
    for it in items:
        freqs[it] = freqs.get(it, 0) + 1
    return freqs


def merge_dicts(d1, d2):
    """Return a new dict merging d1 and d2; d2 values override d1."""
    merged = d1.copy()
    merged.update(d2)
    return merged


def set_operations(a, b):
    """Return dict with union, intersection, and difference (a - b)."""
    return {
        'union': a | b,
        'intersection': a & b,
        'difference': a - b
    }


if __name__ == '__main__':
    # Example usages — students can expand these or write tests
    sample_list = [1, 2, 2, 3, 1, 4]
    print('Unique items:', get_unique_items(sample_list))

    sample_tuple = (10, 20, 30)
    print('Tuple to list:', tuple_to_list(sample_tuple))

    items = ['apple', 'banana', 'apple', 'orange', 'banana']
    print('Frequencies:', count_frequencies(items))

    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 3, 'c': 4}
    print('Merged dict:', merge_dicts(d1, d2))

    A = {1, 2, 3}
    B = {2, 3, 4}
    ops = set_operations(A, B)
    print('Union:', ops['union'])
    print('Intersection:', ops['intersection'])
    print('Difference (A - B):', ops['difference'])

#In this assignment, you will build a Rotate My Scores program using Python arrays/lists. They will reverse scores using two pointers, reverse elements in fixed-size groups, perform left rotation by 1, perform left rotation by n, and find leaders in an array by scanning from the right side.
def reverse_array(scores):
    left = 0
    right = len(scores) - 1
    while left < right:
        scores[left], scores[right] = scores[right], scores[left]
        left += 1
        right -= 1
    return scores
def reverse_in_groups(scores, k):
    n = len(scores)
    if k <= 1:
        return scores
    for i in range(0, n, k):
        left = i
        right = min(i + k - 1, n - 1)
        while left < right:
            scores[left], scores[right] = scores[right], scores[left]
            left += 1
            right -= 1
    return scores
def left_rotate_by_one(scores):
    if not scores:
        return scores
    first_element = scores[0]
    for i in range(1, len(scores)):
        scores[i - 1] = scores[i]
    scores[-1] = first_element
    return scores
def left_rotate_by_n(scores, n_rotations):
    length = len(scores)
    if length == 0:
        return scores
    n_rotations = n_rotations % length
    def reverse_sub(arr, start, end):
        while start < end:
            arr[start], arr[end], arr[start]
            start += 1
            end -= 1
    reverse_sub(scores, 0, n_rotations - 1)
    reverse_sub(scores, n_rotations, length - 1)
    reverse_sub(scores, 0, length - 1)
    return scores
def find_leaders(scores):
    if not scores:
        return []
    leaders = []
    current_max = scores[-1]
    leaders.append(current_max)
    for i in range(len(scores) -2, -1, -1):
        if scores[i] > current_max:
            current_max = scores[i]
            leaders.append(current_max)
    leaders.reverse()
    return leaders
if __name__ == "__main__":
    print("=== Rotate My Scores Program ===\n")

    test_scores = [10,20,30,40,50]
    print(f"Original: {test_scores}")
    print(f"✅ Reversed (Two-Pointer): {reverse_array(test_scores.copy())}\n")

    test_scores = [1,2,3,4,5,6,7,8]
    k_size = 3
    print(f"Original: {test_scores}")
    print(f"✅ Reversed in groups of {k_size}: {reverse_in_groups(test_scores.copy(), k_size)}\n")

    test_scores = [11,22,33,44,55]
    print(f"Original: {test_scores}")
    print(f"✅ Left rotated by 1: {left_rotate_by_one(test_scores.copy())}\n")

    test_scores = [10,20,30,40,50,60,70]
    rotations = 3
    print(f"Original: {test_scores}")
    print(f"✅ Left rotated by {rotations}: {left_rotate_by_n(test_scores.copy(), rotations)}\n")

    test_scores = [16,17,4,3,5,2]
    print(f"Original: {test_scores}")
    print(f"✅ Leaders found: {find_leaders(test_scores)}")
import unittest


# PROGRAM BELOW
def count_distanced_prefix_sums(prefix_sum_array: [int], array_len: int, distance: int) -> int:
    count = 0
    r_pointer = 1
    for l_pointer in range(array_len - 1):
        while r_pointer < array_len - 1 and prefix_sum_array[r_pointer] - prefix_sum_array[l_pointer] <= distance:
            r_pointer += 1
        if prefix_sum_array[r_pointer] - prefix_sum_array[l_pointer] <= distance:
            break
        count += array_len - r_pointer
    return count


if __name__ == "__main__":
    landmark_count, min_distance = list(map(int, input().split(" ")))
    landmark_distance_prefix_sum = list(map(int, input().split(" ")))
    print(count_distanced_prefix_sums(landmark_distance_prefix_sum, landmark_count, min_distance))


# PROGRAM ABOVE
# TESTING BELOW
'''
class ProgramTester(unittest.TestCase):
    def test_1(self):
        landmark_arr, distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 10
        count = count_distanced_prefix_sums(landmark_arr, len(landmark_arr), distance)
        self.assertEqual(1, count)

    def test_2(self):
        landmark_arr, distance = [1, 3, 5, 8], 4
        count = count_distanced_prefix_sums(landmark_arr, len(landmark_arr), distance)
        self.assertEqual(2, count)

    def test_3(self):
        landmark_arr, distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000, 2000], 100
        count = count_distanced_prefix_sums(landmark_arr, len(landmark_arr), distance)
        self.assertEqual(21, count)


if __name__ == "__main__":
    unittest.main()
'''

import unittest


# PROGRAM BELOW
def get_min_apparel(blue_shirts: int, red_shirts: int, blue_socks: int, red_socks: int) -> [int]:
    # If we have 0 of something then our set is defined
    if blue_shirts == 0:
        return [1, blue_socks + 1]
    if red_shirts == 0:
        return [1, red_socks + 1]
    if blue_socks == 0:
        return [blue_shirts + 1, 1]
    if red_socks == 0:
        return [red_shirts + 1, 1]
    # We can try taking every color of one apparel to only draw once from the other drawer
    # If it will be less actions than getting defined outcome
    shirts_for_random_set = max(blue_shirts, red_shirts) + 1
    socks_for_random_set = max(blue_socks, red_socks) + 1
    if shirts_for_random_set <= socks_for_random_set:
        if shirts_for_random_set + 1 <= min(blue_shirts + blue_socks, red_shirts + red_socks) + 2:
            return [shirts_for_random_set, 1]
    else:
        if socks_for_random_set + 1 <= min(blue_shirts + blue_socks, red_shirts + red_socks) + 2:
            return [1, socks_for_random_set]
    # By drawing color+1 of one clothes type we can 100% get clothes of other color
    if blue_shirts + blue_socks >= red_shirts + red_socks:
        return [red_shirts + 1, red_socks + 1]
    return [blue_shirts + 1, blue_socks + 1]


if __name__ == '__main__':
    min_apparel = get_min_apparel(int(input()), int(input()),
                                  int(input()), int(input()))
    print(min_apparel[0], min_apparel[1])


# PROGRAM ABOVE
# TESTING BELOW
class ProgramTester(unittest.TestCase):

    def test_all_present(self):
        blue_shirts, red_shirts, blue_socks, red_socks = 6, 2, 7, 3
        testing_min_apparel = get_min_apparel(blue_shirts, red_shirts, blue_socks, red_socks)
        print(f"Синие майки: {blue_shirts}, Красные майки: {red_shirts}\n"
              f"Синие носки: {blue_socks}, Красные носки: {red_socks}")
        self.assertEqual([3, 4], testing_min_apparel)

    def test_no_blue_socks(self):
        blue_shirts, red_shirts, blue_socks, red_socks = 6, 2, 0, 3
        testing_min_apparel = get_min_apparel(blue_shirts, red_shirts, blue_socks, red_socks)
        print(f"Синие майки: {blue_shirts}, Красные майки: {red_shirts}\n"
              f"Синие носки: {blue_socks}, Красные носки: {red_socks}")
        self.assertEqual([7, 1], testing_min_apparel)

    def test_no_red_socks(self):
        blue_shirts, red_shirts, blue_socks, red_socks = 6, 2, 7, 0
        testing_min_apparel = get_min_apparel(blue_shirts, red_shirts, blue_socks, red_socks)
        print(f"Синие майки: {blue_shirts}, Красные майки: {red_shirts}\n"
              f"Синие носки: {blue_socks}, Красные носки: {red_socks}")
        self.assertEqual([3, 1], testing_min_apparel)

    def test_no_blue_shirts(self):
        blue_shirts, red_shirts, blue_socks, red_socks = 0, 2, 7, 3
        testing_min_apparel = get_min_apparel(blue_shirts, red_shirts, blue_socks, red_socks)
        print(f"Синие майки: {blue_shirts}, Красные майки: {red_shirts}\n"
              f"Синие носки: {blue_socks}, Красные носки: {red_socks}")
        self.assertEqual([1, 8], testing_min_apparel)

    def test_no_red_shirts(self):
        blue_shirts, red_shirts, blue_socks, red_socks = 6, 0, 7, 3
        testing_min_apparel = get_min_apparel(blue_shirts, red_shirts, blue_socks, red_socks)
        print(f"Синие майки: {blue_shirts}, Красные майки: {red_shirts}\n"
              f"Синие носки: {blue_socks}, Красные носки: {red_socks}")
        self.assertEqual([1, 4], testing_min_apparel)

    def test_no_blue_apparel(self):
        blue_shirts, red_shirts, blue_socks, red_socks = 0, 2, 0, 3
        testing_min_apparel = get_min_apparel(blue_shirts, red_shirts, blue_socks, red_socks)
        print(f"Синие майки: {blue_shirts}, Красные майки: {red_shirts}\n"
              f"Синие носки: {blue_socks}, Красные носки: {red_socks}")
        self.assertEqual([1, 1], testing_min_apparel)

    def test_no_red_apparel(self):
        blue_shirts, red_shirts, blue_socks, red_socks = 6, 0, 7, 0
        testing_min_apparel = get_min_apparel(blue_shirts, red_shirts, blue_socks, red_socks)
        print(f"Синие майки: {blue_shirts}, Красные майки: {red_shirts}\n"
              f"Синие носки: {blue_socks}, Красные носки: {red_socks}")
        self.assertEqual([1, 1], testing_min_apparel)

    def test_all_present_socks_reversed(self):
        blue_shirts, red_shirts, blue_socks, red_socks = 6, 2, 3, 7
        testing_min_apparel = get_min_apparel(blue_shirts, red_shirts, blue_socks, red_socks)
        print(f"Синие майки: {blue_shirts}, Красные майки: {red_shirts}\n"
              f"Синие носки: {blue_socks}, Красные носки: {red_socks}")
        self.assertEqual([7, 1], testing_min_apparel)

    def test_all_present_shirts_additional_0(self):
        blue_shirts, red_shirts, blue_socks, red_socks = 10000, 6, 20000, 3
        testing_min_apparel = get_min_apparel(blue_shirts, red_shirts, blue_socks, red_socks)
        print(f"Синие майки: {blue_shirts}, Красные майки: {red_shirts}\n"
              f"Синие носки: {blue_socks}, Красные носки: {red_socks}")
        self.assertEqual([7, 4], testing_min_apparel)

    def test_all_present_additional_1(self):
        blue_shirts, red_shirts, blue_socks, red_socks = 11000, 21000, 10, 10
        testing_min_apparel = get_min_apparel(blue_shirts, red_shirts, blue_socks, red_socks)
        print(f"Синие майки: {blue_shirts}, Красные майки: {red_shirts}\n"
              f"Синие носки: {blue_socks}, Красные носки: {red_socks}")
        self.assertEqual([1, 11], testing_min_apparel)

    def test_all_present_additional_2(self):
        blue_shirts, red_shirts, blue_socks, red_socks = 90000, 10, 11, 90000
        testing_min_apparel = get_min_apparel(blue_shirts, red_shirts, blue_socks, red_socks)
        print(f"Синие майки: {blue_shirts}, Красные майки: {red_shirts}\n"
              f"Синие носки: {blue_socks}, Красные носки: {red_socks}")
        self.assertEqual([90001, 1], testing_min_apparel)

    def test_all_present_additional_3(self):
        blue_shirts, red_shirts, blue_socks, red_socks = 90000, 11, 10, 90000
        testing_min_apparel = get_min_apparel(blue_shirts, red_shirts, blue_socks, red_socks)
        print(f"Синие майки: {blue_shirts}, Красные майки: {red_shirts}\n"
              f"Синие носки: {blue_socks}, Красные носки: {red_socks}")
        self.assertEqual([90001, 1], testing_min_apparel)

if __name__ == "__main__":
    unittest.main()

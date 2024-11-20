from collections import deque


if __name__ == "__main__":
    chair_count, height = list(map(int, input().split()))
    chair_list = sorted(
        zip(list(map(int, input().split())), list(map(int, input().split()))),
        key=lambda x: (x[0], x[1]))
    discomfort_deque = deque()
    min_discomfort = 10**9
    l_pointer = 0
    bed_variants = 0
    bed_width = 0
    for r_pointer in range(chair_count):
        bed_width += chair_list[r_pointer][1]
        if r_pointer > l_pointer and chair_list[r_pointer][0] != chair_list[r_pointer - 1][0]:
            current_discomfort = chair_list[r_pointer][0] - chair_list[r_pointer - 1][0]
            while discomfort_deque and discomfort_deque[-1] < current_discomfort:
                discomfort_deque.pop()
            discomfort_deque.append(current_discomfort)
        while bed_width >= height:
            if not discomfort_deque:
                min_discomfort = 0
            elif min_discomfort > discomfort_deque[0]:
                min_discomfort = discomfort_deque[0]
            if discomfort_deque and chair_list[l_pointer + 1][0] - chair_list[l_pointer][0] == discomfort_deque[0]:
                discomfort_deque.popleft()
            bed_width -= chair_list[l_pointer][1]
            l_pointer += 1
    print(min_discomfort)

if __name__ == "__main__":
    arr_i = sorted([[a, b, c, False] for a, b, c in zip(range(1, 1 + int(input())), list(map(int, input().split())), list(map(int, input().split())))], key=lambda x: (x[1], x[2], -x[0]), reverse=True)
    arr_u = sorted(arr_i, key=lambda x: (x[2], x[1], -x[0]), reverse=True)
    ip = up = 0
    for i in list(map(int, input().split())):
        if i:
            while arr_u[up][3]:
                up += 1
            print(arr_u[up][0])
            arr_u[up][3], up = 1, up + 1
        else:
            while arr_i[ip][3]:
                ip += 1
            print(arr_i[ip][0])
            arr_i[ip][3], ip = 1, ip + 1

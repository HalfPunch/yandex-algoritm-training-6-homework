if __name__ == "__main__":
    clue_count = int(input())
    clues = [[clue_weight, 1] for clue_weight in list(map(int, input().split()))]
    experiment_count, adhd_endurance = list(map(int, input().split()))
    current_endurance = adhd_endurance
    last_uncertain_clue_pointer = clue_count - 1
    experiments = list(map(int, input().split()))
    if clue_count == 1:
        print(" ".join(["1" for _ in range(experiment_count)]))
    else:
        for i in range(clue_count - 1, 0, -1):
            if clues[i - 1] > clues[i]:
                while last_uncertain_clue_pointer != i - 1:
                    clues[last_uncertain_clue_pointer][1] = i + 1
                    last_uncertain_clue_pointer -= 1
                current_endurance = adhd_endurance
            elif clues[i - 1] == clues[i]:
                if current_endurance == 0:
                    while clues[last_uncertain_clue_pointer - 1] != clues[last_uncertain_clue_pointer]:
                        clues[last_uncertain_clue_pointer][1] = i + 1
                        last_uncertain_clue_pointer -= 1
                    clues[last_uncertain_clue_pointer][1] = i + 1
                    last_uncertain_clue_pointer -= 1
                else:
                    current_endurance -= 1
        print(" ".join(map(str, [clues[experiment - 1][1] for experiment in experiments])))

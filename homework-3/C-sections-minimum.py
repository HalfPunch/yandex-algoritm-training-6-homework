if __name__ == "__main__":
    array_length, section_length = list(map(int, input().split()))
    array = list(map(int, input().split()))
    # Deck init
    deck = []
    for element_id in range(section_length):
        while deck and array[element_id] < deck[-1]:
            deck.pop()
        deck.append(array[element_id])
    print(deck[0])
    # Moving window
    for element_id in range(array_length - section_length):
        if array[element_id] == deck[0]:
            deck.pop(0)
        while deck and array[element_id + section_length] < deck[-1]:
            deck.pop()
        deck.append(array[element_id + section_length])
        print(deck[0])

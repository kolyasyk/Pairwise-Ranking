import itertools


def compare_pair(pair):
    print(f"1: {pair[0]}")
    print(f"2: {pair[1]}")
    choice = input("Which do you prefer? Type 1 or 2: ")
    return pair[0] if choice == '1' else pair[1]


def pairwise_comparison(items):
    # Generate all unique pairs of items
    pairs = list(itertools.permutations(items, 2))

    # Dictionary to keep track of wins
    results = {item: 0 for item in items}

    # Loop through each pair, display them, and record user's choice
    for pair_number, pair in enumerate(pairs):
        print(f" --- {pair_number + 1}/{len(pairs)} --- \n")
        winner = compare_pair(pair)
        results[winner] += 1
        print(f"You preferred {winner}.\n")

    # Print final results
    print("Final Preferences:")
    for item, score in sorted(results.items(), key=lambda x: x[1], reverse=True):
        print(f"{item}: {score} wins")


def load_list(list_name: str) -> [str]:
    options: [str] = []
    with open(f"../data/{list_name}.txt") as f:
        options = f.readlines()
        options = [o.strip() for o in options if not o.startswith("-")]
    return options


def main():
    list_name: str = "Achievement"
    # list_name: str = "Fruit"
    options: [str] = load_list(list_name=list_name)
    pairwise_comparison(options)


if __name__ == "__main__":
    main()
